def bubble_sort(list):
    """
    The `bubble_sort` function implements the bubble sort algorithm to sort a list in ascending order.
    
    Author - Liam Scott
    Last update - 03/19/2024
    @param list () - The `bubble_sort` function you provided implements the bubble sort algorithm to
    sort a list of elements in ascending order.
    @returns The `bubble_sort` function is returning the sorted list in ascending order after performing
    the bubble sort algorithm on the input list.
    
    """
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
