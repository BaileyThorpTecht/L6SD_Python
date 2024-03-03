import copy

#                                         #
# ------ design pattern: Singleton ------ #
#                                         #
def PresidentsOfficialPen():
    class PresidentsPen:

        penName = None
        instance = None
        
        def __new__(cls):
            if cls.instance == None:
                cls.penName = "pilot 51"
                cls.instance = super(PresidentsPen, cls).__new__(cls)
            return cls.instance
        
        def Write(self):
            print("scribble scribble")
    
    pen1 = PresidentsPen()
    pen2 = PresidentsPen()
    print(pen1.penName, pen2.penName)
    pen2.penName = "lamy safari" 
    print(pen1.penName, pen2.penName)
    #pen1 and pen2 always have the same penName because they are the same instance


#                                       #
# ------ design pattern: Factory ------ #
#                                       #

def CarManufacturingPlant():
    class Car():
        def Construct(self):
            pass
    
    class VDub():
        def Construct(self):
            print("VDub being put together")
    
    class Beetle():
        def Construct(self):
            print("Beetle being put together")
    
    class NissanLeaf():
        def Construct(self):
            print("Nissan Leaf being put together")
    
    class CarPlant():
        def MakeCar(model):
            if model == "vdub":
                return VDub()
            if model == "beetle":
                return Beetle()
            if model == "leaf":
                return NissanLeaf()
    
    car1 = CarPlant.MakeCar("beetle")
    car1.Construct()
    #"Beetle being put together"
    
        
#                                         #
# ------ design pattern: Prototype ------ #
#                                         #

def DrawingTool():
    class Shape():
        def __init__(self, sides, color, size):
            self.sides = sides
            self.color = color
            self.size = size
            
        def PrintDetails(self):
            print(f"{self.size} and {self.color} with {self.sides} sides")
        
        def Duplicate(self):
            return copy.copy(self)
        
    
    shape1 = Shape(3,"green", "small")
    shape2 = shape1.Duplicate()
    shape1.sides = 4
    shape2.color = "red"
    shape1.PrintDetails()
    shape2.PrintDetails()
    #both shapes are separate entities
    

#                                         #
# ------ design pattern: Singleton ------ #
#                                         #

def GlobalCounter():
     class Counter:

        count = None
        instance = None
        
        def __new__(cls):
            if cls.instance == None:
                cls.count = 0
                cls.instance = super(Counter, cls).__new__(cls)
            return cls.instance
        
        def Increment(self):
            self.count += 1
            
#                                       #
# ------ design pattern: Factory ------ #
#                                       #

def GreetingCardPersonalization():
    class Generic():
        sender = None
        recipient = None

        def AddDetails(self, sen, rec):
            self.sender = sen
            self.recipient = rec
            
        def PrintCard(self):
            print(f"A generic card from {self.sender} to {self.recipient}")
    
    class Festive():
        sender = None
        recipient = None

        def AddDetails(self, sen, rec):
            self.sender = sen
            self.recipient = rec
            
        def PrintCard(self):
            print(f"A festive card from {self.sender} to {self.recipient}")
    
    class Autumn():
        sender = None
        recipient = None

        def AddDetails(self, sen, rec):
            self.sender = sen
            self.recipient = rec
            
        def PrintCard(self):
            print(f"An autumn card from {self.sender} to {self.recipient}")
    
    class CardTemplate():
        def __init__(self, rec):
            self.recipient = rec
            
        def MakeCard(theme):
            if theme == "generic":
                return Generic()
            if theme == "festive":
                return Festive()
            if theme == "autumn":
                return Autumn()
    
    
    #is there any way to not have to repeat the functions and variables for every subclass? maybe with inheritance?
    
    card1 = CardTemplate.MakeCard("autumn")
    card1.AddDetails("Me", "You")
    card1.PrintCard()
    
            
    





#PresidentsOfficialPen()
CarManufacturingPlant()
#DrawingTool()
#GlobalCounter()
#GreetingCardPersonalization()