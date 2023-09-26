import pytest
from src.app import app

def test_index_route():
    response = app.test_client().get('/test')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == '<p>OK</p>'