class Vendor():
    def __init__(self, detailDict):
        self.detailDict = detailDict           
        
    
    def PrintDetails(self):
        #for each detail in the dict, print the name and the contents if the contents is not empty
        for s in self.detailDict:
            if self.detailDict[s] != "":
                print(f"{s}: {self.detailDict[s]}")
    
    def UpdateDetails(self):
        print("Enter new details. Press Enter without typing to keep the same.")
        
        #update each variable if input is not empty
        for s in detailList:
            newDetail = input(f"{s}: ")
            if newDetail != "":
                self.detailDict[s] = newDetail
            
        
            
#Main Functions: ------------------------------------  
def ShowMainMenu():
    while True:
        print("\nChoose a number to perform an action:")
        print("1: Add New Vendor")
        print("2: Search For a Vendor")
        print("3: Remove a Vendor")
        print("4: Update a Vendor's Details")
        print("5: Add New Detail Type")
        print("6: View all vendors")
        print("7: Close program")
        
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
            AddNewDetailType()
        elif choice == "6":
            ShowAllVendorNames()
        elif choice == "7":
            break #breaks the loop and ends the program for "7"
        else:
            print("invalid input")
            
        input("Press Enter to continue")

def AddVendor():
    print("Enter the vendor's name:")
    name = input()
    
    #Check if vendor already exists
    if name in vendorDict:
        print("A vendor with this name already exists.")
    
    else:
        detailDict = {}
        
        #hardcoded to have name go first (name was inputted already)
        detailDict[detailList[0]] = name
        
        #for every detail in the detailList, the user inputs the detail into a dictionary
        i = 1
        while i < len(detailList):
            print(f"Enter the vendor's {detailList[i]}:")
            detailDict[detailList[i]] = input()
            i += 1
        #vendor object is made with dictionary
        vendorDict[name] = (Vendor(detailDict))


def ShowSpecificVendorDetails():
    vendorClass = SearchSpecificVendor()
    if vendorClass != "failed":
            
        vendorClass.PrintDetails()


def RemoveVendor():
    vendorClass = SearchSpecificVendor()
    if vendorClass != "failed":
        
        #remove vendor from vendorDict
        vendorDict.pop(vendorClass.detailDict["Name"])
        print("Vendor removed.")


def UpdateVendorDetails():
    vendorClass = SearchSpecificVendor()
    if vendorClass != "failed":
        
        vendorDict.pop(vendorClass.detailDict["Name"]) #remove old vendor with old name from vendorDict
        vendorClass.UpdateDetails()
        vendorDict[vendorClass.detailDict["Name"]] = (vendorClass) #add vendor with new name back to vendorDict
        print("Details Updated")

def AddNewDetailType():
    print("Enter a new type of detail you want for vendors:")
    
    #adds a detail to the detailList
    newDetail = input()
    detailList.append(newDetail)
    pass

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
detailList = ["Name", "Phone Number", "Email Address"]
#code starts here ------------------------------------
print("------- Contact Book -------")
ShowMainMenu()