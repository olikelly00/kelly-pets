from lib.ingest_from_api import ingest_from_api


def test_ingest_all_data_from_api():
    api_url = "http://127.0.0.1:5000/claims"
    result = ingest_from_api(api_url)
    assert result[1] == {
        "claim_amount": 1800,
        "claim_date": "2023-07-10",
        "claim_id": 502,
        "claim_type": "Surgery",
        "pet_id": 2,
        "pet_name": "Mittens",
        "policy_id": 1002,
        "species": "Cat",
        "status": "Pending",
    }
    assert result[-1] == {
        "claim_amount": 120.5,
        "claim_date": "2023-06-18",
        "claim_id": 505,
        "claim_type": "Medication",
        "pet_id": 5,
        "pet_name": "Max",
        "policy_id": 1005,
        "species": "Dog",
        "status": "Denied",
    }


def test_ingest_specific_data_from_api():
    api_url = "http://127.0.0.1:5000/claims/3"
    result = ingest_from_api(api_url)
    assert result == [
        {
            "claim_amount": 75,
            "claim_date": "2023-08-01",
            "claim_id": 503,
            "claim_type": "Vaccination",
            "pet_id": 3,
            "pet_name": "Charlie",
            "policy_id": 1003,
            "species": "Dog",
            "status": "Approved",
        }
    ]
