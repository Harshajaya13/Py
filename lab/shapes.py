class Shape:
    def area(self): pass

class Rectangle(Shape):
    def area(self,l,b): print(l*b)

class Circle(Shape):
    def area(self,r): print(3.14*r*r)

class Triangle(Shape):
    def area(self,b,h): print(0.5*b*h)
    
r1 = Rectangle()
r1.area(5,6)    
c1 = Circle()
c1.area(7)
t1 = Triangle()
t1.area(5,6)