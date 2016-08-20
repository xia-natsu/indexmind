# -*- coding: utf-8 -*-
# Reference: http://www.python-izm.com/contents/application/config.shtml
import configparser
import csv
import os
import pandas as pd

RUNTIME_ENV_KEY = 'indexmind.data.runtime.env'
config_file = configparser.ConfigParser()
env = os.getenv(key=RUNTIME_ENV_KEY,default='prod')
config_file.read("../../etc/config/{env}.ini".format(env=env))

##### Utils ######
def read_s3_credentials(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        cred = next(reader)
        return cred[0], cred[1], cred[2]


##### Parameters ######
# Settings
credential_path = config_file.get("settings", "aws_creds_file")
S3_ACCOUNT, S3_USERNAME, S3_PASSWORD = read_s3_credentials(credential_path)

# Data
FILE_SYSTEM = config_file.get("data", "fs")
DATA_ROOT = config_file.get("data", "data_root")

# List
def symbol_list(path):
    df = pd.read_csv(path)
    dfTrue = df[df['isActive']]
    return dfTrue.symbol.values
SYMBOL_LIST = symbol_list("../../etc/config/symbol.csv")

