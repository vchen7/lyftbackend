import unittest
from datetime import datetime

from engine.model.capulet_engine import CapuletEngine
from engine.model.sternman_engine import SternmanEngine
from engine.model.willoughby_engine import WilloughbyEngine
from Battery.BatteryModel.NubbinBattery import NubbinBattery
from Battery.BatteryModel.SpindlerBattery import SpindlerBattery
from Tires.TiresModel import CarriganTires
from Tires.TiresModel import OctoprimeTires

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 10000000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 1
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
        
class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
        
class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 100000000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 10
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())    
           
class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2023, 1, 1)
        last_service_date = datetime.datetime(2010,1,1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2023, 1, 1)
        last_service_date = datetime.datetime(2022,12,25)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2023, 1, 1)
        last_service_date = datetime.datetime(2010,1,1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2023, 1, 1)
        last_service_date = datetime.datetime(2022,12,25)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
        
class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9, 0.9, 0.9, 0.9]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.1, 0.1, 0.1]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())
        
class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9, 0.9, 0.9, 0.9]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.1, 0.1, 0.1]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())  
             
if __name__ == '__main__':
    unittest.main()
