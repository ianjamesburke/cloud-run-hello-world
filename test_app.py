from app import app

def test_hello_world_route():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200