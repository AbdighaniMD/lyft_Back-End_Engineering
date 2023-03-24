from car import Car
from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.sternman_engine import SternmanEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine
from batteries.battery_type.nubbin_battery import Nubbin
from batteries.battery_type.spindler_bettery import Spindler
from tires.tire_types.carrigan_tires import CarriganTire
from tires.tire_types.octoprime_tires import OctoprimeTire


class CarFactory:
    @staticmethod
    def build_calliope(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tires = CarriganTire(tire_wear)
        car = Car(engine, battery, tires)
        return car
    @staticmethod
    def build_glissade(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tires = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def build_palindrome(current_date, last_service_date, warning_light_is_on, tire_wear):
        engine = SternmanEngine(warning_light_is_on)
        battery = Spindler(current_date, last_service_date)
        tires = CarriganTire(tire_wear)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def build_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tires = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def build_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tires = CarriganTire(tire_wear)
        car = Car(engine, battery, tires)
        return car