import os

PROJECT_ROOT_PATH = os.path.abspath(os.path.join('../..'))

#@todo: why does it work for RAW_DATA_PATH, but not for RRAW_DATA_PATH
RAW_DATA_PATH='/Users/valeria/Google Drive/Valeria - Personal/projects/responsible_lending/responsible-lending/data/raw_loan_data.csv'
RRAW_DATA_PATH = os.path.join(PROJECT_ROOT_PATH, 'data/raw_loan_data.csv')
