def quicksort(my_list):
    """
    The function `quicksort` implements the quicksort algorithm to sort a list of integers.
    
    Author - Liam Scott
    Last update - 03/19/2024
    @param my_list () - The `quicksort` function you provided is an implementation of the quicksort
    algorithm in Python. It takes a list `my_list` as input and recursively sorts it in ascending order.
    @returns The function `quicksort` is returning a sorted version of the input list `my_list`. It uses
    the quicksort algorithm to sort the elements in ascending order and returns the sorted list.
    
    """
    if len(my_list) <= 1:
        return my_list
    pivot = int(my_list[len(my_list) // 2])  
    left = [int(x) for x in my_list if int(x) < pivot] 
    middle = [int(x) for x in my_list if int(x) == pivot]  
    right = [int(x) for x in my_list if int(x) > pivot]  
    return quicksort(left) + middle + quicksort(right)