import pokebase as pb
from poke_fundamentals import *

def type_matchups(offe, defe): # provides effectiveness of each typing matchup
    # list of all pokemon typings
    o_type = pb.type_(offe)
    if defe in [typ.name for typ in o_type.damage_relations.no_damage_to]:
        print ("Immune")
    elif defe in [typ.name for typ in o_type.damage_relations.half_damage_to]:
        print("Ineffective")
    elif defe in [typ.name for typ in o_type.damage_relations.double_damage_to]:
        print("Super Effective")
    else:
        print("Effective")
    

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
                        effective1[other_type] = "Immune"
                    elif other_type in [t.name for t in typ.damage_relations.half_damage_to]:
                        effective1[other_type] = "Ineffective"
                    elif other_type in [t.name for t in typ.damage_relations.double_damage_to]:
                        effective1[other_type] = "Super Effective"
                    else:
                        effective1[other_type] = "Effective"
                else:
                    typ = pb.type_(typings[i])
                    if other_type in [t.name for t in typ.damage_relations.no_damage_to]:
                        effective2[other_type] = "Immune"
                    elif other_type in [t.name for t in typ.damage_relations.half_damage_to]:
                        effective2[other_type] = "Ineffective"
                    elif other_type in [t.name for t in typ.damage_relations.double_damage_to]:
                        effective2[other_type] = "Super effective"
                    else:
                        effective2[other_type] = "Ineffective"
        print(f"'{typings[0].capitalize()}' Type Offensive Matchups: {effective1}")
        print(f"'{typings[1].capitalize()}' Type Offensive Matchups: {effective2}")
    else:   # if pokemon is single-typed
        for other_type in TYPES:
                typ = pb.type_(typings[0])
                if other_type in [t.name for t in typ.damage_relations.no_damage_to]:
                    effective1[other_type] = "Immune"
                elif other_type in [t.name for t in typ.damage_relations.half_damage_to]:
                    effective1[other_type] = "Ineffective"
                elif other_type in [t.name for t in typ.damage_relations.double_damage_to]:
                    effective1[other_type] = "Super effective"
                else:
                    effective1[other_type] = "Effective"
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
                        weakness1[other_type] = "Immune"
                    elif other_type in [t.name for t in typ.damage_relations.half_damage_from]:
                        weakness1[other_type] = "Ineffective"
                    elif other_type in [t.name for t in typ.damage_relations.double_damage_from]:
                        weakness1[other_type] = "Super Effective"
                    else:
                        weakness1[other_type] = "Effective"
                else:
                    typ = pb.type_(typings[i])
                    if other_type in [t.name for t in typ.damage_relations.no_damage_from]:
                        weakness2[other_type] = "Immune"
                    elif other_type in [t.name for t in typ.damage_relations.half_damage_from]:
                        weakness2[other_type] = "Ineffective"
                    elif other_type in [t.name for t in typ.damage_relations.double_damage_from]:
                        weakness2[other_type] = "Super effective"
                    else:
                        weakness2[other_type] = "Effective"
        print(f"'{typings[0].capitalize()}' Type Defensive Matchups: {weakness1}")
        print(f"'{typings[1].capitalize()}' Type Defensive Matchups: {weakness2}")
    else:   # if pokemon if single-typed
        for other_type in TYPES:
            typ = pb.type_(typings[0])
            if other_type in [t.name for t in typ.damage_relations.no_damage_from]:
                    weakness1[other_type] = "Immune"
            elif other_type in [t.name for t in typ.damage_relations.half_damage_from]:
                    weakness1[other_type] = "Ineffective"
            elif other_type in [t.name for t in typ.damage_relations.double_damage_from]:
                    weakness1[other_type] = "Super Effective"
            else:
                    weakness1[other_type] = "Effective"
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
                else:
                    typ = pb.type_(typings[i])
                    if against in [t.name for t in typ.damage_relations.double_damage_to]:
                        eff_against2.append(against)
                    eff_list2 = ", ".join(str(eff_type.capitalize()) for eff_type in eff_against2)
        print(f"Its {typings[0].capitalize()} typing is super effective against: " + eff_list1 + " types.")    
        print(f"Its {typings[1].capitalize()} typing is super effective against: " + eff_list2 + " types.")
    else:
        for against in TYPES:
            typ = pb.type_(typings[0])
            if against in [t.name for t in typ.damage_relations.double_damage_to]:
                eff_against1.append(against)
        eff_list = ", ".join(str(eff_type.capitalize()) for eff_type in eff_against1)
        print("This Pokémon is super effective against: " + eff_list + " types.")


# get types pokémon is weak against
def get_weakness(typings):
    weak_against1 = []
    if len(typings) == 2:
        weak_against2, half_against1, half_against2, imm_against1, imm_against2, fin_weakness= ([] for i in range(6))
        for i in range(2):
            for against in TYPES:
                if i == 0:
                    typ = pb.type_(typings[i])
                    if against in [t.name for t in typ.damage_relations.double_damage_from]:
                        weak_against1.append(against) # weaknesses of first typing
                    elif against in [t.name for t in typ.damage_relations.half_damage_from]:
                        half_against1.append(against) # types that do 0.5x damage to first typing
                    elif against in [t.name for t in typ.damage_relations.no_damage_from]:
                        imm_against1.append(against) # types first typing is immune to
                else:
                    typ = pb.type_(typings[i])
                    if against in [t.name for t in typ.damage_relations.double_damage_from]:
                        weak_against2.append(against) # weaknesses of second typing
                    elif against in [t.name for t in typ.damage_relations.half_damage_from]:
                        half_against2.append(against) # types that do 0.5x damage to second typing
                    elif against in [t.name for t in typ.damage_relations.no_damage_from]:
                        imm_against2.append(against) # types second typing is immune to
        for weak1 in weak_against1:
            if weak1 in weak_against2:
                fin_weakness.append(weak1)
            elif (weak1 not in half_against2) and (weak1 not in imm_against2):
                fin_weakness.append(weak1)
        for weak2 in weak_against2:
            if (weak2 not in half_against1) and (weak2 not in imm_against1):
                fin_weakness.append(weak2)
        weak_list = ", ".join(str(weak_type.capitalize()) for weak_type in fin_weakness)
        print("This Pokémon is weak against: " + weak_list + " types.")
    else:
        for against in TYPES:
            typ = pb.type_(typings[0])
            if against in [t.name for t in typ.damage_relations.double_damage_from]:
                weak_against1.append(against)
        weak_list = ", ".join(str(weak_type.capitalize()) for weak_type in weak_against1)
        print("This Pokémon is weak against: " + weak_list + " types.")
