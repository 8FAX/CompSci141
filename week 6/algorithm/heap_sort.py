def heapify(list, n, i):
    """
    The code defines a heapify function and a heap_sort function in Python to sort a list using the heap
    sort algorithm.
    
    Author - Liam Scott
    Last update - 03/19/2024
    @param list () - The `list` parameter in the `heapify` and `heap_sort` functions represents the list
    of elements that you want to sort using the heap sort algorithm. The elements in the list are
    compared and rearranged to create a max heap structure during the heapify process, and then the list
    is
    @param n () - In the context of the provided code snippet, the parameter `n` represents the size of
    the heap or the number of elements in the list that is being operated on. It is used in the
    `heapify` function and `heap_sort` function to determine the boundaries and iterate over the
    elements in
    @param i () - In the `heapify` function, the parameter `i` represents the index of the current node
    in the heap that needs to be heapified. It is used to compare the node with its left and right
    children to maintain the heap property.
    
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list[left] > list[largest]:
        largest = left

    if right < n and list[right] > list[largest]:
        largest = right

    if largest != i:
        list[i], list[largest] = list[largest], list[i]  
        heapify(list, n, largest)

def heap_sort(list):
    n = len(list)

    list = [int(x) for x in list]

    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]  
        heapify(list, i, 0)

    list = [str(x) for x in list]
    return list
