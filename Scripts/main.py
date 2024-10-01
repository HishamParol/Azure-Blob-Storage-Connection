import pandas as pd
from azure.storage.blob import BlobServiceClient
import os
import json

# Load configuration from JSON file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

connection_string = config['connection_string']
container_name = config['container_name']
blob_name = config['blob_name']
output_excel_file = config['output_excel_file']

def read_csv_from_blob():
    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a BlobClient
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Download the CSV file content to a Pandas DataFrame
    with open("temp_file.csv", "wb") as temp_file:
        data = blob_client.download_blob()
        temp_file.write(data.readall())

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv("temp_file.csv")

    # Clean up the temporary CSV file
    os.remove("temp_file.csv")

    return df

def save_df_to_excel(df):
    # Save the DataFrame to an Excel file
    df.to_excel(output_excel_file, index=False, engine='openpyxl')

def main():
    # Read the CSV file from Azure Blob Storage
    df = read_csv_from_blob()
    
    # Save the DataFrame to an Excel file
    save_df_to_excel(df)

    print(f"Data has been successfully saved to {output_excel_file}")

if __name__ == "__main__":
    main()
