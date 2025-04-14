import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'b30f832be01ebe7393060143126ac95d'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 2
}

response = requests.post(url = f'{URL}/v2/pokemons', headers= HEADER,json=body_create_pokemon)
print(response.text)


body_switch ={
    "pokemon_id": "289168",
    "name": "New Name",
    "photo_id": 2
}
response_switch = requests.put(url=f'{URL}/v2/pokemons', headers= HEADER,json=body_switch)
print(response_switch.text)


body_catch ={
    "pokemon_id": "289168"
}
response_catch = requests.post(url=f'{URL}/v2/trainers/add_pokeball', headers= HEADER,json=body_catch)
print(response_catch.text)