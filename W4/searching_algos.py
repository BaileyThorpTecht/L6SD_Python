import pandas as pd

def LinearSearch(arr, searchTerm):
    for i in range(0,len(arr)):
        if arr[i] == searchTerm:
            return i
    return "Not found"

def BinarySearch(arr, searchTerm):
    low = 0
    high = len(arr) - 1
    while high - low > 0:
        median = int((high + low) / 2)
        medianValue = arr[median]
        if medianValue < searchTerm:
            low = median + 1
        elif medianValue > searchTerm:
            high = median - 1
        elif medianValue == searchTerm:
            return median
    return "Not found"

def BreadthFirstSearch():
    pass

def depthFirstSearch():
    pass
        
    
    
    
    
    
    
    
listRandom = [765, 234, 512, 789, 321, 456, 876, 123, 678, 543,
890, 456, 234, 765, 321, 908, 567, 876, 345, 654,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654]
listSorted = [123, 123, 123, 123, 234, 234, 321, 321, 321, 321,
345, 345, 345, 345, 432, 432, 432, 456, 456, 512,
543, 567, 567, 567, 567, 654, 654, 654, 654, 678,
765, 765, 765, 765, 789, 789, 789, 789, 876, 876,
876, 876, 876, 890, 890, 890, 890, 908, 908, 908]


searchTerm = 654
position = BinarySearch(listSorted, searchTerm)
print(position)
