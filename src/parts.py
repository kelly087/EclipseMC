"""
This is a template for ship parts.
"""

import weapons as weapon_objects

class Part(object):
    def __init__(self,name="",aim=0,hull=0,initiative=0,power=0,shield=0,speed=0,weapons=None):
        self.name = name
        self.aim = aim
        self.hull = hull
        self.initiative = initiative
        self.power = power
        self.shield = shield
        self.speed = speed
        self.weapons = weapons

    def __str__(self):
        weaponstring = ""
        if self.weapons is not None:
            for w in self.weapons:
                weaponstring = weaponstring+"\t\t["+str(w)+"]\n"
        outstring = "%s:\n\tAim=%d\n\tHull=%d\n\tInit=%d\n\tPower=%d\n\tShield=%d\n\tSpeed=%d\n\tWeapons:\n%s"%(self.name,self.aim,self.hull,self.initiative,self.power,self.shield,self.speed,weaponstring)
        return outstring

class Ion_cannon(Part):
    def __init__(self):
        Part.__init__(self,name="Ion Cannon",power=-1,weapons=[weapon_objects.Ion_cannon()])

class Electron_computer(Part):
    def __init__(self):
        Part.__init__(self,name="Electron Computer",aim=1)

class Hull(Part):
    def __init__(self):
        Part.__init__(self,name="Hull",hull=1)

class Improved_hull(Part):
    def __init__(self):
        Part.__init__(self,name="Improved Hull",hull=2)

if __name__ == '__main__':
    ic = Ion_cannon()
    print ic
    ih = Improved_hull()
    print ih
    ec = Electron_computer()
    print ec