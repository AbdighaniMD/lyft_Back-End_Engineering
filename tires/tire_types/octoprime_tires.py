from tires.tire_types import Tires


class OctoprimeTire(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.tire_need_to_service = 3.0

    def needs_service(self):
        return sum(self.tire_wear) >= self.tire_need_to_service