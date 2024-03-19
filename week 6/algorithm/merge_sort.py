def merge_sort(list):
    """
    The given Python code implements the merge sort algorithm to sort a list of numbers in ascending
    order.
    
    Author - Liam Scott
    Last update - 03/19/2024
    @param list () - It looks like you have provided the code for a merge sort algorithm in Python. The
    `merge_sort` function recursively divides the input list into halves until each sublist has only one
    element, and then merges them back together in sorted order using the `merge` function.
    @returns The `merge_sort` function is returning a sorted list after recursively splitting and
    merging the input list. The `merge` function is used to merge two sorted lists into a single sorted
    list.
    
    """
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]
    

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if int(left[left_index]) < int(right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

