from fastapi.testclient import TestClient
from serve import create_app


def test_get():
    client = TestClient(create_app())
    response = client.post('/', json={'text': 'I am speaking in English'})

    assert response.status_code == 200
    res = response.json()
    print(res['is_us'])
