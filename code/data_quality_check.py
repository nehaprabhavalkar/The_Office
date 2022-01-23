import pandas as pd 

DATA_PATH = '../data/'

def dq_on_imdb(df):
    check_row_count(df)
    check_null_values(df)

def dq_on_dialogues(df):
    check_row_count(df)
    check_null_values(df) 

def check_row_count(df):
    if len(df) > 0:
        print("Row count check is successful")

    else:
        raise Exception("Row count check has failed")

def check_null_values(df):
    if df.isnull().values.any() == False:
        print("No null values found")

    else:
        raise Exception("There are null values in data")

if __name__ == '__main__':

    imdb_file_name = 'office.csv'
    dialogue_file_name = 'dialogues.csv'

    df = pd.read_csv(DATA_PATH + imdb_file_name)

    dq_on_imdb(df)

    df = pd.read_csv(DATA_PATH + dialogue_file_name)

    dq_on_dialogues(df)