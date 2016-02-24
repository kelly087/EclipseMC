"""
This file contains the fleet class, which is a collection
for many ships. This has facilities for firing from all ships,
and calculating whether they hit. In addition, it can return
arrays containing information about the ships in the fleet.
"""

import copy as copy_module #Needed to make deep copies of fleets
import parts as ship_parts
import ships

class Fleet():
    #def __init__(self, name="", shiplist=[]):
    #    self.name = name
    #    self.shiplist = shiplist

    def __init__(self, name="", shiplist=[], filename="", num_interceptors=0, num_cruisers=0, num_dreadnaughts=0, num_starbases=0):
        self.shiplist = shiplist
        self.name = name

    def __str__(self):
        shipstring = ""
        if self.shiplist is not None:
            for i, s in zip(range(len(self.shiplist)),self.shiplist):
                shipstring = shipstring+"\t"+str(i)+". "+s.name+"\n"
        return "%s:\n%s"%(self.name,shipstring)

    def apply_damage(self, attack_list, damage_distribution_model):
        damage_distribution_model.apply_damage(self, attack_list)

    def load_from_file(self, filename, num_interceptors, num_cruisers, num_dreadnaughts, num_starbases):
        self.shiplist = []
        f = open(filename, 'r')
        line = f.readline().strip()
        for _ in range(num_interceptors):
            self.shiplist.append(ships.CreateShip("Interceptor", line))
        line = f.readline().strip()
        for _ in range(num_cruisers):
            self.shiplist.append(ships.CreateShip("Cruiser", line))
        line = f.readline().strip()
        for _ in range(num_dreadnaughts):
            self.shiplist.append(ships.CreateShip("Dreadnaught", line))
        line = f.readline().strip()
        for _ in range(num_starbases):
            self.shiplist.append(ships.CreateShip("Starbase", line))
        f.close()

    def add(self, ship):
        self.shiplist.append(ship)

    def get_ships_by_init(self, init):
        '''
        Returns a list of all ships with a given get_initiative
        '''
        s_list = []
        for s in self.shiplist:
            if s.get_initiative() == init:
                s_list.append(s)

        return s_list

    def copy(self):
        return copy_module.deepcopy(self)

if __name__ == '__main__':
    fleet = Fleet(name="test")
    fleet.load_from_file("human.eFu", 1, 1, 1, 1)
    print(fleet)