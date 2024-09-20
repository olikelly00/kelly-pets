import csv

def ingest_from_csv(csv_file_path):
    data = []
    with open (csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data