import pandas as pd
import json

def read_data_from_csv(filepath):
    df = pd.read_csv(filepath)
    df = df.fillna('')
    return df.to_dict(orient='records')

def read_data_from_json(filepath):
    with open(filepath, "r") as jsonFile:
        return json.loads(jsonFile.read())

if __name__ == '__main__':
    print('Helper file ran')