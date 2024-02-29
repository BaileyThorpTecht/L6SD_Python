import time
import pandas as pd
import numpy as np


###### sorting algos

def BubbleSort(arr):

    leng = len(arr)
    #i = 0
    #while i < leng - 1: #number of times to iterate
    for i in range(leng - 1):
        #j = 0
        #while j < leng - 1: #iterating through the array. could do: j < len - i - 1 to be more optimal
        for j in range(leng - i - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j]) #swap
                
            j += 1    
        i += 1
    return arr


def InsertionSort(arr):
    
    sortedArr = []
    for num in arr: #for every number in the input array...
        i = len(sortedArr) #starting at the end of the sortedArray...
        while i > 0 and num < sortedArr[i - 1]: #check if the number is smaller than the next one or at the end of the array.
            i -= 1
        else: 
            sortedArr.insert(i,num)
    
    return sortedArr

def SelectionSort(self, arrIn):
    arr = list(arrIn)
    sortedArr = []
    for i in range(0,len(arr)):
        lowest = min(arr)
        lowestIndex = arr.index(lowest)
        sortedArr.append(arr.pop(lowestIndex))
    
    return sortedArr
    

def MergeSort(arr):

    if len(arr) <= 1: #if array is unit length just return it immediately
        return arr
    
    #split arr
    middle = int(len(arr) / 2)
    leftSplit = arr[:middle]
    rightSplit = arr[middle:]
    arrL = MergeSort(leftSplit)
    arrR = MergeSort(rightSplit)
    
    #i is pointer for arrL, j is pointer for arrR. K is for later
    i = j = k = 0
    arrTemp = []
    
    #while neither pointers have exceeded the list:
    while i < len(arrL) and j < len(arrR):
        if arrL[i] < arrR[j]:
            arrTemp.append(arrL[i])
            i += 1
        else:
            arrTemp.append(arrR[j])
            j += 1
        k += 1
    
    #use k to put the rest of a the array which the pointer hasnt gotten through into the arrTempt
    totalLength = len(arrL) + len(arrR)
    if k < totalLength: #'if' instead of 'while' because duh
        while i < len(arrL):
            arrTemp.append(arrL[i])
            i += 1
        while j < len(arrR):
            arrTemp.append(arrR[j])
            j += 1
    return arrTemp





def QuickSort(arr):
    high = len(arr) - 1
    low = 0
    Partition(arr, high, low)
    return arr
        
def Partition(arr, high, low):
    i = low #pointer
    pivot = arr[high]
    
    #move elements smaller than pivot to left
    for j in range(low, high):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    #swap pivot with pointer. all smaller is on the left, larger on the right
    #pivot is in the correct position
    arr[high], arr[i] = arr[i], arr[high]
    
    #partition again on the left and right
    LLow = low
    LHigh = i - 1
    RLow = i + 1
    RHigh = high
    if LHigh - LLow > 0:
        Partition(arr, LHigh, LLow)
    if RHigh - RLow > 0:
        Partition(arr, RHigh, RLow)
        
        
        
        
        
        
######Other Functions

def TestSorting(SortingMethod, data):
    startTime = time.time()
    sortedArr = SortingMethod(data)
    endTime = time.time()
    duration = endTime - startTime
    print(f"{SortingMethod.__name__}: {round(duration, 3)}")
    #print(sortedArr[:30])

######
###### ##Code Starts Here
######

list0 = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45]
list1 = [765, 234, 512, 789, 321, 456, 876, 123, 678, 543,
890, 456, 234, 765, 321, 908, 567, 876, 345, 654,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654]

df = pd.read_excel(r"C:\Users\Bailey\Desktop\L6SD_Python\W3\rugby_players_data_extra.xlsx")
#columns names:
#Name Age Height Gender 'Sorted Name' 'Reversed Name' Empty
#probably just use 'Age' for duplicate data
colName = "Name"
colData = df[colName]

TestSorting(BubbleSort, colData.tolist())
TestSorting(InsertionSort, colData.tolist())
TestSorting(SelectionSort, colData.tolist())
TestSorting(MergeSort, colData.tolist())
TestSorting(QuickSort, colData.tolist()) 

