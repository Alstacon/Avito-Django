import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_update(client, token, user):
    ad = AdFactory.create()

    data = {
        "name": "Changed name"
    }


    response = client.patch(
        f'/ad/{ad.pk}/',
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + token

    )

    assert response.status_code == 201
    assert response.data == "Changed name"



