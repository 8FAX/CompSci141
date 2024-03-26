from dataclasses import dataclass
import os

@dataclass
class Box:
    name: str
    size: int

@dataclass
class Item:
    name: str
    size: int


def file_data(file):
    """
    The function `file_data` reads data from a file, creates box and item objects, and stores them in
    lists.
    
    Author - Liam Scott
    Last update - 03/21/2024
    @param file () - The `file_data` function reads data from a file and processes it to create box and
    item objects. The `file` parameter is the file path of the file you want to read the data from.
    
    """
    print(f"Reading data from file '{file}'...\n")

    boxes = []
    items = []
    with open(file, 'r') as f:
        box_sizes = list(map(int, f.readline().strip().split()))
        for i, size in enumerate(box_sizes):
            boxes.append(Box(f'box{i + 1}', size))

        for line in f:
            item_data = line.strip().split()
            items.append(Item(item_data[0], int(item_data[1])))

    return boxes, items

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
    file_name = input("Please enter the name of the file you would like to use: ").strip()
    if check_file(file_name):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        if os.path.isfile(file_name):
            print(f"File '{file_name}' found.")
            return file_name
    else:
        print("Invalid file name. Please try again.")
        file_input()

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

def tightest_fit_packaging(boxes, items):
    """
    Pack items into boxes using the tightest fit algorithm.

    @param 'boxes' (list): A list of Box objects representing the available boxes and 'items' (list): A list of 
    Item objects representing the items to be packed.
    @returns: None

    Returns:
        None

    Prints the result of the packaging process, including the success or failure of the packing,
    the items that could not be packed, and the boxes with their packed items.
    Author - Liam Scott
    Last update - 03/21/2024

    """
    items = sorted(items, key=lambda x: x.size, reverse=False)
    boxes = sorted(boxes, key=lambda x: x.size, reverse=True) 
    packed_items = {box.name: [] for box in boxes}
    remaining_space = {box.name: box.size for box in boxes}
    unpacked_items = []

    for item in items:
        suitable_boxes = [(box_name, space) for box_name, space in remaining_space.items() if space >= item.size]
        suitable_boxes.sort(key=lambda x: x[1])

        if suitable_boxes:
            box_name = suitable_boxes[0][0]
            packed_items[box_name].append((item.name, item.size))
            remaining_space[box_name] -= item.size
        else:
            unpacked_items.append(item)

    if unpacked_items:
        print("Tightest Fit Packaging: \n FAILED\n")

        print("The following items could not be packed:")
        for item in unpacked_items:
            print(f"{item.name}, weight: {item.size}")
        print("\n" + "-" * 50 + "\n")
    else:
        print("Tightest Fit Packaging: \n SUCCESS\n")
        print("All items have been packed.")
        print("\n" + "-" * 50 + "\n")

    print("Boxes with their items:")
    for box_name, items in packed_items.items():
        remaining_space = boxes[int(box_name[-1]) - 1].size - sum(item[1] for item in items)
        print(f"{box_name} (size: {boxes[int(box_name[-1]) - 1].size}, remaining space: {remaining_space}): {', '.join([f'{item[0]} (weight: {item[1]})' for item in items])}")


def roomiest_fit_packaging(boxes, items):
    """
    Pack items into boxes using the roomiest fit algorithm.

    @param 'boxes' (list): A list of Box objects representing the available boxes and 'items' (list): A list of 
    Item objects representing the items to be packed.
    @returns: None

    Prints the result of the packaging process, including the success or failure of the packaging,
    the items that could not be packed, and the contents of each box.
    Author - Liam Scott
    Last update - 03/21/2024

    """
    items = sorted(items, key=lambda x: x.size, reverse=True)
    boxes = sorted(boxes, key=lambda x: x.size, reverse=True)
    packed_items = {box.name: [] for box in boxes}
    remaining_space = {box.name: box.size for box in boxes}
    unpacked_items = []

    for item in items:
        placed = False
        for box_name, space in remaining_space.items():
            if item.size <= space:
                packed_items[box_name].append((item.name, item.size))
                remaining_space[box_name] -= item.size
                placed = True
                break

        if not placed:
            unpacked_items.append(item)

    if unpacked_items:
        print("Roomiest Fit Packaging: \n FAILED\n")
        print("The following items could not be packed:")
        for item in unpacked_items:
            print(f"{item.name}, weight: {item.size}")
        print("\n" + "-" * 50 + "\n")
    else:
        print("Roomiest Fit Packaging: \n SUCCESS\n")
        print("All items have been packed.")
        print("\n" + "-" * 50 + "\n")

    print("Boxes with their items:")
    for box_name, items in packed_items.items():
        remaining_space = boxes[int(box_name[-1]) - 1].size - sum(item[1] for item in items)
        print(f"{box_name} (size: {boxes[int(box_name[-1]) - 1].size}, remaining space: {remaining_space}): {', '.join([f'{item[0]} (weight: {item[1]})' for item in items])}")


def one_box_at_a_time(boxes, items):
    """
    Packs items into boxes using the "One Box At a Time" strategy.

    @param 'boxes' (list): A list of Box objects representing the available boxes and 'items' (list): A list of 
    Item objects representing the items to be packed.
    @returns: None

    Prints the packing result and the boxes with their items.
    Author - Liam Scott
    Last update - 03/21/2024
    """
    items = sorted(items, key=lambda x: x.size, reverse=False)
    boxes = sorted(boxes, key=lambda x: x.size, reverse=True)

    packed_items = {box.name: [] for box in boxes}
    remaining_space = {box.name: box.size for box in boxes}

    for box in boxes:
        for item in items[:]:
            if remaining_space[box.name] >= item.size:
                packed_items[box.name].append((item.name, item.size))
                remaining_space[box.name] -= item.size
                items.remove(item)
    
    unpacked_items = items
    if unpacked_items:
        print("One Box At a Time: \n FAILED\n")
        print("The following items could not be packed:")
        for item in unpacked_items:
            print(f"{item.name}, weight: {item.size}")
        print("\n" + "-" * 50 + "\n")
    else:
        print("One Box At a Time: \n SUCCESS\n")
        print("All items have been packed.")
        print("\n" + "-" * 50 + "\n")

    print("Boxes with their items:")
    for box_name, items in packed_items.items():
        remaining_space = boxes[int(box_name[-1]) - 1].size - sum(item[1] for item in items)
        print(f"{box_name} (size: {boxes[int(box_name[-1]) - 1].size}, remaining space: {remaining_space}): {', '.join([f'{item[0]} (weight: {item[1]})' for item in items])}")


def main():
    """

    This is the main function that executes the program.
    It reads input from a file, displays the boxes and items,
    and performs various packaging algorithms.

    Author - Liam Scott
    Last update - 03/21/2024
    
    """
    file = file_input()
    boxes, items = file_data(file)
    print('-' * 50 + '\n')
    input(f"Boxes: {', '.join([f'{box.name} (size: {box.size})' for box in boxes])}\nItems: {', '.join([f'{item.name} (size: {item.size})' for item in items])}\n\nPress enter to continue...")
    print("\n" + "-" * 50 + "\n")
    tightest_fit_packaging(boxes, items)
    print("\n" + "-" * 50 + "\n")
    roomiest_fit_packaging(boxes, items)
    print("\n" + "-" * 50 + "\n")
    one_box_at_a_time(boxes, items)
    print("\n" + "-" * 50 + "\n")


# The `if __name__ == "__main__":` block in Python is used to check whether the current script is
# being run directly by the Python interpreter or if it is being imported as a module into another
# script.
if __name__ == "__main__":
    main()
