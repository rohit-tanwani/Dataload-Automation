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
