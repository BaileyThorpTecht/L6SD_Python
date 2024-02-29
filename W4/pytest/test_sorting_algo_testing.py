from sorting_algo_testing import Algorithms 
import pandas as pd
import pytest as pt

df = pd.read_excel(r"C:\Users\Bailey\Desktop\L6SD_Python\W3\rugby_players_data_extra.xlsx")
sorted_data = df["Sorted Name"]
unsorted_data = df["Name"]
reversed_data = df["Reversed Name"]
empty_data = df["Empty"] #is a list of 5000 NaNs, not an empty list
duplicate_data = df["Duplicate"]

print(len(empty_data.tolist()))
print(len(empty_data))


current_data = unsorted_data 

def test_bubble_sort():
    assert Algorithms.BubbleSort(current_data.tolist()) == sorted(current_data.tolist())
    #i guess have the assert be True only if it works against all 5 datatypes, False if even one fails


#do these functions/tests need to be called?
    #if so, when?
    #if not, add current_data as an argument
    