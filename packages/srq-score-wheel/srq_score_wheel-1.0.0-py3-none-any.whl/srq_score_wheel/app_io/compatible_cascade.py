import sys
import os
# sys.path.append('/Workspace/Repos/developers@sowntogrow.com/sown-ml-2023/wheel_development')
# from srq_score_wheel.env_setup import RESOURCE_PATH_ABS, ENV

RESOURCE_PATH_ABS = "/dbfs/mnt/sown-ai-resources"
RESOURCE_PATH = "dev_resources"
ENV = "dev"

sys.path.append(os.path.abspath(RESOURCE_PATH_ABS))

import json
import datetime
import pickle
import pandas as pd
import numpy as np
from scipy import stats
from googletrans import Translator
from google.cloud import translate_v2 as translate

# Import resources based on env
if ENV == 'dev':
    import dev_resources as mod
elif ENV == 'prod':
    import prod_resources as mod
    
from srq_score_wheel.app_io import GOOGLE_TRANSLATE_API_CREDENTIALS
from srq_score_wheel.cascade.models.predictions import get_predictions

EMPTY_TEXT = ""
EMPTY_GOAL_LEVEL = 99
PERF_REFLECTION_TYPE = 0
CYC_REFLECTION_TYPE = 1
WEEK_REFLECTION_TYPE = 2
EMPTY_ACTIVITY_TYPE = "unknown"
REFLECTION_DEFAULTS = {mod.GOAL_LEVEL_MODEL: EMPTY_GOAL_LEVEL,
                       mod.CONTENT_MODEL: EMPTY_TEXT,
                       mod.GOAL_NOTES_MODEL: EMPTY_TEXT,
                       mod.REFLECTION_TYPE_MODEL: PERF_REFLECTION_TYPE,
                       mod.ACTIVITY_TYPE_MODEL: EMPTY_ACTIVITY_TYPE}
EXCEPTION_DICT = pickle.load(open(mod.EXCEPTION_FILE_PATH, "rb"))
ENG_LANG_FILTER = pickle.load(open(mod.ENG_LANG_FILTER_PATH, "rb"))

def modify_all_reflections(reflections):
    return [modify_reflection(rename_column_names(reflection)) for reflection in reflections]


def modify_reflection(reflection):
    modified_reflection = replace_missing_values(
        add_missing_keys(reflection))
    modified_reflection[mod.ACTIVITY_TYPE_MODEL] = set_activity_type(
        modified_reflection)
    modified_reflection[mod.REFLECTION_TYPE_MODEL] = set_reflection_type(
        modified_reflection)
    return modified_reflection


def rename_column_names(reflection):
    return {key + '_model'
            if '_model' not in key
            else key: value
            for key, value in reflection.items()}


def add_missing_keys(reflection):
    reflection_all_keys = dict(REFLECTION_DEFAULTS)
    reflection_all_keys.update(reflection)
    return reflection_all_keys


def replace_missing_values(reflection):
    return {key: REFLECTION_DEFAULTS[key]
                 if value in (None, np.nan) and key in mod.REFLECTION_COLS_TO_KEEP
                 else value
            for key, value in reflection.items()}


def add_index(payload):
    for idx, sample in enumerate(payload["samples"]):
        for id_col in mod.REFLECTION_ID_COLS:
            sample[id_col] = idx
    return payload


def set_activity_type(reflection):
    # present for performance, missing for cycle and weekly
    if reflection[mod.REFLECTION_TYPE_MODEL] in ("cycle", CYC_REFLECTION_TYPE):
        return "cycle"
    if reflection[mod.REFLECTION_TYPE_MODEL] in ("weekly", WEEK_REFLECTION_TYPE):
        return "week"
    return reflection[mod.ACTIVITY_TYPE_MODEL]


def set_reflection_type(reflection):
    if reflection[mod.REFLECTION_TYPE_MODEL] == "cycle":
        return CYC_REFLECTION_TYPE
    if reflection[mod.REFLECTION_TYPE_MODEL] == "weekly":
        return WEEK_REFLECTION_TYPE
    return PERF_REFLECTION_TYPE


# pylint: disable=W0702
# No exception type(s) specified (bare-except)
def detect_language(payload):
    translator = Translator()
    client = translate.Client(credentials=GOOGLE_TRANSLATE_API_CREDENTIALS)
    for sample in payload["samples"]:
        sample = get_lang_and_trans(sample, client, translator)
    return payload


def get_lang_and_trans(sample, client, translator):
    default_to_eng_condition = (any(eng_word in ENG_LANG_FILTER
                                    for eng_word in sample[mod.CONTENT_COL].lower().split()) or
                                len(sample[mod.CONTENT_COL]) > mod.CHAR_LIMIT_CONST)
    if default_to_eng_condition:
        return default_eng_filter(sample)
    if EXCEPTION_DICT[mod.UNPAID_FLAG_KEY]:
        sample = unpaid_try_except(sample, translator)
    else:
        check_to_reset_unpaid_flag()
        sample = paid_try_except(sample, client)
    return sample


def default_eng_filter(sample):
    sample[mod.REFLECTION_INPUT_LANG] = mod.ENG_LANG_CONST
    sample[mod.REFLECTION_TRANSLATED_ENG] = sample[mod.CONTENT_COL]
    return sample


def paid_try_except(sample, client):
    try:
        sample[mod.REFLECTION_INPUT_LANG], sample[mod.REFLECTION_TRANSLATED_ENG] = (
            detect_language_paid(sample[mod.CONTENT_COL], client)
        )
    except:
        sample = set_lang_trans_for_exception(sample)
    return sample


def unpaid_try_except(sample, translator):
    try:
        sample[mod.REFLECTION_INPUT_LANG], sample[mod.REFLECTION_TRANSLATED_ENG] = (
            detect_language_unpaid(sample[mod.CONTENT_COL], translator)
        )
    except:
        sample = set_lang_trans_for_exception(sample)
        set_paid_flag()
    return sample


def set_lang_trans_for_exception(sample):
    sample[mod.REFLECTION_INPUT_LANG] = mod.LANG_NOT_FOUND_CONST
    sample[mod.REFLECTION_TRANSLATED_ENG] = sample[mod.CONTENT_COL]
    return sample


def set_paid_flag():
    EXCEPTION_DICT[mod.EXCEPTION_TIME_KEY] = datetime.datetime.now()
    EXCEPTION_DICT[mod.UNPAID_FLAG_KEY] = False
    LOGGER.info("Unpaid Flag set to False")
    with open(mod.EXCEPTION_FILE_PATH, "wb") as file:
        pickle.dump(EXCEPTION_DICT, file)


def check_to_reset_unpaid_flag():
    current_time = datetime.datetime.now()
    if (current_time-EXCEPTION_DICT[mod.EXCEPTION_TIME_KEY]).days >= 1:
        EXCEPTION_DICT[mod.UNPAID_FLAG_KEY] = True
        LOGGER.info("Unpaid Flag set to True")
    with open(mod.EXCEPTION_FILE_PATH, "wb") as file:
        pickle.dump(EXCEPTION_DICT, file)


def detect_language_paid(reflection_content, client):
    language = client.detect_language(reflection_content)["language"]
    if language == mod.ENG_LANG_CONST:
        return language, reflection_content
    return language, client.translate(reflection_content)["translatedText"]


def detect_language_unpaid(reflection_content, translator):
    language = translator.detect(reflection_content).lang
    translation = translate_reflection(reflection_content, language, translator)
    return language, translation


def translate_reflection(reflection, language, translator):
    if language in [mod.ENG_LANG_CONST, mod.LANG_NOT_FOUND_CONST]:
        return reflection
    return translator.translate(reflection).text


def format_predicted_output(payload, models, feature_dicts):
    data_original = pd.json_normalize(payload["samples"])
    data_modeling = pd.json_normalize(
        modify_all_reflections(payload["samples"]))
    if mod.REFLECTION_TRANSLATED_ENG in data_original.columns:
        data_modeling[mod.CONTENT_MODEL] = data_modeling[mod.REFLECTION_TRANSLATED_ENG + "_model"]

    cols_to_return = list(set(data_original.columns) - set(mod.REFLECTION_ID_COLS))
    data_pred = pd.merge(data_original,
                         predict_output(data_modeling, models, feature_dicts),
                         on=mod.REFLECTION_ID_COLS)
    cols_to_return.extend(["classification", "entropy"])
    payload["model_version"] = mod.LATEST_MODEL_VERSIONS["reflection_quality"]
    payload["samples"] = json.loads(data_pred[cols_to_return]
                                    .to_json(orient="records"))
    return payload


def predict_output(data_modeling, models, feature_dicts):
    cols = [c for c in mod.REFLECTION_COLS_TO_KEEP if c in data_modeling.columns]
    predictions = get_predictions(data_modeling[cols], models, feature_dicts)
    likelihoods = predictions[['RF_Prob_0', 'RF_Prob_1',
                               'RF_Prob_2', 'RF_Prob_3', 'RF_Prob_4']]
    predictions[[0, 1, 2, 3, 4]] = likelihoods.div(
        likelihoods.sum(axis=1), axis=0)
    predictions["classification"] = predictions[[0, 1, 2, 3, 4]].apply(
        lambda x: dict(enumerate(x.to_list())), axis=1)
    predictions["entropy"] = predictions[[0, 1, 2, 3, 4]].apply(
        lambda x: stats.entropy(x, base=2), axis=1)
    return predictions