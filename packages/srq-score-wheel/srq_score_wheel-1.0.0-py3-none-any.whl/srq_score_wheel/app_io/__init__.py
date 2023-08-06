import sys
import os
# sys.path.append('/Workspace/Repos/developers@sowntogrow.com/sown-ml-2023/wheel_development')
# from srq_score_wheel.env_setup import RESOURCE_PATH_ABS, RESOURCE_PATH, STG_ENV
RESOURCE_PATH_ABS = "/dbfs/mnt/sown-ai-resources"
RESOURCE_PATH = "dev_resources"
STG_ENV = "DEV"
from google.oauth2 import service_account

CREDENTIALS_FILE = RESOURCE_PATH_ABS + '/' + RESOURCE_PATH + f'/sown-translate-{STG_ENV.lower()}.json'

GOOGLE_TRANSLATE_API_CREDENTIALS = service_account \
                                   .Credentials \
                                   .from_service_account_file(CREDENTIALS_FILE)       