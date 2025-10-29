# Dataload-Automation
A python script written to automate dataload in salesforce
___
## Preparation for running the script

### Installing dependencies
> pip install -r requirements.txt


Once the above requirements are installed please run the main.py file.

---
### Points to consider while running the script.
- Create a `.env` file in your project root and define the following environment variables with your Salesforce org credentials:
  - SF_USERNAME=your_salesforce_username 
  - SF_PASSWORD=your_salesforce_password 
  - SF_SECURITY_TOKEN=your_salesforce_security_token
- Make sure your files have more than one record. 
- Script uses bulk api which skips creation of single record.
- Currently script supports dml operation and no query operation is supported.

### Points to consider while creating files.
- Make sure the column names in csv matches with the object field names.
- To use external id use format LookupFieldApiName.ExternalIdFieldApiName

### Things to implement
- Support for combination of fields for objects where external ids are not present
- A desktop application for creating json files, running the data load.