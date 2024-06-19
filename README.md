# Real-time Data Processing with Databricks and Azure Functions

This repository contains a sample implementation for extracting data from Google Analytics, cross-referencing it with Excel data stored on SharePoint, and storing the processed data using Databricks' medallion architecture (Bronze, Silver, Gold).

## Directory Structure

- `azure-functions/`: Contains Azure Functions code to fetch data from Excel on SharePoint.
- `databricks/`: Contains Databricks notebooks for real-time data processing.
- `README.md`: This file.

## Azure Functions Setup

1. Navigate to the `azure-functions` directory.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Deploy the Azure Function:
   ```bash
   func azure functionapp publish <FunctionAppName>
   ```

## Databricks Notebooks

1. Upload the notebooks in `databricks/notebooks/` to your Databricks workspace.
2. Run the notebooks in the following order:
   - `01_google_analytics_stream.py`
   - `02_cross_reference_with_excel.py`
   - `03_medallion_model.py`

## Environment Variables

Make sure to set the following environment variables:
- `EXCEL_URL`: URL to the Excel file in SharePoint.

## Notes

- The paths and schemas used in the sample code are hypothetical and should be adjusted according to your actual data and requirements.
- Ensure that you have the necessary permissions and credentials to access Google Analytics and SharePoint data.
