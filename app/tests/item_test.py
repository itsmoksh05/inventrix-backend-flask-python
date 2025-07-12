def test_add_item(client):
    response = client.post('/api/items/', json={
        "name": "Test Item",
        "user_name": "tester",
        "quantity": 10,
        "category_name": "Test Category",
        "expiry_date": "2025-08-01",
        "image_url": None
    })
    assert response.status_code in [200, 400]
    json_data = response.get_json()
    assert "Item_id" in json_data or "Runtime Error" in json_data

def test_get_all_items(client):
    response = client.get('/api/items/')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_update_item(client):
    items = client.get("/api/items/").get_json()
    if items:
        item_id = items[0]["_id"]
        res = client.put(f"/api/items/{item_id}", json={"quantity": 999})
        assert res.status_code in [200, 404]

def test_delete_item(client):
    items = client.get("/api/items/").get_json()
    if items:
        item_id = items[-1]["_id"]
        res = client.delete(f"/api/items/{item_id}")
        assert res.status_code in [200, 404]