from names_types import *
from matchups import *
from create_team import *

def main():
    # user selects team size and picks out pokémon
    team_size = pick_size()
    team = choose_team(team_size)

    # prints out user's team
    if team is not None:
        team_list = ", ".join(str(mon.capitalize()) for mon in team)
        print("Your Pokémon team: " + team_list)

        # prints out user's team information if they opt to sea offensive/defensive matchups
        want_info = input("Would you like to see your team's info and type matchups? (Y for yes): ")
        if want_info == "Y":
            for mon in team: 
                print("")
                mon_info = get_pokemon_info(mon)
                mon_types = get_typings(mon_info)
                print_nametypes(mon_info)
                get_weakness(mon_types)
                get_effectiveness(mon_types)
        
main()
