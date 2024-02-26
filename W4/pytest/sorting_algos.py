import pandas as pd
import pytest as pt

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
    

    

    