
class Vendor():
    def __init__(self, name, phoneNumber, email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
    
    def PrintDetails(self):
        print(f"\nName: {self.name}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"Email Address: {self.email}")      
            
#Main Functions: ------------------------------------  
def ShowMainMenu():
    while True:
        print("\nChoose a number to perform an action:")
        print("1: Add New Vendor")
        print("2: Search For a Vendor")
        print("3: Remove a Vendor")
        print("4: View all vendors")

    
        #call a function depending on what the user inputs
        choice = input()
        if choice == "1":
            AddVendor()
        elif choice == "2":
            SearchVendor()
        elif choice == "3":
            RemoveVendor()
        elif choice == "4":
            ShowAllVendors()
        else:
            print("invalid input")

def AddVendor():
    print("Enter the vendor's name:")
    name = input()
    
    #Check if vendor with that name already exists in the dictionary
    if name in vendorDict:
        print("A vendor with this name already exists.")
    else:
        #get new vendor details
        print("Enter the vendor's phone number")
        phone = input()
        print("Enter the vendor's email address")
        email = input()
        
        #Add an entry to a dictionary, with the inputted name as the key
        #and a new Vendor object with the inputted details as the value
        vendorDict[name] = (Vendor(name, phone, email))


def SearchVendor():
    print("Enter name of Vendor")
    searchedName = input()
    
    try: #look for vendor class by name in vendorDict
        vendorClass = vendorDict[searchedName]  
    except :#excepts if vendor does not exist.
        print("Vendor does not exist.")
    else: #prints details if the vendor is found     
        vendorClass.PrintDetails()


def RemoveVendor():
    print("Enter name of Vendor")
    searchedName = input()
    
    try: #look for vendor class by name in vendorDict
        vendorClass = vendorDict[searchedName]  
    except :#excepts if vendor does not exist.
        print("Vendor does not exist.")
    else: #removes vendor if it is found     
        vendorDict.pop(vendorClass.name)
        print("Vendor removed.")


def ShowAllVendors():
    #prints details of every vendor
    for name in vendorDict:
        vendorDict[name].PrintDetails()
    
#global vars ------------------------------------
vendorDict = {}

#code starts here ------------------------------------
print("------- Contact Book -------")
ShowMainMenu()