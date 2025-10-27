import json, csv
import pandas as pd
from datetime import datetime

def read_data_from_csv(filepath):
    df = pd.read_csv(filepath)
    df = df.fillna('')
    return df.to_dict(orient='records')


def read_data_from_json(filepath):
    with open(filepath, "r") as jsonFile:
        return json.loads(jsonFile.read())


def prepare_success_error_files(json_data, success_keys, error_keys):
    now = datetime.now()
    formatted_datestr = now.strftime('%Y-%m-%d %H.%M.%S')

    success_data = list(filter(lambda data: 'success' in data, json_data))
    with open('success' + formatted_datestr + '.csv', 'w', newline='') as success_file:
        writer = csv.DictWriter(success_file, fieldnames=success_keys)
        writer.writeheader()
        writer.writerows(success_data)

    error_data = list(filter(lambda data: 'errors' in data, json_data))
    with open('error' + formatted_datestr + '.csv', 'w') as error_file:
        writer = csv.DictWriter(error_file, fieldnames=error_keys)
        writer.writeheader()
        writer.writerows(error_data)

    return success_file, error_file


def prepare_success_error_keys(json_data):
    data_keys = list(json_data[0].keys())
    success_keys = data_keys + ['Id', 'success']
    error_keys = data_keys + ['errors']

    return success_keys, error_keys


if __name__ == '__main__':
    print('Helper file ran')