import os
from dotenv import load_dotenv
from simple_salesforce import Salesforce
from simple_salesforce.exceptions import SalesforceMalformedRequest

import Helper as hp


def prepare_result_files(result, json_data):
    print(result)
    print(json_data)


def navigate_to_location(files_location, sf_instance):
    if not os.path.exists(files_location):
        print("Path specified is not found")
    else :
        os.chdir(files_location)
        directories = os.listdir()
        json_data = []
        operation_details = []
        data_file_exists = False

        for directory in directories:
            if os.path.isdir(directory):
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

        if not data_file_exists or not operation_details:
            return
        object_api_name = operation_details.get("objectApiName")
        operation_name = operation_details.get("operationName")

        result = []
        if json_data is []:
            print(f"No Data to insert for {object_api_name}")
            return
        try:
            result = sf_instance.bulk.submit_dml(object_api_name,
                                                 operation_name,
                                                 json_data,
                                                 batch_size="auto",
                                                 use_serial=True)
            prepare_result_files(result, json_data)
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