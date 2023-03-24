import unittest
from datetime import date

from batteries.battery_type.spindler_bettery import Spindler


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-25")
        battery = Spindler(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-03-23")
        last_service_date = date.fromisoformat("2017-02-11")
        battery = Spindler(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()