def test_get_all_users(client):
    response = client.get('/api/admin/users')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_user_by_id(client):
    # Get one user from list
    res = client.get("/api/admin/users")
    users = res.get_json()

    if users:
        user_id = users[0]["_id"]
        detail_res = client.get(f"/api/admin/user/{user_id}")
        assert detail_res.status_code == 200
        assert "_id" in detail_res.get_json()

def test_delete_user_by_id(client):
    # Create a user first
    create_res = client.post("/api/auth/register", json={
        "username": "todelete",
        "email": "todelete@example.com",
        "password": "delete123",
        "role": "USER"
    })

    # Get created user
    res = client.get("/api/admin/users")
    users = res.get_json()
    user = next((u for u in users if u["username"] == "todelete"), None)

    if user:
        del_res = client.delete(f"/api/admin/user/{user['_id']}")
        assert del_res.status_code == 200
        assert "Deleted" in del_res.get_json().get("message", "")
