from sorting_algos import Algorithms 
import pandas as pd
import pytest as pt

df = pd.read_excel(r"C:\Users\Bailey\Desktop\Python_Exercises\W3\rugby_players_data_extra.xlsx")
unsorted_list = df["Age"]
sorted_list = ["Sorted Age"] #just have a sorted list in the excel file

current_list = unsorted_list 

def test_bubble_sort():
    assert Algorithms.BubbleSort(current_list) == sorted(current_list)
    
    
    

#what do?