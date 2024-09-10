import pokebase as pb


# list of all typings
TYPES = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]


def type_matchups(offe, defe): # provides effectiveness of each typing matchup
    # list of all pokemon typings
    o_type = pb.type_(offe)
    if defe in [typ.name for typ in o_type.damage_relations.no_damage_to]:
        return 0.0
    elif defe in [typ.name for typ in o_type.damage_relations.half_damage_to]:
        return 0.5
    elif defe in [typ.name for typ in o_type.damage_relations.double_damage_to]:
        return 2.0
    else:
        return 1.0
    

def poke_offensive_matchups(typings):
    # empty dictionary for type : pokemon's effectiveness against it
    effective1 = {}

    if len(typings) == 2: # if pokemon is double-typed
        effective2 = {}
        for i in range(2):
            for other_type in TYPES:
                if i == 0:
                    typ = pb.type_(typings[i])
                    if other_type in [t.name for t in typ.damage_relations.no_damage_to]:
                        effective1[other_type] = 0.0
                    elif other_type in [t.name for t in typ.damage_relations.half_damage_to]:
                        effective1[other_type] = 0.5
                    elif other_type in [t.name for t in typ.damage_relations.double_damage_to]:
                        effective1[other_type] = 2.0
                    else:
                        effective1[other_type] = 1.0
                else:
                    typ = pb.type_(typings[i])
                    if other_type in [t.name for t in typ.damage_relations.no_damage_to]:
                        effective2[other_type] = 0.0
                    elif other_type in [t.name for t in typ.damage_relations.half_damage_to]:
                        effective2[other_type] = 0.5
                    elif other_type in [t.name for t in typ.damage_relations.double_damage_to]:
                        effective2[other_type] = 2.0
                    else:
                        effective2[other_type] = 1.0
        print(f"'{typings[0].capitalize()}' Type Offensive Matchups: {effective1}")
        print(f"'{typings[1].capitalize()}' Type Offensive Matchups: {effective2}")
    else:   # if pokemon is single-typed
        for other_type in TYPES:
                typ = pb.type_(typings[0])
                if other_type in [t.name for t in typ.damage_relations.no_damage_to]:
                    effective1[other_type] = 0.0
                elif other_type in [t.name for t in typ.damage_relations.half_damage_to]:
                    effective1[other_type] = 0.5
                elif other_type in [t.name for t in typ.damage_relations.double_damage_to]:
                    effective1[other_type] = 2.0
                else:
                    effective1[other_type] = 1.0
        print(f"'{typings[0].capitalize()}' Type Offensive Matchups: {effective1}")


def poke_defensive_matchups(typings):
    # empty dictionary for type : how weak pokemon is against it
    weakness1 = {}

    if len(typings) == 2: # if pokemon is double-typed
        weakness2 = {}
        for i in range(2):
            for other_type in TYPES:
                if i == 0:
                    typ = pb.type_(typings[i])
                    if other_type in [t.name for t in typ.damage_relations.no_damage_from]:
                        weakness1[other_type] = 0.0
                    elif other_type in [t.name for t in typ.damage_relations.half_damage_from]:
                        weakness1[other_type] = 0.5
                    elif other_type in [t.name for t in typ.damage_relations.double_damage_from]:
                        weakness1[other_type] = 2.0
                    else:
                        weakness1[other_type] = 1.0
                else:
                    typ = pb.type_(typings[i])
                    if other_type in [t.name for t in typ.damage_relations.no_damage_from]:
                        weakness2[other_type] = 0.0
                    elif other_type in [t.name for t in typ.damage_relations.half_damage_from]:
                        weakness2[other_type] = 0.5
                    elif other_type in [t.name for t in typ.damage_relations.double_damage_from]:
                        weakness2[other_type] = 2.0
                    else:
                        weakness2[other_type] = 1.0
        print(f"'{typings[0].capitalize()}' Type Defensive Matchups: {weakness1}")
        print(f"'{typings[1].capitalize()}' Type Defensive Matchups: {weakness2}")
    else:   # if pokemon if single-typed
        for other_type in TYPES:
            typ = pb.type_(typings[0])
            if other_type in [t.name for t in typ.damage_relations.no_damage_from]:
                    weakness1[other_type] = 0.0
            elif other_type in [t.name for t in typ.damage_relations.half_damage_from]:
                    weakness1[other_type] = 0.5
            elif other_type in [t.name for t in typ.damage_relations.double_damage_from]:
                    weakness1[other_type] = 2.0
            else:
                    weakness1[other_type] = 1.0
        print(f"'{typings[0].capitalize()}' Type Offensive Matchups: {weakness1}")


# get types pokémon is effective against
def get_effectiveness(typings):
    eff_against1 = []
    if len(typings) == 2:
        eff_against2 = []
        for i in range(2):
            for against in TYPES:
                if i == 0:
                    typ = pb.type_(typings[i])
                    if against in [t.name for t in typ.damage_relations.double_damage_to]:
                        eff_against1.append(against)
                    eff_list1 = ", ".join(str(eff_type.capitalize()) for eff_type in eff_against1)
                if i == 1:
                    typ = pb.type_(typings[i])
                    if against in [t.name for t in typ.damage_relations.double_damage_to]:
                        eff_against2.append(against)
                    eff_list2 = ", ".join(str(eff_type.capitalize()) for eff_type in eff_against2)
        print(f"This Pokémon's {typings[0].capitalize()} typing is effective against: " + eff_list1 + " types.")    
        print(f"Its {typings[1].capitalize()} typing is effective against: " + eff_list2 + " types.")
    else:
        for against in TYPES:
            typ = pb.type_(typings[0])
            if against in [t.name for t in typ.damage_relations.double_damage_to]:
                eff_against1.append(against)
        eff_list = ", ".join(str(eff_type.capitalize()) for eff_type in eff_against1)
        print("This Pokémon is effective against: " + eff_list + " types.")


# get types pokémon is weak against
def get_weakness(typings):
    weak_against = []
    if len(typings) == 2:
        pass
    else:
        for against in TYPES:
            typ = pb.type_(typings[0])
            if against in [t.name for t in typ.damage_relations.double_damage_from]:
                weak_against.append(against)
        weak_list = ", ".join(str(weak_type.capitalize()) for weak_type in weak_against)
        print("This Pokémon is weak against: " + weak_list + " types.")