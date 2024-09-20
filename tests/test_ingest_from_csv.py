from lib.ingest_from_csv import *
import os

def test_ingest_from_csv():
    csv_file_path = os.path.join(os.path.dirname(__file__), '../mock_data/pet_details.csv')
    print(csv_file_path)
    result = ingest_from_csv(csv_file_path)
    assert result[0] == {'pet_id': '1', 'name': 'Buddy', 'species': 'Dog', 'breed': 'Golden Retriever', 'age': '5'}
    assert result[19] == {'pet_id': '20', 'name': 'Nala', 'species': 'Cat', 'breed': 'British Shorthair', 'age': '4'}
    

def test_all_csv_data_is_ingested():
    csv_file_path = os.path.join(os.path.dirname(__file__), '../mock_data/pet_details.csv')
    result = ingest_from_csv(csv_file_path)
    assert len(result) == 20



