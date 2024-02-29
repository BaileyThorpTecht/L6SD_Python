import pandas as pd
import pytest as pt

#is it really necessary to have the algos in a class?
#if not, maybe just copy and paste the w3 sorting algos

class Algorithms():
    
    def BubbleSort(self, arr):
        
        leng = len(arr)
        for i in range(leng - 1):
            for j in range(leng - i - 1):
                if arr[j] > arr[j + 1]:
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])                  
                j += 1    
            i += 1
        return arr
    
    def InsertionSort(self, arr):
    
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
    
    def MergeSort(self, arr):

        if len(arr) <= 1: #if array is unit length just return it immediately
            return arr
        
        #split arr
        middle = int(len(arr) / 2)
        leftSplit = arr[:middle]
        rightSplit = arr[middle:]
        arrL = self.MergeSort(leftSplit)
        arrR = self.MergeSort(rightSplit)
        
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
#print(algoList[1](list1))
#print(algoList[2](list1))
#print(algoList[3](list1))

    

    