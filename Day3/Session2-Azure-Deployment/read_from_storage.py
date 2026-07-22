"""
Day 3 - Session 2  |  Read your CSV back out of Blob Storage.

This shows how a real application uses data in the cloud: it does not
need the file on the local machine at all.

HOW TO RUN (in Azure Cloud Shell)
    pip install azure-storage-blob azure-identity pandas
    python read_from_storage.py

Change the two names below first.
"""

import io
import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# ---------------------------------------------------------------
# CHANGE THESE
# ---------------------------------------------------------------
STORAGE_ACCOUNT = "stabebe2026cli"      # your storage account name
CONTAINER = "data"
BLOB_NAME = "soldiers_fitness.csv"

ACCOUNT_URL = f"https://{STORAGE_ACCOUNT}.blob.core.windows.net"


def main():
    print(f"Connecting to {ACCOUNT_URL} ...")

    # DefaultAzureCredential uses whoever is signed in to Cloud Shell.
    # No passwords or keys in the code - this is the safe way.
    credential = DefaultAzureCredential()
    service = BlobServiceClient(account_url=ACCOUNT_URL, credential=credential)

    blob = service.get_blob_client(container=CONTAINER, blob=BLOB_NAME)

    print(f"Downloading {BLOB_NAME} ...")
    raw = blob.download_blob().readall()

    # Read it straight into pandas without saving to disk
    df = pd.read_csv(io.BytesIO(raw))

    print(f"\nLoaded {len(df)} rows and {len(df.columns)} columns.\n")
    print(df.head())

    print("\n--- How many people at each fitness level? ---")
    print(df["level"].value_counts())

    print("\n--- Average 5km time by level (minutes) ---")
    print(df.groupby("level")["run_5km_min"].mean().round(1))

    print("\nThe file never touched this computer's disk.")
    print("That is the point of cloud storage.")


if __name__ == "__main__":
    main()
