from sorting_algo_testing import Algorithms 
import pandas as pd
import pytest as pt
import time

df = pd.read_excel(r"C:\Users\Bailey\Desktop\L6SD_Python\Assessment1\BirthWeight.xlsx")
sorted_list = df["SortedBirthWeight"].tolist()
unsorted_list = df["BirthWeight"].tolist()
reversed_list = df["ReversedBirthWeight"].tolist()
empty_list = []
duplicate_list = df["DuplicateBirthWeight"].tolist()

def sort_and_get_time(Algo, lis):
    start_time = time.time() #gets the start time
    sorted_list = Algo(lis) #sorts the given list using the given algorithm
    end_time = time.time() #then gets the end time
    duration = end_time - start_time
    print(round(duration, 3)) #prints the duration to 3 dp
    return sorted_list #returns the sorted list for the pytest

# ------ Bubble Sort Tests ------
def test_bubblesort_sorted():
    print("\nBubble Sort:")
    #for every test, I use the sort_and_get_time() function to sort the list with the given algorithm
    #it also gets the time complexity for the sorting
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
