def selection_sort(list):
    """
    The `selection_sort` function implements the selection sort algorithm to sort a list of numbers in
    ascending order.
    
    Author - Liam Scott
    Last update - 03/19/2024
    @param list () - The `selection_sort` function you provided implements the Selection Sort algorithm
    to sort a list of elements in ascending order. The function iterates through the list and selects
    the minimum element in each iteration, swapping it with the element at the current position.
    @returns The selection_sort function is returning the input list after sorting it in ascending order
    using the selection sort algorithm.
    
    """
    n = len(list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if int(list[j]) < int(list[min_index]):
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

