import unittest
from datetime import date

from batteries.battery_type.nubbin_battery import Nubbin

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-03-23")
        last_service_date = date.fromisoformat("2021-01-25")
        battery = Nubbin(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-03-23")
        last_service_date = date.fromisoformat("2010-02-08")
        battery = Nubbin(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()