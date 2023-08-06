import sys
import os
# sys.path.append('/Workspace/Repos/developers@sowntogrow.com/sown-ml-2023/wheel_development')
# from srq_score_wheel.env_setup import (RESOURCE_PATH_ABS, ENV, PGUSER, PGHOST, PGDATABASE) 

RESOURCE_PATH_ABS = "/dbfs/mnt/sown-ai-resources"
RESOURCE_PATH = "dev_resources"
ENV = "dev"

sys.path.append(os.path.abspath(RESOURCE_PATH_ABS))

import pandas as pd

# Import resources based on env
if ENV == 'dev':
    import dev_resources as mod
elif ENV == 'prod':
    import prod_resources as mod

def append_model_features(data_features, model_features):
    
    data_combined = data_features.copy(deep=False)
    for features in model_features:
        data_combined = pd.merge(data_combined,
                                 features.loc[:, features.columns.str.contains(
                                     '|'.join(["Top", "id"]))], on=mod.REFLECTION_ID_COLS)

    return data_combined