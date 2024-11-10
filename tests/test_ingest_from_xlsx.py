from lib.ingest_from_xlsx import ingest_from_xlsx
import os

def test_ingest_from_xlsx():
    xlsx_file_path = os.path.join(os.path.dirname(__file__), '../mock_data/policy_data.xlsx')
    result = ingest_from_xlsx(xlsx_file_path)
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

def test_ingest_from_xlsx_all_data_is_ingested():
    xlsx_file_path = os.path.join(os.path.dirname(__file__), '../mock_data/policy_data.xlsx')
    result = ingest_from_xlsx(xlsx_file_path)
    assert len(result) == 5
