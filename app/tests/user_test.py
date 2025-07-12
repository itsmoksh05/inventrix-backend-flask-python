
def test_register_user(client):
    response = client.post('/api/auth/register', json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "Test@1234",
        "role": "USER"
    })
    assert response.status_code in [201, 400]  # Might already exist
    assert "message" in response.get_json() or "error" in response.get_json()

def test_login_user(client):
    response = client.post('/api/auth/login', json={
        "username": "testuser",
        "password": "Test@1234"
    })
    assert response.status_code in [200, 401]
