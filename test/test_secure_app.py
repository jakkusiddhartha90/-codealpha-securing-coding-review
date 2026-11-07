import pytest
from app.secure_app import app

@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client

def test_home_renders_normal_name(client):
    response = client.get("/?name=Student")
    assert response.status_code == 200
    assert b"Hello Student" in response.data

def test_home_escapes_html_input(client):
    response = client.get("/?name=%3Cscript%3Ealert(1)%3C/script%3E")
    assert response.status_code == 200
    assert b"<script>" not in response.data
    assert b"&lt;script&gt;" in response.data

def test_lookup_valid_id(client):
    response = client.get("/lookup?id=1")
    assert response.status_code == 200
    assert response.get_json() == {"result": "demo item"}

@pytest.mark.parametrize("bad_id", ["abc", "-1", "1 OR 1=1"])
def test_lookup_rejects_invalid_id(client, bad_id):
    response = client.get(f"/lookup?id={bad_id}")
    assert response.status_code == 400
