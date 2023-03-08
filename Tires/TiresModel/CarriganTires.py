from Tires import Tires


class CarriganTires(Tires):
    def __init__(self, wear):
        self.wear = wear
        self.tire_need: = 0.9

    def needs_service(self):
        for tire in self.wear:
            if tire >= self.tire_need:
                return True
        return False