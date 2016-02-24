"""
This file contains the ship parent class as well as child classes for each of the the ships.
"""

import copy as copy_module #Needed to make deep copies of ships
import parts as ship_parts
import random

class Ship(object):
    def __init__(self,name="",aim=0,initiative=0,power=0,shield=0,parts=[],damage=0):
        self.name = name
        self.parts = parts
        self.aim = aim
        self.initiative = initiative
        self.power = power
        self.shield = shield
        self.damage = damage

    def __str__(self):
        partsstring = ""
        if self.parts is not None:
            for i,p in zip(range(len(self.parts)),self.parts):
                partsstring = partsstring+"\t"+str(i)+". "+p.name+"\n"
        return "%s:\n%s"%(self.name,partsstring)

    def __cmp__(self, obj):
        if obj is None or not isinstance(obj,Ship):
            raise Exception("Cannot compare to type "+str(obj)+".")
        return cmp(-self.get_initiative(),-obj.get_initiative())

    def get_attacks(self):
        '''
        retruns an array of tuples with:
            corrected dice roll (roll + targetting computer)
            damage possible from attack
        '''
        shots = []

        # Calculate adjusted aim
        aim = self.aim
        for part in self.parts:
            aim += part.aim

        # append all parts that are weapons with a random roll for that weapon
        for part in self.parts:
            if part.is_weapon:
                shots.append((random.randint(1,6) + aim, part.weapon_damage))

        return shots


    def attack(self):
        aim = self.aim
        weaponlist = []
        barrage = []
        for part in self.parts:
            aim+=part.aim
            if part.weapons is not None:
                for weapon in part.weapons:
                    weaponlist.append(weapon)
        for weapon in weaponlist:
            shot = weapon.fire()
            shot.append(shot[0]+aim)
            barrage.append(shot)
        return barrage

    def copy(self):
        return copy_module.deepcopy(self)

    def get_hull(self):
        hull = 0
        for part in self.parts:
            hull+=part.hull
        return hull

    def get_initiative(self):
        init = self.initiative
        for part in self.parts:
            init+=part.initiative
        return init

    def get_shield(self):
        shield = self.shield
        for part in self.parts:
            shield+=part.shield
        return shield

    def swap(self,part,index):
        if self.parts is None:
            raise Exception("Swap attempted with no parts.")
        if index > len(self.parts) or index < 0:
            raise Exception("Swapped part index is invalid.")
        self.parts[index] = part
        return

def CreateShip(ship_name, csv_line):
    '''
    This function creates a ship from a name and comma separated line
    '''
    speed = 0
    if ship_name == "Interceptor":
        speed = 2
    elif ship_name == "Cruiser":
        speed = 1
    elif ship_name == "Dreadnaught":
        speed = 0
    elif ship_name == "Starbase":
        speed = 4

    part_list = []
    for p in csv_line.split(','):
        part_list.append(ship_parts.Create_Part(p))
    return Ship(name=ship_name, parts=part_list, initiative=speed)