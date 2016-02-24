class DamageDistributionModel():
    '''
    Empty structure base class for damage distribution
    '''
    def apply_damage(self, fleet, attack_list):
        '''
        Choose which ships in fleet to attack with list of attacks
        attack_list is tuple (adjusted roll value, damage value)
        '''
        return NotImplemented

    def calculate_threat(self, ship):
        '''
        Calculates the threat of a given ship
        '''
        return NotImplemented
    
class DefaultDamageDistributionModel(DamageDistributionModel):
    '''
    Default model to choose how to apply damage to a fleet

    fleet.shiplist is a list of all ships in fleet
    attack_list is an array of tuples (roll, aim, damage) sorted by highest damage first
    '''
    def apply_damage(self, fleet, attack_list):
        # Sort ships by threat level, then by hull
        ships = []
        for ship in fleet.shiplist:
            ships.append((ship, self.calculate_threat(ship), ship.get_hp()))

        ships.sort(key=lambda ship:ship[2], reverse=True)
        ships.sort(key=lambda ship:ship[1], reverse=True)

        # Run attacks
        for atk in attack_list:
            used = False # boolean if attack has been used
            if atk[0] == 1:
                continue # ignore 1 rolls

            # Check if can one shot
            for ship in ships:
                if not ship[0].is_alive():
                    continue # Skip dead ships

                # Check if roll can hit ship
                if atk[0] == 6 or atk[0] + atk[1] - ship[0].get_shield() >= 6:
                    if ship[0].get_hp() <= atk[2]:
                        # Damage ship
                        ship[0].take_damage(atk[2])
                        used = True
                        break # break out of ship for loop and move to next attack if it exists

            # Hit first ship can hit
            if not used:
                for ship in ships:
                    if not ship[0].is_alive():
                        continue # skip dead ships
                    # Check if roll can hit ship
                    if atk[0] == 6 or atk[0] + atk[1] - ship[0].get_shield() >= 6:
                        # Damage ship
                        ship[0].take_damage(atk[2])
                        used = True
                        break # break out of ship for loop and move to next attack if it exists

    def calculate_threat(self, ship):
        '''
        Default threat level is calculated damage per turn
        '''
        aim = 1
        damage = 0
        for part in ship.parts:
            aim += part.aim
            damage += part.weapon_damage

        if aim > 5:
            aim = 5

        return damage * (aim / 6.0) # aim / 6.0 should be estimated hit chance

if __name__ == '__main__':
    import ships
    ship = ships.CreateShip("Cruiser", "hull,blank,ion_cannon,nuclear_source,electron_computer,nuclear_drive")
    model = DefaultDamageDistributionModel()
    print(model.calculate_threat(ship))