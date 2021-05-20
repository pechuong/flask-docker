import pytest
import requests

from pytest_bdd import scenarios, when, then

CHARACTER_API = 'https://rickandmortyapi.com/api/character/?name='

scenarios('../features/ram_alive.feature', example_converters=dict(character=str, status=str))


@pytest.fixture
@when('the RAM API is queried with "<character>"')
def character_response(character):
    params = {'format': 'json'}
    response = requests.get(CHARACTER_API + character, params=params)
    return response


@then('the response status code is 200')
def character_response_code(character_response):
    assert character_response.status_code == 200


@then('the response shows status of "<status>"')
def character_alive(character_response, status):
    assert character_response.json()['status'] == status
