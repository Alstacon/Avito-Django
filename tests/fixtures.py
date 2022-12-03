import pytest


@pytest.fixture
@pytest.mark.django_db
def token(client, django_user_model):
    username = 'user'
    password = '123Qwe'

    django_user_model.objects.create_user(
        username=username,
        password=password,
        role='admin'
    )

    response = client.post(
        '/user/token/',
        {"username": username, "password": password},
        format="json"
    )

    return response.data['access']


@pytest.fixture
@pytest.mark.django_db
def user(django_user_model):
    username = 'user'
    password = '123Qwe)'

    django_user_model.objects.create_user(
        username=username,
        password=password,
        role='admin'
    )
