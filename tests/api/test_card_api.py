def test_add_card_api():
    payload = {"card_number": "4111111111111111", "expiry": "12/26", "cvv": "123"}
    response = requests.post("http://localhost:5000/addCard", json=payload)
    assert response.status_code == 200