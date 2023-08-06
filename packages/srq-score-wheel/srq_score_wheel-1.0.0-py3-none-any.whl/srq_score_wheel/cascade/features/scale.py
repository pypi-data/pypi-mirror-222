import sys
import os
# sys.path.append('/Workspace/Repos/developers@sowntogrow.com/sown-ml-2023/wheel_development')
# from srq_score_wheel.env_setup import RESOURCE_PATH_ABS, ENV               

RESOURCE_PATH_ABS = "/dbfs/mnt/sown-ai-resources"
RESOURCE_PATH = "dev_resources"
ENV = "dev"

sys.path.append(os.path.abspath(RESOURCE_PATH_ABS))

from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd

# Import resources based on env
if ENV == 'dev':
    import dev_resources as mod
elif ENV == 'prod':
    import prod_resources as mod

def scale_features(data, model_type, train_flag):
    non_scale_cols_present = [c for c in mod.NON_SCALE_COLS if c in data.columns]
    scale_path = f"{mod.PROD_MODEL_PATH_1}/Scalar_{model_type}.joblib"
    data_to_not_scale = data[non_scale_cols_present]
    data_to_scale = data.drop(non_scale_cols_present, axis=1)
    if train_flag == 1:
        scaler = StandardScaler()
        scaler.fit(data_to_scale)
        data_scaled = scaler.transform(data_to_scale)
        joblib.dump(scaler, scale_path)
    else:
        scaler = joblib.load(scale_path)
        data_scaled = scaler.transform(data_to_scale)
    data_scaled = pd.DataFrame(
        data=data_scaled, index=data_to_scale.index, columns=data_to_scale.columns)
    data_scaled[non_scale_cols_present] = data_to_not_scale

    return data_scaled