import turtle as t
import random

def draw_square():
    i = 0
    while i < 4:
        t.forward(100)
        t.right(90)
        i += 1
    
def draw_hexagon():
    i = 0
    while i < 6:
        t.forward(100)
        t.right(60)
        i += 1

def draw_circle(turns):
    if turns < 4:
        return 
    i = 0
    while i < turns:
        t.forward(1)
        t.right(360 / turns)
        i += 1

def is_anagram(s1, s2):
    dect1 = {}
    dect2 = {}
    for letters in s1:
        if letters in dect1:
            dect1[letters] += 1
        else:
            dect1[letters] = 1
    
    for letters in s2:
        if letters in dect2:
            dect2[letters] += 1
        else:
            dect2[letters] = 1
    
    return dect1 == dect2

def test_is_anagram():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    s1 = ''.join(random.choices(letters, k=10))
    s2 = ''.join(random.choices(letters, k=10))
    randoms1 = random.shuffle(s1)
    randoms2 = random.shuffle(s2)
    is_anagram(s1, s2)
    is_anagram(s1, randoms1)
    is_anagram(s2, randoms2)
    is_anagram(randoms1, randoms2)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def test_insertion_sort():
    worst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # O(n^2)
    best = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # O(n)
    randoms = random.choices(range(100), k=10)
    # O(n^2)
    insertion_sort(worst)
    insertion_sort(best)
    insertion_sort(randoms)

def binary_search(data, target, start, end):
    if start >= end:
        return -1
    mid_index = (start + end) // 2
    mid_value = data[mid_index]
    if target == mid_value:
        return mid_index
    elif target < mid_value:
        return binary_search(data, target, start, mid_index-1)
    else:
        return binary_search(data, target, start+1, end)
    # start wil always be less then end so this is a flawed implementation