import csv
import os

def ingest_from_csv(csv_file_path):
    data = []
    with open (csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


csv_file_path = os.path.join(os.path.dirname(__file__), '../mock_data/missing_pet_details.csv')

print(ingest_from_csv(csv_file_path))
