class Car:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
    
    def display(self):
        print(f"{self.year} {self.color} {self.make} {self.model}")
    
    def set_color(self, new_color):
        self.color = new_color
    
    def set_make(self, new_make):
        self.make = new_make
    
    def set_model(self, new_model):
        self.model = new_model
        
c = Car("Toyota", "Corolla", "Red", 2020)
c.display()  
c.set_color("Blue")
c.display() 
c.set_make("Honda")
c.set_model("Civic")
c.display()  