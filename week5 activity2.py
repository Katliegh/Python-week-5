class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

vehicles = [car, plane, boat, bicycle]
for vehicle in vehicles:
    vehicle.move()

