import pandas as pd
import pytest as pt
import openpyxl 

class Algorithms():
    
    def BubbleSort(arrIn):
        #make a copy of the input list so it returns a new list,
        #without altering the one inputted, just in case 
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
                #check if the number is smaller than the next one OR is at the end of the array.
            while i > 0 and num < sortedArr[i - 1]:
                #If so, move it to the left until it is larger or at the end
                i -= 1 
            else: 
                #then insert it into the new array
                sortedArr.insert(i,num) 
        return sortedArr
    
    def SelectionSort(arrIn):
        arr = list(arrIn)
        sortedArr = []
        
        #Until we have gone through the enitre array...
        #find the lowest number, remove it and add it to the end of a new list
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
                left = i + 1 
                #This line is similar to recusing QuickSortRecurse again, instead relying on the while loop
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