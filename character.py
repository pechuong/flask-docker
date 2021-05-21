import pytest
import requests

CHARACTER_API = 'https://rickandmortyapi.com/api/character/?name='

def get_character(character):
    params = {'format': 'json'}
    response = requests.get(CHARACTER_API + character, params=params)
    return response.json()['results']

"""
    name:    get_alive
    input:   character (in json form from @get_character)
    output:  boolean - whether character is alive or not
"""
def is_alive(character):
    return character.json()['status'].equals("Alive")

"""
    name:    episodes_alive
    input:   character (in json form from @get_character)
    output:  int - number of episodes that the character was alive for
"""
def episodes_alive(character):
    split_text = "https://rickandmortyapi.com/api/episode/"

