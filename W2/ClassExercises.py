def Cars():
    class Car:
        
        def __init__(self, ma, mo, y):
            self.make = ma
            self.model = mo
            self.year = y
        
        def Start_Engine(self):
            print("vroom vroom")
        
        def PrintDetails(d):
            print(f"{d.make} model {d.model}: {d.year}")
        
        def __del__(self):
            print("car is gone :(")
            
    car1 = Car("Tesla","Y","1998")
    car2 = Car("Te","A","2024")
    car3 = Car("Bestla","Z","1884")

    car1.PrintDetails()
    car2.PrintDetails()
    car3.PrintDetails()

    del car3

def Persons():
    class person():
        
        name = "Stan"
        age = "34"
        
        def PrintDetails(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
        
        def __del__(self):
            print("The person is gone")
        
    man1 = person()
    man1.PrintDetails()
    del man1

def Rectangles():
    class Rectangle():
        def __init__(self):

            self.length = 1
            self.width = 1
            
        def __init__(self, l, w):

            self.length = l
            self.width = w
        
        
    
    rec1 = Rectangle(40, 10)
    rec2 = Rectangle()


#   
#
#
#Cars()
#Persons()
#Rectangles()
s1 = "1"
s2 = "2"

def test(a):
    s1 = a

def test(a, b):
    s1 = a
    s2 = b

test("haa")

print(s1)
print(s2)
    




input()