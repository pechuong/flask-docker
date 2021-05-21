import time

from flask import Flask
import requests
import pytest

app = Flask(__name__)


@app.route('/')
def hello():
  return 'Hi! I\'m Mr. Meeseeks! Look at me!!\n Existence is pain!'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
