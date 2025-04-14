import requests
import pytest


URL = 'https://api.pokemonbattle.ru'
TOKEN = 'b30f832be01ebe7393060143126ac95d'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '29259'

def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers')
    assert response.status_code == 200

def test_trainer_id():
    response_name = requests.get(url = f'{URL}/v2/trainers', params={"trainer_id": TRAINER_ID})
    assert response_name.json()["data"][0]['trainer_name'] == 'dezulure'