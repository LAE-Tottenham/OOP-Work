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

         def Perimeter(self):
             sq_peri = (self.length * 2) + (self.length * 2)
             print("The perimeter of this square is", sq_peri,"m")

class Rectangle(Measurements):
         def __init__(self, length, height):
             super().__init__(length, height)
        
         def Area(self):
             rec_area = self.length * self.height
             print("Area of this square is", rec_area,"m²")
     
         def Perimeter(self):
             rec_peri = (self.length * 2) + (self.length * 2)
             print("The perimeter of this square is", rec_peri,"m")

class Triangle(Measurements):    
         def __init__(self, length, height):
             super().__init__(length, height)
        
         def Area(self):
               tri_area = (self.length * self.height) / 2
               print("Area of this square is", tri_area,"m²")
        
         def Perimeter(self):
               hypotenuse = math.sqrt((self.length**2)+(self.height**2))
               tri_peri = self.length + self.height + hypotenuse
               tri_peri = round(tri_peri, 3)
               print("The perimeter of this square is", tri_peri,"m (3 d.p)")

         def Hypotenuse(self):
               hypotenuse = math.sqrt((self.length**2)+(self.height**2))
               hypotenuse = round(hypotenuse, 3)
               print("The hypotenuse of the triangle is",hypotenuse,"m (3 d.p)")

class Circle(Measurements):
         def __init__(self, length, height):
               super().__init__(length, height)
        
         def Area(self):
               cir_area = (self.length * 3.14159)
               cir_area = round(cir_area,3)
               print("Area of this circle is", cir_area,"m² (3 d.p)")
        
         def Perimeter(self):
               radius = self.length / 2
               cir_peri = radius * 2 * 3.14159
               cir_peri = round(cir_peri, 3)
               print("The perimeter of this circle is", cir_peri,"m (3 d.p)")





sq_tst = Square(30, 5)
sq_tst.Perimeter()

rec_tst = Rectangle(50,4)
rec_tst.Perimeter()

tri_tst = Triangle(20,5)
tri_tst.Hypotenuse()

cir_tst = Circle(50,0)
cir_tst.Perimeter()
