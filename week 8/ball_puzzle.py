from rit_stack import *
from ball_puzzle_animate import *

def sort_balls(R, G, B):
    """
    The function `sort_balls` sorts balls of different colors (red, green, blue) by moving them between
    stacks while keeping track of the number of steps taken.
    
    Author - Liam Scott
    Last update - 03/28/2024
    @param R () - The `sort_balls` function you provided seems to be sorting balls of different colors
    (red, green, blue) using stacks. The function moves the balls according to certain rules until they
    are sorted in the order of red, green, blue.
    @param G () - The code you provided seems to be a function for sorting balls of different colors
    (red, green, blue) using stacks. It looks like you are trying to move the balls in a specific order
    based on their colors.
    @param B () - The code you provided seems to be a function that sorts balls of different colors
    (red, green, blue) based on certain rules. The function takes three stacks representing the balls of
    each color (R for red, G for green, B for blue) as input and sorts them according to the following
    @returns The function `sort_balls` returns the total number of steps taken to sort the balls in the
    stacks R, G, and B according to the specified rules.
    
    """

    steps = 0
    while not empty_stack(R):
        ball = top(R)
        pop(R)
        if ball == 'B':
            push(B, ball)
            animate_move([R, G, B] , 0, 2) 
        else:
            push(G, ball)
            animate_move([R, G, B] , 0, 1)
        steps += 1

    while not empty_stack(G):
        ball = top(G)
        pop(G)

        if ball == 'R':
            push(R, ball)
            animate_move([R, G, B] , 1, 0)
        else:
            push(B, ball)
            animate_move([R, G, B] , 1, 2)
        steps += 1

    while not empty_stack(B) and top(B) != 'B':
        ball = top(B)
        pop(B)
        push(G, ball)
        animate_move([R, G, B] , 2, 1)
        steps += 1
    return steps

def main():
    """
    The main function initializes three stacks, reads a sequence of balls, pushes them onto the red
    stack, sorts the balls into three stacks, and prints the number of steps taken.
    
    Author - Liam Scott
    Last update - 03/28/2024
    @returns The `main()` function does not explicitly return any value. It prints out messages and
    waits for user input before exiting.
    
    """

    R = mk_empty_stack()
    G = mk_empty_stack()
    B = mk_empty_stack()

    input_string = input("Enter the sequence of balls: ")
    if len(input_string) > 50:
        print("Puzzle graphics only handle up to 50 balls.")
        return
    animate_init(input_string)
    for i in input_string:
        push(R, i)
    print(f"All balls are in the red stack! \n Stack size: {size(R)} \n Stack top: {top(R)}")

    steps = sort_balls(R, G, B)
    print(f"Number of steps: {steps}")
    input("Press enter to exit...")



# The `if __name__ == '__main__':` block in Python is a common idiom used to ensure that the code
# inside it is only executed if the script is run directly, and not imported as a module into another
# script.
if __name__ == '__main__':
    main()
    