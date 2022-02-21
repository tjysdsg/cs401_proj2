from fastapi.testclient import TestClient
from serve import create_app


def test_get():
    client = TestClient(create_app())
    response = client.post('/api/american', json={
        'text': 'As we move forward together during the #COVID19 crisis,'
                'we are saying #thankyou to all our medical volunteers'
    })

    assert response.status_code == 200
    res = response.json()
    print(res['is_american'])
