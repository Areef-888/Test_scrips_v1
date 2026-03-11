def test_multiply_number(client):
    response = client.post("/multiply_number", json={"number": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 10}