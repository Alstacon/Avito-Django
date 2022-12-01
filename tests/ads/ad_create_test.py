import pytest


@pytest.mark.django_db
def test_ad_create(client, token):
    expected_response = {
        "id": 1,
        "name": "Testnamead",
        "author": 1,
        "price": 1500,
        "description": "Test desc",
        "is_published": False,
        "image": None,
        "category": 1
    }

    data = {
        "name": "Testnamead",
        "price": 1500,
        "description": "Test desc",
        "is_published": False,
        "category": 1
    }

    response = client.post(
        '/ad/',
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 201
    assert response.data == expected_response
