from flask.testing import FlaskClient
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client: FlaskClient):
    rv = client.get('/')
    assert b'Hello, World!' in rv.data