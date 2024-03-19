def quick_select(my_list, k):
    """
    The function `quick_select` implements the quickselect algorithm to find the kth smallest element in
    a list.
    
    Author - Liam Scott
    Last update - 03/17/2024
    @param my_list () - The `my_list` parameter in the `quick_select` function is a list of elements
    from which we want to find the k-th smallest element. The function uses the quickselect algorithm to
    efficiently find the k-th smallest element in the list.
    @param k () - The parameter `k` in the `quick_select` function represents the index of the element
    we want to find in the sorted list. It is zero-based, meaning that `k=0` corresponds to finding the
    smallest element, `k=1` corresponds to finding the second smallest element, and
    @returns the k-th smallest element in the input list `my_list`.
    
    """
    if my_list:
        pivot = my_list[len(my_list) // 2]
        smaller_list = [x for x in my_list if x < pivot]
        larger_list = [x for x in my_list if x > pivot]
        count = my_list.count(pivot)
        m = len(smaller_list)
        if k >= m and k < m + count:
            return int(pivot) 
        elif k < m:
            return quick_select(smaller_list, k)
        else:
            return quick_select(larger_list, k - m - count)

