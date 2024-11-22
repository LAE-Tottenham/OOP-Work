import math

class Measurements():
    def __init__(self, length, height):
        self.length = length
        self.height = height


class Square(Measurements):
        def __init__(self, length, height):
             super().__init__(length, height)
        
        def Area(self):
             sq_area = self.length * self.height
             print("Area of this square is", sq_area,"m²")

class Triangle(Measurements):
     def __init__(self, length, height):
             super().__init__(length, height)
        
     def Area(self):
        tri_area = (self.length * self.height) / 2
        print("Area of this square is", tri_area,"m²")

class Circle(Measurements):
     def __init__(self, length, height):
             super().__init__(length, height)
        
     def Area(self):
        cir_area = (self.length * 3.14159)
        print("Area of this circle is", cir_area,"m²")



sq_tst = Square(30, 5)
sq_tst.Area()

tri_tst = Triangle(20,5)
tri_tst.Area()

cir_tst = Circle(50,0)
cir_tst.Area()
