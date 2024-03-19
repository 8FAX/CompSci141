def insertion_sort(list):
    """
    The function `insertion_sort` implements the insertion sort algorithm to sort a list of integers in
    ascending order.
    
    Author - Liam Scott
    Last update - 03/13/2024
    @param list () - The `insertion_sort` function you provided implements the insertion sort algorithm
    in Python. It takes a list of integers as input, sorts the list in ascending order, and returns the
    sorted list as a list of strings.
    @returns The `insertion_sort` function takes an array of integers, sorts it using the insertion sort
    algorithm, and then returns the sorted array as a list of strings.
    
    Preconditions: The input list `list` is a list of strings representing integers.
    postconditions: The function returns the sorted list of integers as a list of strings.

    """
    list = [int(x) for x in list]
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    list = [str(x) for x in list]
    return list


# made my own insertion sort function as i found the old one to be too bulky and hard to understand