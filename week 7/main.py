from dataclasses import dataclass
import os

boxes = []
items = []

@dataclass
class box:
    name : str
    size : int

@dataclass
class item:
    name : str
    size : int


    """
    The function `file_data` reads data from a file, creates box and item objects, and stores them in
    lists.
    
    Author - Liam Scott
    Last update - 03/21/2024
    @param file () - The `file_data` function reads data from a file and processes it to create box and
    item objects. The `file` parameter is the file path of the file you want to read the data from.
    
    """
def file_data(file):
    with open(file, 'r') as f:
        box_data = f.readline().strip().split(" ")
        n = 0 
        for i in box_data:
            n += 1
            boxes.append(box(f'box{n}', int(i)))

        for line in f:
            item_data = line.strip().split(" ")
            items.append(item(item_data[0], int(item_data[1])))

def file_input():
    """
    The function `file_input` prompts the user to enter a file name, checks if the file exists and has a
    .txt extension, and recursively asks for input until a valid file name is provided.
    
    Author - Liam Scott
    Last update - 03/21/2024
    @returns The `file_input()` function returns the name of the file that the user would like to use
    after checking its validity and ensuring that it ends with '.txt'. If the file name is valid, it
    returns the file name. If the file name is invalid, it prompts the user to enter a valid file name
    again by calling the `file_input()` function recursively.
    
    """
    file_name = input("Please enter the name of the file you would like to use: ")
    if check_file(file_name):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        return file_name
    else:
        print("Invalid file name. Please try again.")
        return file_input()

def check_file(file_name):
    """
    The function `check_file` checks if a given file exists and appends '.txt' extension if missing.
    
    Author - Liam Scott
    Last update - 03/21/2024
    @param file_name () - The `check_file` function takes a file name as input, checks if the file name
    ends with '.txt', and appends '.txt' if it doesn't. It then verifies if the file exists in the
    current directory.
    @returns The function `check_file` is returning a boolean value. It returns `True` if the file
    exists and has a `.txt` extension or if the extension is added to the file name, and it returns
    `False` if the file does not exist or if the extension is not `.txt`.
    
    """
    input_file = file_name.strip()
    if not input_file.endswith('.txt'):
        input_file += '.txt'
    if not os.path.isfile(input_file):
        return False
    else:
        return True
    
def simple_packaging(boxes, items):
    """
    The function `simple_packaging` iterates through a list of boxes and items, packing items into boxes
    based on size constraints.
    
    Author - Liam Scott
    Last update - 03/21/2024
    @param boxes () - Boxes is a list of objects representing different boxes available for packaging.
    Each box object has attributes such as name and size.
    @param items () - I see that you have defined a function `simple_packaging` that takes two
    parameters, `boxes` and `items`. The function seems to be iterating over each box and each item to
    check if the item can fit into the box based on their sizes.
    
    """
    packed_items = {box.name: [] for box in boxes}
    
    for box in boxes:
        for item in items:
            if item.size <= box.size:
                print(f"{item.name} fits in {box.name}")
                box.size -= item.size
                packed_items[box.name].append(item.name)
                items.remove(item)
        if not items:
            break
    print("Packing complete.")
    print("The following items could not be packed: ")
    for item in items:
        print(item.name)
    
    print("Boxes with their items:")
    for box_name, items in packed_items.items():
        print(f"{box_name}: {', '.join(items)}")

def main():
    """
    The main function reads file input, processes the data, sorts boxes and items by size, and then
    performs simple packaging.
    
    Author - Liam Scott
    Last update - 03/21/2024
    
    """
    file = file_input()
    print(file)
    file_data(file)
    boxes.sort(key=lambda x: x.size)
    items.sort(key=lambda x: x.size)
    print(boxes)
    print(items)
    simple_packaging(boxes, items)

# The `if __name__ == "__main__":` block in Python is used to check whether the current script is
# being run directly by the Python interpreter or if it is being imported as a module into another
# script.
if __name__ == "__main__":
    main()