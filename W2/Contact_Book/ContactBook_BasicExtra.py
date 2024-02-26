
class Vendor():
    def __init__(self, name, phoneNumber, email, extra):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.extra = extra
        
    
    def PrintDetails(self):
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"Email Address: {self.email}")
        if self.extra != "": #does not print notes if its empty
            print(f"Notes: {self.extra}")
    
    def UpdateDetails(self):
        print("Enter new details. Press Enter without typing to keep the same.")
        
        #update each variable if input is not empty
        i = input("Name: ")
        if i != "":
            self.name = i
        i = input("Phone Number: ")
        if i != "":
            self.phoneNumber = i
        i = input("Email Address: ")
        if i != "":
            self.email = i
        i = input("Notes: ")
        if i != "":
            self.extra = i
        
            
#Main Functions: ------------------------------------  
def ShowMainMenu():
    while True:
        print("\nChoose a number to perform an action:")
        print("1: Add New Vendor")
        print("2: Search For a Vendor")
        print("3: Remove a Vendor")
        print("4: Update a Vendor's Details")
        print("5: View all vendors")
        print("6: Close program")
        
        #call a function depending on what the user inputs
        choice = input()
        if choice == "1":
            AddVendor()
        elif choice == "2":
            ShowSpecificVendorDetails()
        elif choice == "3":
            RemoveVendor()
        elif choice == "4":
            UpdateVendorDetails()
        elif choice == "5":
            ShowAllVendorNames()
        elif choice == "6":
            break #breaks the loop and ends the program for "6"
        else:
            print("invalid input")

def AddVendor():
    print("Enter the vendor's name:")
    name = input()
    
    #Check if vendor already exists
    if name in vendorDict:
        print("A vendor with this name already exists.")
    
    #get vendor details then add a new Vendor object to vendorDict
    else:
        print("Enter the vendor's phone number")
        phone = input()
        print("Enter the vendor's email address")
        email = input()
        print("Enter any extra notes for this vendor. Or press Enter to leave empty")
        extra = input()
        vendorDict[name] = (Vendor(name, phone, email, extra))


def ShowSpecificVendorDetails():
    vendorClass = SearchSpecificVendor()
    if vendorClass != "failed":
            
        vendorClass.PrintDetails()


def RemoveVendor():
    vendorClass = SearchSpecificVendor()
    if vendorClass != "failed":
        
        #remove vendor from vendorDict
        vendorDict.pop(vendorClass.name)
        print("Vendor removed.")


def UpdateVendorDetails():
    
    vendorClass = SearchSpecificVendor()
    if vendorClass != "failed":
        
        vendorDict.pop(vendorClass.name) #remove old vendor with old name from vendorDict
        vendorClass.UpdateDetails()
        vendorDict[vendorClass.name] = (vendorClass) #add vendor with new name back to vendorDict
        print("Details Updated")
        

def ShowAllVendorNames():
    #prints every vendor name along with a number for each one
    i = 1
    for name in vendorDict:
        print(f"{i}: {name}")
        i += 1

#other functions ------------------------------------
def SearchSpecificVendor():
    print("Enter name of Vendor")
    searchingFor = input()
    
    #look for vendor class by name in vendorDict
    try: 
        vendorClass = vendorDict[searchingFor]
        
    #excepts if vendor does not exist. Returns 'failed' to stop the higher function
    except:
        print("Vendor does not exist.")
        return "failed"
    
    #returns the vendor class if it is found
    else:
        return vendorClass

    
#global vars ------------------------------------
vendorDict = {}

#code starts here ------------------------------------
print("------- Contact Book -------")
ShowMainMenu()