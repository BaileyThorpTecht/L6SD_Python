import pandas as pd
import time

df = pd.read_excel(r"C:\Users\Bailey\Desktop\Python_Exercises\W3\rugby_players_data.xlsx")
data = df["Age"].tolist()



#Put simply, Quick Sort works by splitting the list into two parts around a 'pivot'
#with all the smaller numbers on the left, and larger numbers on the right

#The left and right halves are repeatedly put through that same splitting function
#until each half until the whole list is sorted

def QuickSort(lis):
    
    #To start, we will work within the entire list
    high = len(lis) - 1 
    low = 0             
    
    #This is the function that actually does the splitting.
    #It will split the current list into a Left and Right list.
    Partition(lis, high, low)
    
    
    return lis
        
        
        
def Partition(lis, high, low):
    #We use 'i' as a pointer. It will keep track of where things need to be moved within the list
    #The pointer starts at the left on the list
    i = low
    #The last element in the list is chosen as the pivot.
    pivot = lis[high]
    
    
    
    for j in range(low, high): #For each element in the current list... (except the pivot)
        if lis[j] < pivot: #If it is smaller than the pivot...
            lis[j], lis[i] = lis[i], lis[j] #move it to the location of the pointer 'i' by swapping
            i += 1 #and increment the pointer
            
    
    #Finally, move the pivot to the pointer by swapping.
    #This puts the pivot in the center of the list, with smaller on the left and greater on the right.
    #The pivot is also now in the correct position of the main list.
    lis[high], lis[i] = lis[i], lis[high]
    
    
    #Now that the list is split into a smaller (left) and larger (right) half,
    #we need to get the upper and lower boundary indexes of them.
    #We do this using 'i', which is where the pivot currently is
    
    #The index of 'i' itself doesnt need to be included in either because
    #The pivot is already in the final correct position
    LeftLow = low
    LeftHigh = i - 1
    RightLow = i + 1
    RightHigh = high
    
    
    #Then finally, we run each half through this function again
    #to be split repeatedly until fully sorted
    
    #But if a half contains only 1 or 0 elements, there is no need to split it again
    if LeftHigh - LeftLow > 0:
        Partition(lis, LeftHigh, LeftLow)
    if RightHigh - RightLow > 0:
        Partition(lis, RightHigh, RightLow)


startTime = time.time()
output = QuickSort(data)
endTime = time.time()
duration = endTime - startTime
print(duration)
print(output[:200])