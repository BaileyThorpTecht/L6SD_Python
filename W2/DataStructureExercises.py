def listEx():
    shoppingList = []
    shoppingList.append("apple")
    shoppingList.append("banana")
    shoppingList.append("orange")
    print(shoppingList)
    #part 2
    shoppingList.append("grape")
    shoppingList.remove("banana")
    print(shoppingList)

def tupleEx():
    coordinates = (30,120)
    print(coordinates)
    coordinates = (40,120)
    print(coordinates)
    #part 2
    print(coordinates[1])
    try:
        coordinates[1] = 90
    except:
        print("Error: can't update a tuple")
    else:
        print(coordinates)

def dictionaryEx():
    library = {"1984":"George", 
               "The Windup Girl":"Pacobeli",
               "The Rest of Us Just Live Here":"I forgot"}
    print(library)
    #part 2
    nums = ["Great", "four", "greeting", "a", "what"]
    numDictionary = {}
    for n in nums:
        numDictionary.update({n:len(n)})
    print(numDictionary)

def setEx():
    primeSet = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}
    fibSet = {1, 1, 2, 3, 5, 8, 13, 21}
    newSet = primeSet.intersection(fibSet)
    print(newSet)
    #part 2
    dupeList = [1, 1, 3, 4, 6, 6, 7, 8, 8, 8, 12, 13]
    tempSet = set(dupeList)
    newList = list(tempSet)
    print(newList)

def stackEx():
    #could just do list.reverse() but ok
    list1 = ["first", "second", "third", "fourth"]
    listRev = []
    while len(list1) > 0:
        listRev.append(list1.pop())
    print(listRev)
    #part2
    actionsList = []
    def AddAction():
        actionsList.append("[action here]")
    def UndoAction():
        actionsList.pop()

def queueEx():
    todoList = []
    def AddTask():
        todoList.append("[task here]")
    def CompleteNextTask():
        todoList.pop(0)
    #part2
    queue = []
    def AddCustomer():
        queue.append("[customer name here]")
    def ServeNextCustomer():
        queue.pop(0)
    
    
        
    
        




exers = (listEx, tupleEx, dictionaryEx, setEx, stackEx, queueEx)
#i = int(input())
i = 5
exers[i-1]()
