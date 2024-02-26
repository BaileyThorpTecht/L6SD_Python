def Single():
    
    class animal():
        #def __init__():    
        sound = "placeholder"
        def make_sound(self):
            print(self.sound)
    
    class dog(animal):
        #def __init__():
        sound = "woof"

    anim = dog()
    anim.make_sound()


def Multiple():
    
    class Person():
        name = "john"
        age = "22"
    class Skills():
        progSkill = 7
        commSkill = 4
    class Employee(Person, Skills):
        def show(self):
            print(self.name)
            print(self.age)
            print(self.progSkill)
            print(self.commSkill)
    
    me = Employee()
    me.show()
    
def Multilevel():
    class Vehicle():
        def StartEngine():
            print("vroom vroom")
    class Car(Vehicle):
        def Drive():
            print("vrrrrrrrrrr")
    class EV(Car):
        def ChargeBattery():
            print("hmmmmmmmmmm")
    
    myVehicle = EV()
    

def Zoo():
    class Animal:
        def __init__(self, name, species):
            self.name = name
            self.species = species

        def make_sound(self):
            print("Generic animal sound")

    class Mammal(Animal):
        def __init__(self, name, species, fur_color):
            super().__init__(name, species)
            self.fur_color = fur_color

        def give_birth(self):
            print(f"{self.name} is giving birth")

    class Bird(Animal):
        def __init__(self, name, species, feather_color):
            super().__init__(name, species)
            self.feather_color = feather_color

        def fly(self):
            print(f"{self.name} is flying")
    #end of provided code
    class Penguin(Bird):
        def __init__(self, name, beak_color):
            super().__init__(name, "penguin", "black")
            self.beak_color = beak_color

        def fly(self):
            print("penguins actually cant fly lmao")

    firstPeng = Penguin("John", "orange")
    firstPeng.fly()
    firstPeng.make_sound()
            

def School():
    class Subject:
        def __init__(self, name):
            self.name = name

        def study(self):
            print(f"Studying {self.name}")

    class Math(Subject):
        def __init__(self, name, difficulty_level):
            super().__init__(name)
            self.difficulty_level = difficulty_level

        def solve_problem(self):
            print(f"Solving a {self.difficulty_level} math problem")

    class Language(Subject):
        def __init__(self, name, language_type):
            super().__init__(name)
            self.language_type = language_type

        def practice_language(self):
            print(f"Practicing {self.language_type} language")
    #end of provided code





#Single()
#Multiple()
#Multilevel()
#Zoo()
School()
input()