import pandas as pd


def ingest_from_xlsx(file_path):
    result = pd.read_excel(file_path).to_dict(orient="records")
    return result
