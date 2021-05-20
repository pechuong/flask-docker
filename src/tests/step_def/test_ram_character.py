import pytest
import requests

from pytest_bdd import scenarios, given, when, then

CHARACTER_API = 'https://rickandmortyapi.com/api/character/'

scenarios('../features/dnd_classes.feature', example_converters=dict(classes=str, hit=int))


@pytest.fixture
@when('the DnD API is queried with "<classes>"')
def classes_response(classes):
    params = {'format': 'json'}
    response = requests.get(CLASSES_API + classes, params=params)
    return response


@then('the response status code is 200')
def classes_response_code(classes_response):
    assert classes_response.status_code == 200


@then('the response shows hit_die of "<hit>"')
def classes_hit_die(classes_response, hit):
    assert classes_response.json()['hit_die'] == hit
