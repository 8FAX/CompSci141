from util.tools import file, distance, check_file
from algorithm.slect_median import quick_select
from algorithm.quick_sort import quicksort
from algorithm.insertion_sort import insertion_sort
from algorithm.bubble_sort import bubble_sort
from algorithm.heap_sort import heap_sort
from algorithm.merge_sort import merge_sort
from algorithm.selection_sort import selection_sort

import time
import os

def optimal_location(store_locations):
    """
    This Python function calculates the optimal location for a new store based on a list of existing
    store locations.
    
    Author - Liam Scott
    Last update - 03/13/2024
    @param store_locations () - The `optimal_location` function takes a list of store locations as input
    and calculates the optimal location for a new store based on the median of the existing store
    locations.
    @returns The function `optimal_location` returns the optimal location for a new store based on the
    input list of store locations. If the number of store locations is even, it calculates the average
    of the two middle locations. If the number of store locations is odd, it returns the middle
    location.

    Preconditions: The input list of store locations is a sorted list of strings representing integers.
    postconditions: The function returns the optimal location for a new store based on the median of the input list of store locations as a String.
    
    """
    store_locations = [int(x) for x in store_locations]
    n = len(store_locations)
    if n % 2 == 0:
        mid1 = store_locations[n//2]
        mid2 = store_locations[n//2 - 1]
        optimal_location = (mid1 + mid2) / 2
    else:
        optimal_location = store_locations[n//2]
    return str(optimal_location)


    


def main():
    """
    The main function in the code snippet initializes a blank list, reads data from a file into a list,
    sorts the list using insertion sort, finds the optimal location in the sorted list, and calculates
    the distance between the original list and the optimal location.
    
    Author - Liam Scott
    Last update - 03/13/2024
    
    Preconditions: The input file `input.txt` contains a list of store locations.
    Preconditions: The input file must be run itself, if a function is called from the file, it will not run.
    
    """
    input_file = input("Please enter the name of the file you would like to use: ")
    if check_file(input_file) == False:
        main()
    else:
        file_name = input_file.strip()
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        s_type = input("Please enter the type of sort you would like to use: ")
        blank_list = []
        my_list = file(blank_list, file_name)

        if s_type.lower() == "insertion":
            start_time = time.time()
            sorted_list = insertion_sort(my_list)
            end_time = time.time()
            pick_start_time = time.time()
            best = optimal_location(sorted_list)
            tot_dis = distance(my_list, best)
            print(f"The optimal location for a new store is {best}")
            print(f"The total distance between optimal location and all other locations and the is {tot_dis}")
            pick_end_time = time.time()
            print(f"Total time to Sort the list is {end_time - start_time} seconds")
            print(f"Total time to find the best location {pick_end_time - pick_start_time} seconds")

        elif s_type.lower() == "quick_sort":
            start_time = time.time()
            sorted_list = quicksort(my_list)
            end_time = time.time()
            pick_start_time = time.time()
            best = optimal_location(sorted_list)
            tot_dis = distance(my_list, best)
            print(f"The optimal location for a new store is {best}")
            print(f"The total distance between optimal location and all other locations and the is {tot_dis}")
            pick_end_time = time.time()
            print(f"Total time to Sort the list is {end_time - start_time} seconds")
            print(f"Total time to find the best location {pick_end_time - pick_start_time} seconds")

        elif s_type.lower() == "quick_select":
            pick_start_time = time.time()
            low = 0
            high = len(my_list) - 1
            low_out = int(quick_select(my_list, low)) 
            high_out = int(quick_select(my_list, high))
            med = low_out + high_out // 2
            end_time = time.time()
            pick_end_time = time.time()
            tot_dis = distance(my_list, med)
            print(f"The optimal location for a new store is {med}")
            print(f"The total distance between optimal location and all other locations and the is {tot_dis}")
            print(f"Total time to find the best location {pick_end_time - pick_start_time} seconds")

        elif s_type.lower() == "bubble":
            start_time = time.time()
            sorted_list = bubble_sort(my_list)
            end_time = time.time()
            pick_start_time = time.time()
            best = optimal_location(sorted_list)
            tot_dis = distance(my_list, best)
            print(f"The optimal location for a new store is {best}")
            print(f"The total distance between optimal location and all other locations and the is {tot_dis}")
            pick_end_time = time.time()
            print(f"Total time to Sort the list is {end_time - start_time} seconds")
            print(f"Total time to find the best location {pick_end_time - pick_start_time} seconds")
        
        elif s_type.lower() == "heap":
            start_time = time.time()
            sorted_list = heap_sort(my_list)
            end_time = time.time()
            pick_start_time = time.time()
            best = optimal_location(sorted_list)
            tot_dis = distance(my_list, best)
            print(f"The optimal location for a new store is {best}")
            print(f"The total distance between optimal location and all other locations and the is {tot_dis}")
            pick_end_time = time.time()
            print(f"Total time to Sort the list is {end_time - start_time} seconds")
            print(f"Total time to find the best location {pick_end_time - pick_start_time} seconds")

        elif s_type.lower() == "merge":
            start_time = time.time()
            sorted_list = merge_sort(my_list)
            end_time = time.time()
            pick_start_time = time.time()
            best = optimal_location(sorted_list)
            tot_dis = distance(my_list, best)
            print(f"The optimal location for a new store is {best}")
            print(f"The total distance between optimal location and all other locations and the is {tot_dis}")
            pick_end_time = time.time()
            print(f"Total time to Sort the list is {end_time - start_time} seconds")
            print(f"Total time to find the best location {pick_end_time - pick_start_time} seconds")
        
        elif s_type.lower() == "selection":
            start_time = time.time()
            sorted_list = selection_sort(my_list)
            end_time = time.time()
            pick_start_time = time.time()
            best = optimal_location(sorted_list)
            tot_dis = distance(my_list, best)
            print(f"The optimal location for a new store is {best}")
            print(f"The total distance between optimal location and all other locations and the is {tot_dis}")
            pick_end_time = time.time()
            print(f"Total time to Sort the list is {end_time - start_time} seconds")
            print(f"Total time to find the best location {pick_end_time - pick_start_time} seconds")

        else:
            print("Please enter a valid sort type (insertion, quick_select, quick_sort, bubble, heap, merge_sort, selection_sort")
                 # WANT TO ADD (but ran out of time):  shell_sort, Radix Sort, Counting Sort, Bucket Sort, or Timsort 
            main()


if __name__ == "__main__":
    main()