from rit_stack import *
from ball_puzzle_animate import *

def sort_balls(R, G, B):
    """
    The function `sort_balls` takes three stacks representing red, green, and blue balls, and sorts the
    balls in the stacks according to a specific order, returning the number of steps taken to sort them.
    
    Author - Liam Scott
    Last update - 03/28/2024
    @param R () - The `R` parameter in the `sort_balls` function likely represents a stack of red balls.
    The function seems to be sorting the balls based on their color (red, green, blue) by moving them
    between different stacks (`R`, `G`, `B`) until they are sorted in
    @param G () - The code you provided seems to be a sorting algorithm for balls of different colors
    (red, green, and blue). The function `sort_balls` takes three stacks representing balls of red (R),
    green (G), and blue (B) colors, and it sorts them according to a specific order
    @param B () - The code you provided seems to be a function that sorts balls of different colors
    (red, green, and blue) based on certain conditions. It looks like the function is using stacks to
    move the balls around until they are sorted in a specific order.
    @returns The function `sort_balls` returns the total number of steps taken to sort the balls in the
    stacks R, G, and B according to the specified rules.
    
    """
    steps = 0
    while not empty_stack(R):
        ball = pop(R)
        if ball == 'B':
            push(B, ball)
        else:
            push(G, ball)
        steps += 1

    while not empty_stack(G):
        ball = pop(G)
        if ball == 'R':
            push(R, ball)
        else:
            push(B, ball)
        steps += 1

    while not empty_stack(B) and top(B) != 'B':
        ball = pop(B)
        push(G, ball)
        steps += 1
    return steps

def main():
    """
    The main function initializes three stacks, reads a sequence of balls, pushes them onto the red
    stack, sorts the balls into three stacks, and prints the number of steps taken.
    
    Author - Liam Scott
    Last update - 03/28/2024
    @returns The `main()` function does not explicitly return any value. It simply prints out some
    information and waits for user input before exiting.
    
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
    