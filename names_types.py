import requests
from poke_exceptions import *
from poke_fundamentals import *


def get_pokemon_info(name): # retrieves info of selected pokemon from pokeapi
    try:
        url = f"{base_url}/pokemon/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            pokemon_data = response.json()
            return pokemon_data
        else: 
            raise PokemonDoesNotExistError("Error: The Pokémon does not exist.")
    except PokemonDoesNotExistError as err:
         print(err)


def get_typings(poke_data): # gets typings of selected pokemon
    if poke_data:
        typings = [typing["type"]["name"] for typing in poke_data["types"]]
        return typings


def print_nametypes(poke_data): # function to print out name and typing of selected pokemon
    vowels = ['A', 'E', 'I', 'O', 'U'] # for specification of 'a' or 'an'
    typs = get_typings(poke_data)
    if len(typs) == 2: # formatting if multi-typed
            typing = "{}/{}".format(typs[0].capitalize(), typs[1].capitalize())
    else:
            typing = typs[0].capitalize()

    if typing[0] in vowels: # printing info
        print(f"{poke_data['name'].capitalize()} is an {typing} Pokémon.")
    else:
        print(f"{poke_data['name'].capitalize()} is a {typing} Pokémon.")
