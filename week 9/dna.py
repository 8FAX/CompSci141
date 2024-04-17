from node_types import FrozenNode
import immutable_extra as ie



def convert_to_nodes(s):
    """
    The function `convert_to_nodes` recursively converts a string into a linked list of nodes.
    
    Author - Liam Scott
    Last update - 04/16/2024
    @param s () - It looks like the function `convert_to_nodes` takes a string `s` as input and
    recursively converts it into a linked list of nodes. Each node contains a character from the string
    `s`. The function returns the head of the linked list.
    @returns The function `convert_to_nodes` is returning a linked list of nodes created from the
    characters in the input string `s`. Each node contains a character from the string, and the nodes
    are linked together in the order they appear in the string. The function recursively creates nodes
    for each character in the string until the string is empty.
    
    """
    if len(s) == 0:
        return None
    else:
        return FrozenNode(s[0], convert_to_nodes(s[1:]))

def is_match(list1, list2):
    """
    The function `is_match` compares two linked lists for equality by recursively checking if their
    values match.
    
    Author - Liam Scott
    Last update - 04/16/2024
    @param list1 () - The function `is_match` is designed to compare two linked lists for equality. The
    function recursively checks if the values of corresponding nodes in the two lists are equal.
    @param list2 () - It seems like you have provided the code snippet for a function `is_match` that
    compares two linked lists for equality. However, you have not provided the definition or content of
    `list2`. In order to assist you further, could you please provide the definition or content of
    `list2` that
    @returns The function is checking if two linked lists are a match by comparing their values. If both
    lists are empty (None), it returns True. If one list is empty and the other is not, it returns
    False. If the values of the current nodes in both lists are the same, it recursively calls the
    function on the next nodes. If any values are different, it returns False.
    
    """
    if list1 == None and list2 == None:
        return True
    elif list1 == None or list2 == None:
        return False
    elif list1.value == list2.value:
        return is_match(list1.next, list2.next)
    else:
        return False
    
def insert_seq(lst1, lst2, index):
    """
    The function `insert_seq` inserts the elements of one list into another list at a specified index.
    
    Author - Liam Scott
    Last update - 04/16/2024
    @param lst1 () - It seems like the code snippet you provided is incomplete. Could you please provide
    more information about the `lst1` parameter so that I can assist you better?
    @param lst2 () - It seems like you were about to provide some information about the `lst2`
    parameter, but the message got cut off. Could you please provide more details or let me know how I
    can assist you further with the `lst2` parameter?
    @param index () - The `index` parameter in the `insert_seq` function represents the position at
    which the elements from `lst2` should be inserted into `lst1`. It indicates the index in `lst1`
    where the insertion should occur.
    @returns a call to the `FrozenNode` constructor with the value of the first element in `lst1` and
    the result of recursively calling `insert_seq` on the rest of `lst1`, `lst2`, and `index-1`.
    
    """
    if index == 0:
        return ie.concatenate(lst2, lst1)
    elif lst1 == None:
        raise IndexError("invalid insertion index")
    else:
        return FrozenNode(lst1.value, insert_seq(lst1.next, lst2, index-1))
    

def convert_to_string(head):
    """
    The function `convert_to_string` takes a linked list as input and returns a string by concatenating
    the values of each node in the linked list.
    
    Author - Liam Scott
    Last update - 04/16/2024
    @param head () - It looks like you are trying to define a function `convert_to_string` that takes a
    linked list as input and converts it into a string. However, you have not provided the full
    implementation of the linked list structure or the Node class.
    @returns The function `convert_to_string` is returning a concatenated string of all the values in
    the linked list starting from the `head` node.
    
    """
    str = ""
    while head is not None:
        str += head.value
        head = head.next
    return str
    

def str_to_linked_list(s):
    """
    The function `str_to_linked_list` takes a string as input and creates a linked list where each
    character in the string becomes a node in reverse order.
    
    Author - Liam Scott
    Last update - 04/16/2024
    @param s () - The function `str_to_linked_list` takes a string `s` as input and converts it into a
    linked list where each character in the string becomes a node in the linked list. The nodes are
    created in reverse order, meaning the last character of the string becomes the first node in the
    linked list
    @returns A linked list is being returned, where each character in the input string `s` is
    represented as a node in the linked list. The nodes are connected in reverse order of appearance in
    the input string.
    
    """
    head = None
    for char in s[::-1]:
        head = FrozenNode(char, head)
    return head

def length_rec(head):
    """
    The function `length_rec` recursively calculates the length of a linked list starting from the given
    head node.
    
    Author - Liam Scott
    Last update - 04/16/2024
    @param head () - The `head` parameter in the `length_rec` function is likely referring to the head
    node of a linked list. The function is a recursive function that calculates the length of the linked
    list starting from the given head node.
    @returns The function `length_rec` is a recursive function that calculates the length of a linked
    list. It returns the length of the linked list starting from the given `head` node.
    
    """
    if head is None:
        return 0
    else:
        return 1 + length_rec(head.next)

def is_pairing(lst1,lst2):
    """
    The function `is_pairing` compares two linked lists for complementary base pairs 'A' and 'T', 'C'
    and 'G', and returns True if they match.
    
    Author - Liam Scott
    Last update - 04/16/2024
    @param lst1 () - It seems like you have provided the beginning of a function `is_pairing` that
    checks if two lists are pairing elements. However, you have not provided the complete code for the
    function, and you have left a comment at the end of the code snippet.
    @param lst2 () - It seems like you have provided the code snippet for a function that checks if two
    lists are pairing based on certain conditions. However, the code snippet you provided is incomplete
    as it references a function `length_rec(lst1)` which is not defined in the snippet.
    @returns The function is checking if the elements in two linked lists `lst1` and `lst2` are pairing
    nucleotides ('A' with 'T' and 'C' with 'G'). If the elements in the lists are pairing nucleotides,
    the function recursively calls itself with the next elements in the lists. If the elements are not
    pairing nucleotides or the lengths of the lists
    
    """
    if lst1 == None and lst2 == None:
        return True
    if length_rec(lst1) != length_rec(lst2):
        return False
    if lst1.value == 'A' and lst2.value == 'T':
        return is_pairing(lst1.next, lst2.next)
    if lst1.value == 'T' and lst2.value == 'A':
        return is_pairing(lst1.next, lst2.next)
    if lst1.value == 'C' and lst2.value == 'G':
        return is_pairing(lst1.next, lst2.next)
    if lst1.value == 'G' and lst2.value == 'C':
        return is_pairing(lst1.next, lst2.next)
    else:
        return False
    
def substitute(lst, index, char):
    """
    The function `substitute` replaces a character at a specific index in a linked list with a new
    character.
    
    Author - Liam Scott
    Last update - 04/16/2024
    @param lst () - It seems like the `substitute` function is designed to replace a character in a
    linked list at a specific index with a new character. However, the implementation is incomplete as
    it references a `FrozenNode` class which is not defined in the provided code snippet.
    @param index () - The `index` parameter in the `substitute` function represents the position in the
    list where you want to substitute a character with a new character. It is used to specify the
    location within the list where the substitution operation should take place.
    @param char () - The `char` parameter in the `substitute` function represents the character that
    will replace the value at the specified index in the linked list.
    @returns The `substitute` function is returning a new linked list where the character at the
    specified index in the original list `lst` is replaced with the character `char`. The function
    recursively traverses the original list until it reaches the specified index, at which point it
    creates a new `FrozenNode` with the character `char` at that index and links it to the rest of the
    original list.
    
    """
    if lst == None:
        raise IndexError("index out of range")
    else:
        if index == 0:
            return FrozenNode(char, lst.next)
        else:
            return FrozenNode(lst.value, substitute(lst.next, index-1, char))
        
def delete_seq(lst, start, length):
    """
    The function `delete_seq` recursively removes a sequence of elements from a list starting at a
    specified index.
    
    Author - Liam Scott
    Last update - 04/16/2024
    @param lst () - A list from which a sequence of elements will be deleted.
    @param start () - The `start` parameter in the `delete_seq` function represents the index position
    in the list (`lst`) where the deletion of elements should begin.
    @param length () - The `length` parameter in the `delete_seq` function represents the number of
    elements to be deleted from the list `lst` starting from the index `start`. It determines how many
    elements will be removed in each recursive call until the specified length is reached.
    @returns The function `delete_seq` is recursively removing a sequence of elements from a list `lst`
    starting at index `start` and of length `length`. The function is returning the modified list after
    removing the specified sequence.
    
    """
    if lst is None:
        if start == 0 and length == 0:
            return None
        else:
            raise IndexError("index out of range")
    else:
        if length == 0:
            return lst
        else:
            lst = ie.remove_at(start, lst)
            return delete_seq(lst, start, length-1)
        
def duplicate_seq(lst, index, size):
    """
    The function `duplicate_seq` takes a linked list `lst`, an index, and a size, and duplicates a
    sequence of nodes starting from the specified index with the specified size.
    
    Author - Liam Scott
    Last update - 04/16/2024
    @param lst () - The `lst` parameter in the `duplicate_seq` function seems to represent a linked list
    node. Each node has a `value` attribute and a `next` attribute pointing to the next node in the
    linked list.
    @param index () - The `index` parameter in the `duplicate_seq` function represents the starting
    index from which the duplication of elements in the list will begin. It indicates the position in
    the list where the duplication process should start.
    @param size () - The `size` parameter in the `duplicate_seq` function represents the number of
    elements to duplicate in the sequence starting from the specified `index`. It determines how many
    elements will be duplicated in the sequence.
    @returns The function `duplicate_seq` is returning a modified sequence based on the input parameters
    `lst`, `index`, and `size`. The specific return value will depend on the conditions met within the
    function.
    
    """
    if lst is None:
        if index == 0 and size == 0:
            return None
        else:
            raise IndexError("index out of range")

    if lst.next is None and size > 2 or lst.next is None and size == 0:
        if index == 0 and size > 2:
            raise IndexError("index out of range")
        if  size == 0:
            return FrozenNode(lst.value, None)
        else:
            return FrozenNode(lst.value, duplicate_seq(lst.next, index-1, size-1))
    if size == 0:
        return lst
    if index == 0:
        lst2 = dupe_helper(lst, size)
        new = insert_seq(lst ,lst2, 0)
        return new
    else:
        return FrozenNode(lst.value, duplicate_seq(lst.next, index-1, size))


def dupe_helper(lst, size):
    """
    The function `dupe_helper` duplicates a linked list up to a specified size.
    
    Author - Liam Scott
    Last update - 04/16/2024
    @param lst () - It seems like you were about to provide some information about the `lst` parameter,
    but it got cut off. Could you please provide more details or context about the `lst` parameter so
    that I can assist you further with the `dupe_helper` function?
    @param size () - The `size` parameter in the `dupe_helper` function represents the number of
    elements you want to duplicate from the input list `lst`. It determines how many elements will be
    duplicated in the new list that is being created recursively.
    @returns The function `dupe_helper` is recursively duplicating the elements of a linked list `lst`
    up to a specified `size`. It returns a new linked list with duplicated elements up to the specified
    size.
    
    """
    if size == 0:
        return None
    if lst.next is None and size > 1:
        raise IndexError("index out of range")
    else:
        return FrozenNode(lst.value, dupe_helper(lst.next, size-1))
