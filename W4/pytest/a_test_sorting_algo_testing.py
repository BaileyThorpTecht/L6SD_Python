from sorting_algo_testing import Algorithms 
import pandas as pd
import pytest as pt
import time

df = pd.read_excel(r"C:\Users\Bailey\Desktop\L6SD_Python\W3\rugby_players_data_extra.xlsx")
sorted_list = df["Sorted"].tolist()
unsorted_list = df["Unsorted"].tolist()
reversed_list = df["Reversed"].tolist()
empty_list = []
duplicate_list = df["Duplicate"].tolist()

def sort_and_get_time(Algo, lis):
    start_time = time.time()
    sorted_list = Algo(lis)
    end_time = time.time()
    duration = end_time - start_time
    print(f"{round(duration, 3)}")
    return sorted_list

# ------ Bubble Sort Tests ------
def test_bubblesort_sorted():
    print("\nBubble Sort:")
    assert sort_and_get_time(Algorithms.BubbleSort, sorted_list) == sorted_list
def test_bubblesort_unsorted():
    assert sort_and_get_time(Algorithms.BubbleSort, unsorted_list) == sorted_list
def test_bubblesort_reversed():
    assert sort_and_get_time(Algorithms.BubbleSort, reversed_list) == sorted_list
def test_bubblesort_empty():
    assert sort_and_get_time(Algorithms.BubbleSort, empty_list) == []
def test_bubblesort_duplicate():
    assert sort_and_get_time(Algorithms.BubbleSort, duplicate_list) == duplicate_list

# ------ Insertion Sort Tests ------
def test_insertionsort_sorted():
    print("\nInsertion Sort:")
    assert sort_and_get_time(Algorithms.InsertionSort, sorted_list) == sorted_list
def test_insertionsort_unsorted():
    assert sort_and_get_time(Algorithms.InsertionSort, unsorted_list) == sorted_list
def test_insertionsort_reversed():
    assert sort_and_get_time(Algorithms.InsertionSort, reversed_list) == sorted_list
def test_insertionsort_empty():
    assert sort_and_get_time(Algorithms.InsertionSort, empty_list) == []
def test_insertionsort_duplicate():
    assert sort_and_get_time(Algorithms.InsertionSort, duplicate_list) == duplicate_list
    
# ------ Selection Sort Tests ------
def test_selectionsort_sorted():
    print("\nSelection Sort:")
    assert sort_and_get_time(Algorithms.SelectionSort, sorted_list) == sorted_list
def test_selectionsort_unsorted():
    assert sort_and_get_time(Algorithms.SelectionSort, unsorted_list) == sorted_list
def test_selectionsort_reversed():
    assert sort_and_get_time(Algorithms.SelectionSort, reversed_list) == sorted_list
def test_selectionsort_empty():
    assert sort_and_get_time(Algorithms.SelectionSort, empty_list) == []
def test_selectionsort_duplicate():
    assert sort_and_get_time(Algorithms.SelectionSort, duplicate_list) == duplicate_list

# ------ Merge Sort Tests ------
def test_mergesort_sorted():
    print("\nMerge Sort:")
    assert sort_and_get_time(Algorithms.MergeSort, sorted_list) == sorted_list
def test_mergesort_unsorted():
    assert sort_and_get_time(Algorithms.MergeSort, unsorted_list) == sorted_list
def test_mergesort_reversed():
    assert sort_and_get_time(Algorithms.MergeSort, reversed_list) == sorted_list
def test_mergesort_empty():
    assert sort_and_get_time(Algorithms.MergeSort, empty_list) == []
def test_mergesort_duplicate():
    assert sort_and_get_time(Algorithms.MergeSort, duplicate_list) == duplicate_list
    
# ------ Quick Sort Tests ------
def test_quicksort_sorted():
    print("\nQuick Sort:")
    assert sort_and_get_time(Algorithms.QuickSort, sorted_list) == sorted_list
def test_quicksort_unsorted():
    assert sort_and_get_time(Algorithms.QuickSort, unsorted_list) == sorted_list
def test_quicksort_reversed():
    assert sort_and_get_time(Algorithms.QuickSort, reversed_list) == sorted_list
def test_quicksort_empty():
    assert sort_and_get_time(Algorithms.QuickSort, empty_list) == []
def test_quicksort_duplicate():
    assert sort_and_get_time(Algorithms.QuickSort, duplicate_list) == duplicate_list
