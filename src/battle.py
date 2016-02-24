"""
This file contains the battle class. A battle class contains two fleets
and facilities to have them both fire, calculate potential damage, and then
state which ships are destroyed.

One day, this will be modified to have a list of fleets that then battle
in a given order according to the game rules, as opposed to simply
comparing two fleets.
"""

import copy as copy_module
import ships
import fleet as fleet_object
import damage_models

class Battle(object):
    def __init__(self, name, offense, defense):
        self.name = name
        self.defense = defense
        self.offense = offense
        #self.Ofleet_backup = copy_module.deepcopy(Ofleet)
        #self.Dfleet_backup = copy_module.deepcopy(Dfleet)

    def __str__(self):
        return "%s:\nOffense: %sDefense: %s"%(self.name,str(self.offense),str(self.defense))

    def simulate(self, num):
        '''
        Simulates battles num times
        '''
        if self.offense == None or self.defense == None:
            print("Missing fleet information")
        
        print("Simulation begins:")

        # Reverse iteration, defensive fires first
        speed = 8
        while speed >= 0:
            d_attacks = []
            # Get all attacks from defensive ships in initiative group
            for ship in defense.get_ships_by_init(speed):
                for attack in ship.get_attacks():
                    d_attacks.append(attack)

            # Apply all damage from defensive group to offensive ships
            if len(d_attacks) > 0:
                offense.apply_damage(
                    sorted(d_attacks, key=lambda atk:atk[2]),
                    damage_models.DefaultDamageDistributionModel())


            # Get all defensive attacks
            #for ship in offense.get_ships_by_init(speed):

            # Apply all damage from offensive group

            speed -= 1


    def get_attacks(self):
        all_attacks = []
        if self.offense is not None:
            all_attacks.append(self.offense.attack())
        if self.defense is not None:
            all_attacks.append(self.defense.attack())
        return all_attacks

    def get_hulls(self):
        #INCOMPLETE
        return

    def get_initiatives(self):
        #INCOMPLETE
        return

    def get_shields(self):
        #INCOMPLETE
        return

if __name__ == '__main__':
    offense = fleet_object.Fleet(name="Offense")
    offense.load_from_file('human.eFu', 1, 1, 1, 1)
    defense = fleet_object.Fleet(name="Defense")
    defense.load_from_file('human.eFu', 0, 0, 1, 0)
    print(offense)
    print(defense)
    battle = Battle("Test battle", offense, defense)
    battle.simulate(1)

    print(offense)
    print(defense)
