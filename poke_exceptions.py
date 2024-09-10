# raised if user inputs the wrong name for a pokemon
class PokemonDoesNotExistError(Exception):
    pass

# raised if user inputs a number out of specified range
class NumberOutOfRangeError(Exception):
    pass