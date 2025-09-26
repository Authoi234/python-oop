# Inheritance

class Veicle:
    def __init__ ( self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Veichle is starting.")
    def stop(self):
        print("Veichle is stopping.")

class Car(Veicle):
    def __init__(self, brand,model,year,number_of_doors, number_of_wheels):
        super().__init__(brand,model,year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

class Bike(Veicle):
    def __init__(self, brand,model,year,number_of_wheels):
        super().__init__(brand,model,year)
        self.number_of_wheels = number_of_wheels

car = Car("Mustang", "Ford", 2020, 5, 4)
bike = Bike("Scoopy", "Honda", 2022, 2)
print(car.__dict__)
print(bike.__dict__)
car.start()
bike.start()