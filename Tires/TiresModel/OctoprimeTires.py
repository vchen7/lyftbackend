from Tires import Tires
class Octoprime(Tires):
    def __init__(self, wear):
        self.wear = wear
        self.tire_need: = 3

    def needs_service(self):
        if sum(self.wear) >= self.tire_need
            return True
        return False