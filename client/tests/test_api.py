import pytest
import requests

URL_BASE = 'http://127.0.0.1:8000/api/v1/'

def test_customer():
    url = f"{URL_BASE}customers/" 
        
    response = requests.get(url)

    # Verify status code
    assert response.status_code == 200 

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json"

    # Verify response structure
    data = response.json()  
    assert isinstance(data[0], dict)
    
    assert "customer_id" in data[0]
    assert "firstname" in data[0]
    assert "lastname" in data[0]
    assert "updated" in data[0]
    assert "created" in data[0]
    assert "customertype" in data[0]
    assert "user" in data[0]
    assert "status" in data[0]