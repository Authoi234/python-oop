class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed  
        self.owner = owner
    
    def bark(self):
        print("Whoof Whoof!")

    
class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

if __name__ == "__main__":
    owner1 = Owner("Alice", "123 Maple St", "555-1234")
    dog1 = Dog("Buddy", "Golden Retriever", owner1)
    
    print(f"Dog1's Name: {dog1.name}")
    print(f"Dog1's Breed: {dog1.breed}")
    print(f"Owner1's Name: {dog1.owner.name}")
    print(f"Owner1's Address: {dog1.owner.address}")
    print(f"Owner1's Contact Number: {dog1.owner.phone_number}")
    
    dog1.bark()

    owner2 = Owner("Bob", "456 Oak St", "555-5678")
    dog2 = Dog("Max", "Beagle", owner2)
    
    dog2.bark()

    print(dog2.owner.name)