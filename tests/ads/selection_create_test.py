
import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, token):
    AdFactory.create_batch(3)

    expected_response = {
        "id": 1,
        "owner": 1,
        "name": "Test selection",
        "items": [ad.pk for ad in ads]
    }

    data = {
        "name": "Test selection",
        "items": [1, 2, 3]
    }

    response = client.post(
        '/selection/create/',
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 201
    assert response.data == expected_response
