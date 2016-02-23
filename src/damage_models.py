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
    '''
    def apply_damage(self, fleet, attack_list):
        for ship in fleet.shiplist:
            print(self.calculate_threat(ship))

    def calculate_threat(self, ship):
        threat = 0
        for part in ship.parts:
            threat += part.weapon_damage
            threat += (part.aim * 0.1)

        return threat

if __name__ == '__main__':
    import ships
    ship = ships.CreateShip("Cruiser", "hull,blank,ion_cannon,nuclear_source,electron_computer,nuclear_drive")
    model = DefaultDamageDistributionModel()
    print(model.calculate_threat(ship))