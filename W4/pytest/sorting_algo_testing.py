import pandas as pd
import pytest as pt
import openpyxl 

class Algorithms():
    
    def BubbleSort(arrIn):
        arr = list(arrIn)
        leng = len(arr)
        for i in range(leng - 1):
            for j in range(leng - i - 1):
                if arr[j] > arr[j + 1]:
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])                  
                j += 1    
            i += 1
        return arr
    
    def InsertionSort(arrIn):
        arr = list(arrIn)
        sortedArr = []
        for num in arr: #for every number in the input array...
            i = len(sortedArr) #starting at the end of the sortedArray...
            while i > 0 and num < sortedArr[i - 1]: #check if the number is smaller than the next one or at the end of the array.
                i -= 1
            else: 
                sortedArr.insert(i,num)
        return sortedArr
    
    def SelectionSort(arrIn):
        arr = list(arrIn)
        sortedArr = []
        for i in range(0,len(arr)):
            lowest = min(arr)
            lowestIndex = arr.index(lowest)
            sortedArr.append(arr.pop(lowestIndex))   
        return sortedArr
    
    def MergeSort(arrIn):
        arr = list(arrIn)
        
        if len(arr) <= 1: #if array is unit length just return it immediately
            return arr
        
        #split arr
        middle = int(len(arr) / 2)
        leftSplit = arr[:middle]
        rightSplit = arr[middle:]
        arrL = Algorithms.MergeSort(leftSplit)
        arrR = Algorithms.MergeSort(rightSplit)
        
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
        
        #use k to put the rest of a the array which the pointer hasnt gotten to
        totalLength = len(arrL) + len(arrR)
        if k < totalLength:
            while i < len(arrL):
                arrTemp.append(arrL[i])
                i += 1
            while j < len(arrR):
                arrTemp.append(arrR[j])
                j += 1
        return arrTemp

    def QuickSort(arrIn):
        arr = list(arrIn)
        
        #just sets left and right for the first iteration
        return Algorithms.QuickSortRecurse(arr, 0, len(arr)-1)
    
    def QuickSortRecurse(arr, left, right):
        while (left < right):
            i = Algorithms.Partition(arr, left, right)
            
            LSize = i - left
            RSize = right - i
            
            if LSize < RSize: #do the smaller side first
                #left
                Algorithms.QuickSortRecurse(arr, left, i - 1)
                left = i + 1 #This line is similar to recusing QuickSortRecurse again, instead relying on the while (left < right) loop
                #Algorithms.QuickSortRecurse(arr, i + 1, right)
            else:
                #right
                Algorithms.QuickSortRecurse(arr, i + 1, right)
                right = i - 1
            
        return arr
    
    #Partition takes in the list, left boundary and right boundary.
    #returns the point the pivot is at
    def Partition(arr, low, high):
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
        
        return i
        
    
# #                     # # #                     # #
# ------ Below Here Is Not Needed For Pytest ------ #
# #                     # # #                     # #


list1 = [765, 234, 512, 789, 321, 456, 876, 123, 678, 543,
890, 456, 234, 765, 321, 908, 567, 876, 345, 654,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654]

algos = Algorithms()
algoList = [algos.BubbleSort, algos.InsertionSort, algos.SelectionSort, algos.MergeSort]

#print(algoList[0](list1))

print(Algorithms.QuickSort(list1))

    

    