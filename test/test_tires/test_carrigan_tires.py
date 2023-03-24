import unittest

from tires.tire_types.carrigan_tires import CarriganTire


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.1, 0.3, 0.2, 0.9]
        tires = CarriganTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.2, 0.4, 0.2]
        tires = CarriganTire(tire_wear)
        self.assertFalse(tires.needs_service())