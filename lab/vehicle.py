class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def show(self):
        print(self.brand)

class Car(Vehicle):
    def wheels(self):
        print("4 wheels")

class Motorcycle(Vehicle):
    def wheels(self):
        print("2 wheels")
        
car = Car("Toyota")
car.show()  
car.wheels()  
motorcycle = Motorcycle("Honda")
motorcycle.show()  
motorcycle.wheels()  