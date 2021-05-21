import time

from flask import Flask
import requests
import pytest
#import character

app = Flask(__name__)


@app.route('/')
def hello():
#   test_json = character.get_character("Morty Smith")
#   alive = character.is_alive(test_json)
#   test_str = "Morty Smith is "
#   if (alive):
#     test_str += "Alive"
#   else:
#     test_str += "Dead"
#   return test_str
    return 'Hi! I\'m Mr. Meeseeks! Look at me!!\n Existence is pain!'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
