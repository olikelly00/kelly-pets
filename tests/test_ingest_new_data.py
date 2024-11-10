from lib.ingest_new_data import ingest_new_data
import os

def test_ingest_new_data_with_csv_input_returns_correct_data():
    csv_file_path = os.path.join(os.path.dirname(__file__), '../mock_data/pet_details.csv')
    result = ingest_new_data(csv_file_path)
    assert result[0] == {'pet_id': '1', 'name': 'Buddy', 'species': 'Dog', 'breed': 'Golden Retriever', 'age': '5'}
    assert result[19] == {'pet_id': '20', 'name': 'Nala', 'species': 'Cat', 'breed': 'British Shorthair', 'age': '4'}


def test_ingest_new_data_with_csv_input_returns_all_data():
    csv_file_path = os.path.join(os.path.dirname(__file__), '../mock_data/pet_details.csv')
    result = ingest_new_data(csv_file_path)
    assert len(result) == 20

def test_ingest_new_data_with_xlsx_input_returns_correct_data():
    xlsx_file_path = os.path.join(os.path.dirname(__file__), '../mock_data/policy_data.xlsx')
    result = ingest_new_data(xlsx_file_path)
    assert result[0] == {
        "policy_id": 1001,
        "customer_name": "John Doe",
        "pet_name": "Buddy",
        "species": "Dog",
        "policy_start_date": "2023-01-15",
        "policy_end_date": "2024-01-15",
        "premium_amount": 300
    }
    assert result[-1] ==   {
        "policy_id": 1005,
        "customer_name": "Charlie Black",
        "pet_name": "Max",
        "species": "Dog",
        "policy_start_date": "2022-11-11",
        "policy_end_date": "2023-11-11",
        "premium_amount": 375
    }


def test_ingest_new_data_with_xlsx_input_returns_all_data():
    xlsx_file_path = os.path.join(os.path.dirname(__file__), '../mock_data/policy_data.xlsx')
    result = ingest_new_data(xlsx_file_path)
    assert len(result) == 5


def test_ingest_new_data_with_api_input_returns_correct_data():
    api_url = 'http://127.0.0.1:5000/claims/3'
    result = ingest_new_data(api_url)
    assert result ==  [{
    "claim_amount": 75,
    "claim_date": "2023-08-01",
    "claim_id": 503,
    "claim_type": "Vaccination",
    "pet_id": 3,
    "pet_name": "Charlie",
    "policy_id": 1003,
    "species": "Dog",
    "status": "Approved"
  }]


def test_ingest_new_data_with_incorrect_api_input_returns_expected_error_message():
    api_url = 'http://127.0.0.1:5000/clames/3'
    result = ingest_new_data(api_url)
    assert result == "API returned error with status code: 404"



def test_load_new_data():
    pass
