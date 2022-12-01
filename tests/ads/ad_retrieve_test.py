import pytest

from ads.serializers import AdDetailSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_retrieve(client, token):
    ad = AdFactory.create()

    expected_response = AdDetailSerializer(ad).data

    response = client.get(
        '/ad/1/',
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 200
    assert response.data == expected_response
