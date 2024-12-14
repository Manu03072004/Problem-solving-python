class vehicle:
    def description(self):
        print("this is a vehicle")
class Engine:
    def engine_type(self):
        print("engine type is diesel")
class car(vehicle,Engine):
    def wheel(self):
        print("car has four wheels")
car=car()
car.description()
car.engine_type()