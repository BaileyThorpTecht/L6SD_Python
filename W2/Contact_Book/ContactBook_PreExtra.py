#make a class for each vendor
#for 'extra details', ill make it so you can have as many types of details as you want.
#   OR ill let you do a y/n when adding or updating a vendor to add more details

#todo:
#add 'extra details'

class Vendor():
    def __init__(self, name, phoneNumber, email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
    
    def PrintDetails(self):
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"Email: {self.email}")
        #will need more for 'extra details' here
    
    def UpdateDetails(self):
        print("Enter new details. Press Enter without typing to keep the same.")
        oldName = self.name
        #repeated code
        i = input("Name: ")
        if i != "":
            self.name = i
        i = input("Phone Number: ")
        if i != "":
            self.phoneNumber = i
        i = input("Email Address: ")
        if i != "":
            self.email = i
            
#Main Functions: ------------------------------------  
def ShowMainMenu():
    while True:
        print("\nChoose a number to perform an action:")
        print("1: Add New Vendor")
        print("2: Search For a Vendor")
        print("3: Remove a Vendor")
        print("4: Update a Vendor's Details")
        print("5: Add Extra Detail Options")
        print("6: View all vendors")
        print("7: Close program")
        
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
            #might not need to exist
            AddExtraCategory()
        elif choice == "6":
            ShowAllVendorNames()
        elif choice == "7":
            break
        else:
            print("invalid input")

def AddVendor():
    print("Enter the vendor's name:")
    name = input()
    if name in vendorDict:
        print("A vendor with this name already exists.")
    else:
        print("Enter the vendor's phone number")
        phone = input()
        print("Enter the vendor's email address")
        email = input()
        vendorDict[name] = (Vendor(name, phone, email))
        #extra details


def ShowSpecificVendorDetails():
    vendorClass = SearchSpecificVendor()
    if vendorClass != "failed":
            
        vendorClass.PrintDetails()


def RemoveVendor():
    vendorClass = SearchSpecificVendor()
    if vendorClass != "failed":
        
        vendorDict.pop(vendorClass.name)
        print("Vendor removed.")


def UpdateVendorDetails():
    
    vendorClass = SearchSpecificVendor()
    if vendorClass != "failed":
        
        vendorDict.pop(vendorClass.name) #remove old vendor with old name from dict
        vendorClass.UpdateDetails()
        vendorDict[vendorClass.name] = (vendorClass) #add vendor with new name back to dict
        print("Details Updated")
        
        
def AddExtraCategory():
    pass


def ShowAllVendorNames():
    i = 1
    for name in vendorDict:
        print(f"{i}: {name}")
        i += 1

#other functions ------------------------------------
def SearchSpecificVendor():
    print("Enter name of Vendor")
    searchingFor = input()
    try:
        vendorClass = vendorDict[searchingFor]
    except:
        print("Vendor does not exist.")
        return "failed"
    else:
        return vendorClass

    
#global vars ------------------------------------
vendorDict = {}

#code starts here ------------------------------------
print("------- Contact Book -------")
ShowMainMenu()