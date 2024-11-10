from ingest_from_api import ingest_from_api
from ingest_from_csv import ingest_from_csv
from ingest_from_xlsx import ingest_from_xlsx
import requests


def ingest_new_data(data_source):
    if data_source.startswith(("http", "https")):
        try:
            response = requests.get(data_source)
            if response.headers["Content-Type"] == "application/json":
                return ingest_from_api(data_source)
            else:
                return f"API returned error with status code: {response.status_code}"
        except requests.RequestException as e:
            return f"API Error: {e}"
    if data_source.endswith(".csv"):
        return ingest_from_csv(data_source)
    elif data_source.lower().endswith((".xls", ".xlsx")):
        return ingest_from_xlsx(data_source)
    return "Invalid data source"
