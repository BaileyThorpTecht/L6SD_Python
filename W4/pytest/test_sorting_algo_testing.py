from sorting_algo_testing import Algorithms 
import pandas as pd
import pytest as pt
import openpyxl
import time

df = pd.read_excel(r"C:\Users\Bailey\Desktop\L6SD_Python\W3\rugby_players_data_extra.xlsx")
sorted_data = df["Sorted"]
unsorted_data = df["Unsorted"]
reversed_data = df["Reversed"]
empty_df = pd.DataFrame()
empty_df["empty"] = []
empty_data = empty_df["empty"]
duplicate_data = df["Duplicate"]
all_data = [sorted_data, unsorted_data, reversed_data, empty_data, duplicate_data]

def Sort_And_Time(Algo, data):
    start_time = time.time()
    sorted_list = Algo(data.tolist())
    end_time = time.time()
    duration = end_time - start_time
    print(f"{data.name}: {round(duration, 3)}")
    return sorted_list

def test_bubble_sort():
    print("------ Bubble Sort: ------")
    success = True
    for data_type in all_data:
        if success:
            algo_sorted_list = Sort_And_Time(Algorithms.BubbleSort, data_type)

            if not algo_sorted_list == sorted(data_type.tolist()):
                success = False
    assert success

