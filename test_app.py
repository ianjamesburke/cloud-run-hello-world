from flask.testing import FlaskClient
from app import app, auth
import pytest


# Define a pytest xl named 'client' to initialize an authorized test client
@pytest.fixture(name='client')
def initialize_authorized_test_client(monkeypatch: pytest.MonkeyPatch):
    # Set the app to testing mode
    app.testing = True
    # Create a test client for the app
    client = app.test_client()
    # Monkeypatch the 'authenticate' method of 'auth' to always return True
    monkeypatch.setattr(auth, 'authenticate', lambda x, y: True)
    # Yield the test client to be used in tests
    yield client
    # Reset the app to non-testing mode
    app.testing = False



def test_hello_world_route(client: FlaskClient):
    response = client.get('/')
    assert response.status_code == 200
