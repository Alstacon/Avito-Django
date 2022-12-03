import pytest

from ads.serializers import AdSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client, token):
    ads = AdFactory.create_batch(2)

    expected_response = {
        "count": 2,
        "next": None,
        "previous": None,
        "results": AdSerializer(ads, many=True).data
    }

    response = client.get('/ad/', HHTP_AUTHORIZATION="Bearer " + token)

    assert response.status_code == 200
    assert response.data == expected_response

