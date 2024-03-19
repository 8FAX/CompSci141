import os




def file(my_list, file_name):
    """
    This function reads the contents of a file line by line, splits each line by spaces, and appends the
    second element of each line to a given list.
    
    Author - Liam Scott
    Last update - 03/13/2024
    @param my_list () - The `file` function you provided reads from a file named "input.txt" and appends
    the second element of each line (split by space) into the `my_list` parameter.
    @returns the updated `my_list` after extracting the second element from each line in the "input.txt"
    file and adding it to the list.

    Preconditions: The input file `input.txt` contains a list of store locations. in this format " "name" "number" "
    
    """
    if file_name == "":
        file = open("input.txt")
    else:
        file = open(file_name)

    for line in file:
        svalues = line.strip("\n")
        values = svalues.split(" ")
        my_list += [values[1]]
    return my_list

def distance(my_list, best):
    """
    The function calculates the total distance between each element in a list and a specified value.
    
    Author - Liam Scott
    Last update - 03/13/2024
    @param my_list () - A list of numbers.
    @param best () - The `best` parameter in the `distance` function represents the reference value to
    which the absolute difference is calculated for each element in the `my_list`.
    @returns The function `distance` calculates the total distance between each element in `my_list` and
    the `best` value. It returns the sum of the absolute differences between each element in `my_list`
    and the `best` value.

    Preconditions: The input list `my_list` is a list of strings representing integers.
    
    """
    i = 0
    for n in my_list:
        i += abs(float(n) - float(best))
    return i

def check_file(file_name):
    input_file = file_name.strip()
    if not input_file.endswith('.txt'):
        input_file += '.txt'

    if not os.path.isfile(input_file):
        print(f"No file was found under the name {input_file}")
        return False
    else:
        return True



