import logging
import os
import requests
from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Set up authentication
    credential = DefaultAzureCredential()
    client = GraphClient(credential=credential)

    # Fetch data from Excel in SharePoint
    excel_url = os.environ["EXCEL_URL"]
    response = client.get(excel_url)

    if response.status_code == 200:
        excel_data = response.json()  # Process the data as needed
        return func.HttpResponse(f"Fetched data: {excel_data}", status_code=200)
    else:
        return func.HttpResponse(f"Failed to fetch data: {response.status_code}", status_code=500)
