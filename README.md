# **Azure Blob to Excel Converter**

This Python script connects to **Azure Blob Storage**, reads a CSV file from a blob, converts it into a **Pandas DataFrame**, and saves it as an **Excel file**. The script is straightforward to use and can be run directly.

## **Steps to Use**

### **Step 1: Update the Configuration File**
Before running the script, make sure to update the script with your **Azure Blob Storage** details. Replace the placeholders with your actual connection information:
- **Connection String**: The connection string for Azure Blob Storage.
- **Container Name**: The name of the container where your blob is stored.
- **Blob Name**: The name of the blob (CSV file) you wish to read.
- **Output Excel File Name**: The desired name for the output Excel file.

### **Step 2: Install Required Packages**
- The script requires Python packages, which are listed in the `requirements.txt` file.
- To install them, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

### **Step 3: Run the Script**
- Once the configuration is set and the required packages are installed, you can run the script. 
- To execute the script, use the following command in your terminal or command prompt:
```bash
python read_blob_to_excel.py
```

## **Project Structure**
```bash
azure-blob-Storage-Connection/
│
├── read_blob_to_excel.py    # Main script to read CSV from blob and save as Excel
├── requirements.txt         # List of required packages
└── README.md                # Documentation for the project
```
