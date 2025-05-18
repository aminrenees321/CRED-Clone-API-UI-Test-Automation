def test_payment_api():
    payload = {"amount": 1000, "cvv": "123"}
    response = requests.post("http://localhost:5000/payBill", json=payload)
    assert response.status_code == 200