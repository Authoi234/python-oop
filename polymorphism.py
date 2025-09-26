# Polymorphism
# poly = many, morph = forms

class Vehicle:
    def __init__ ( self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting.")
    def stop(self):
        print("Vehicle is stopping.")

class Car(Vehicle):
    def __init__(self, brand,model,year, number_of_doors):
        super().__init__(brand,model,year)
        self.number_of_doors = number_of_doors

    def start(self):
        print("Car is starting.")

    def stop(self):
        print("Car is stopping.")
        
class Motorcycle(Vehicle):
    def __init__(self, brand,model,year):
        super().__init__(brand,model,year)

    def start(self):
        print("Motorcycle is starting.")

    def stop(self):
        print("Motorcycle is stopping.")
        
# Create a list of vehicles and inspect them
vehicles: list[Vehicle] = [
    Car("Mustang", "Ford", 2020, 5),
    Motorcycle("Scoopy", "Honda", 2022)
]

for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type (vehicle).__name__})")
    vehicle.start()
    vehicle.stop()  

# loop through the list of vehicles and inspect them
# for vehicle in vehicles:
#     if isinstance(vehicle, Car):
#        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type (vehicle).__name__})")
#        vehicle.start()
#        vehicle.stop()
#     elif isinstance(vehicle, Motorcycle):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type (vehicle).__name__})")
#         vehicle.start_bike()
#         vehicle.stop_bike()
#     else:
#         raise Exception("Object is not a valid Vehicle")