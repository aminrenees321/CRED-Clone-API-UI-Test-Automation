import requests

def test_login_success():
    payload = {"email": "user@example.com", "password": "password123"}
    response = requests.post("http://localhost:5000/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()