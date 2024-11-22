class Animal:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        
    def play(self, ani_2):
        print(self.name, "is playing with", ani_2.name)

    def fight(self, ani_2):
        print(self.name, "is fighting with", ani_2.name)

class Cat(Animal):
    def __init__(self, name, colour, breed):
        super().__init__(name, colour)
        self.breed = breed
    
    def makenoise(self):
        print("Meow!")
    
    def breed_type(self):
        print(self.name, "is a", self.breed)

class Dog(Animal):
    def __init__(self, name, colour, breed):
        super().__init__(name, colour)
        self.breed = breed
    
    def makenoise(self):
        print("Woof!")
    
    def breed_type(self):
        print(self.name, "is a", self.breed)

catname = Cat("Flakey","black","Normal cat")
dogname = Dog("Eddie","brown","Saussage dog")
nabr_cat = Cat("Garfield","ginger","Cartoon cat")
nabr_dog = Dog("Odie","cream & brown","Cartoon dog")

catname.makenoise()
dogname.makenoise()
catname.play(nabr_cat)
dogname.play(nabr_dog)
catname.fight(dogname)
nabr_dog.fight(nabr_cat)
dogname.breed_type()
catname.breed_type()