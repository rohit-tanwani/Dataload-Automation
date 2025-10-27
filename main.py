import os
from dotenv import load_dotenv
from simple_salesforce import Salesforce
from simple_salesforce.exceptions import SalesforceMalformedRequest

import helper as hp


def prepare_result_files(result_data, json_data):
    if not result_data:
        return

    success_keys, error_keys = hp.prepare_success_error_keys(json_data)

    for index, data in enumerate(json_data):
        result = result_data[index]
        if 'id' in result:
            data['Id'] = result['id']

        if result['success']:
            data['success'] = result['success']

        if result['errors']:
            data['errors'] = result['errors']

    hp.prepare_success_error_files(json_data, success_keys, error_keys)


def navigate_to_location(files_location, sf_instance):
    if not os.path.exists(files_location):
        print("Path specified is not found")
    else :
        os.chdir(files_location)

        json_data = []
        operation_details = []
        data_file_exists = False

        directories = os.listdir()
        for directory in directories:
            if directory == '__result__':
                continue
            elif os.path.isdir(directory):
                navigate_to_location(files_location + os.sep + directory, sf_instance)
                os.chdir(files_location)
                continue
            else:
                filepath = directory
                filename, extension = os.path.splitext(filepath)
                if extension == ".csv":
                    json_data = hp.read_data_from_csv(filepath)
                    data_file_exists = True
                elif extension == ".json":
                    operation_details = hp.read_data_from_json(filepath)

        if not data_file_exists or not operation_details or not json_data:
            return

        object_api_name = operation_details.get("objectApiName")
        operation_name = operation_details.get("operationName")


        try:
            print('json_data==>', json_data)
            #below method skips the execution for single record.
            result = sf_instance.bulk.submit_dml(object_name=object_api_name, dml=operation_name,
                                                 data=json_data, include_detailed_results=True,
                                                 batch_size="auto")
            print('result==>', result)
            if not os.path.exists('__results__'):
                os.mkdir('__results__')
            os.chdir('__results__')

            prepare_result_files(result, json_data)

            os.chdir(files_location)
        except (SalesforceMalformedRequest, ValueError) as e:
            print(e)


if __name__ == '__main__':
    load_dotenv()
    username = os.getenv("SF_USERNAME")
    password = os.getenv("SF_PASSWORD")
    security_token = os.getenv("SF_SECURITY_TOKEN")

    sf = Salesforce(username=username, password=password, security_token=security_token)

    location = input('Enter location of files: ')
    navigate_to_location(location, sf)