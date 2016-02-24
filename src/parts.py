"""
Basic ship part parent class.
"""
class Part(object):
    def __init__(self,name="",aim=0,hull=0,initiative=0,power=0,shield=0,speed=0,is_weapon=False, weapon_damage=0):
        self.name = name
        self.aim = aim
        self.hull = hull
        self.initiative = initiative
        self.power = power
        self.shield = shield
        self.speed = speed
        self.is_weapon = is_weapon
        self.weapon_damage = weapon_damage

    '''def __str__(self):
        weaponstring = ""
        if self.weapons is not None:
            for w in self.weapons:
                weaponstring = weaponstring+"\t\t["+str(w)+"]\n"
        outstring = "%s:\n\tAim=%d\n\tHull=%d\n\tInit=%d\n\tPower=%d\n\tShield=%d\n\tSpeed=%d\n\tWeapons:\n%s"%(self.name,self.aim,self.hull,self.initiative,self.power,self.shield,self.speed,weaponstring)
        return outstring'''

"""
Here are all of the ship parts.
"""
class Blank(Part):
    def __init__(self):
        Part.__init__(self,name="Blank")

class Electron_computer(Part):
    def __init__(self):
        Part.__init__(self,name="Electron Computer",aim=1)

class Hull(Part):
    def __init__(self):
        Part.__init__(self,name="Hull",hull=1)

class Improved_hull(Part):
    def __init__(self):
        Part.__init__(self,name="Improved Hull",hull=2)

class Ion_cannon(Part):
    def __init__(self):
        Part.__init__(self,name="Ion Cannon",power=-1,is_weapon=True, weapon_damage=1)

class Nuclear_drive(Part):
    def __init__(self):
        Part.__init__(self,name="Nuclear Drive",initiative=1,power=-1,speed=1)

class Nuclear_source(Part):
    def __init__(self):
        Part.__init__(self,name="Nuclear Source",power=3)

class Plasma_cannon(Part):
    def __init__(self):
        Part.__init__(self,name="Plasma Cannon",power=-2,is_weapon=True, weapon_damage=2)

'''
Lookup table for string->part
'''
part_dict = {"blank": Blank(),
    "electron_computer": Electron_computer(),
    "hull": Hull(),
    "improved_hull": Improved_hull(),
    "ion_cannon": Ion_cannon(),
    "nuclear_drive": Nuclear_drive(),
    "nuclear_source": Nuclear_source(),
    "plasma_cannon": Plasma_cannon()}

def Create_Part(part_name):
    return part_dict[part_name]

if __name__ == '__main__':
    print(part_dict['blank'])