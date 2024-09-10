import requests
from poke_exceptions import *
from poke_fundamentals import *

# minimum and maximum sizes for teams
MAX_SIZE = 6
MIN_SIZE = 0

# prompts user to select the size of their pokémon team
def pick_size():
    try:
        size = int(input("How many Pokémon are you planning to have? (NOTE: Min of 0 / Max of 6): "))
        if (size > MAX_SIZE) or (size <= MIN_SIZE ):
            raise NumberOutOfRangeError("Error: The number must be from 1 to 6.")
        else:
            return size
    except NumberOutOfRangeError as err1:
        print(err1)
    except ValueError:
        print("ERROR: The value must be a whole number from 1 to 6.")

# prompts user to choose members for their pokémon team, saving each selection
def choose_team(team_size):
    members = []
    for i in range(team_size):
        try:
            choice = input(f"Enter Pokémon #{i + 1} to add to your team: ").lower()
            member_url = f"{base_url}/pokemon/{choice}"
            response = requests.get(member_url)
            if response.status_code == 200:
                members.append(choice)
                if len(members) == team_size:
                    return members
            else:
                raise PokemonDoesNotExistError("Error: The Pokémon does not exist.")
        except PokemonDoesNotExistError as err2:
            print(err2)
            break
