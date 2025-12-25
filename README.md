# 📦 Salesforce DataLoad Automation

Automate **ordered, repeatable Salesforce data loads** during deployments using Python and the Bulk API.

---

## ❓ What problem does this solve?

Salesforce deployments often require loading **large volumes of related data** after metadata deployment.  
This process is usually:

- Manual and time-consuming
- Error-prone due to incorrect load order
- Dependent on individual knowledge
- Hard to reproduce across environments

This tool removes manual effort by **automating data loads from folders**, making deployments more deterministic and reliable.

---

## 👥 Who is this for?

- Salesforce Developers  
- Technical Consultants  
- Release Managers  
- Teams handling post-deployment data loads  

---

## ⚙️ What does this tool do?

This script:

- Scans folders for CSV files  
- Loads data into Salesforce using the **Bulk API**  
- Supports DML operations (insert / update / upsert)  
- Handles lookup relationships using **external IDs**  
- Logs successes and failures for troubleshooting  

The focus is **repeatability and reliability**, not UI-based uploads.

---

## 🧩 Typical use case

After deploying metadata:

1. Place all required CSV files into a folder  
2. Ensure the correct load order  
3. Run the script once  
4. Review logs for failures or retries  

This reduces:
- Manual intervention  
- Release-time stress  
- Deployment errors  

---

## ✅ Prerequisites

- Python 3.x  
- Salesforce org credentials  
- Salesforce Bulk API enabled  

---

## 📥 Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

## Create a .env file in the project root and define the following variables:
```bash
SF_USERNAME=your_salesforce_username
SF_PASSWORD=your_salesforce_password
SF_SECURITY_TOKEN=your_salesforce_security_token
```

▶️ Running the script

Execute the main script:
```bash
python main.py
```


📁 File preparation guidelines
- CSV column names must match Salesforce field API names
- To reference lookups using external IDs, use the format:
```bash
LookupFieldApiName.ExternalIdFieldApiName
```
- Each CSV file must contain more than one record
- Single-record operations are not supported due to Bulk API constraints

⚠️ Current limitations

- Supports DML operations only (no query support)
- Uses Salesforce Bulk API (not suitable for single record loads)
- Load order must be defined manually
- No automatic dependency resolution yet

🚧 Planned enhancements

- Support for composite external keys
- Config-based load ordering
- Improved retry and failure recovery
- CI/CD pipeline integration

🎯 Why this tool exists

This tool is not a replacement for Salesforce Data Loader UI.
It exists to:

- Reduce deployment-time friction
- Eliminate repetitive manual steps
- Enable predictable and repeatable data loads

📌 Disclaimer

Use this tool in non-production environments first.
Always validate data and permissions before running in production.


---

## Why this README works (important insight)

- It **leads with the problem**, not the script
- It defines **who should use it**
- It explains **when NOT to use it**
- It builds trust by listing limitations
- It positions the tool as a **deployment utility**, not a hack

This is now a **real asset**, not a personal script.

---

### Next step (don’t skip this):
Do you want me to help you:
- **Write the Medium article** that complements this repo  
- **Design a config-based load order** (`yaml/json`)  
- **Turn this into a CLI tool**  

Pick **one** and we continue.
