# The `import turtle` statement is importing the turtle module, which provides a way to create
# graphics and drawings using turtle graphics. The `import random` statement is importing the random
# module, which provides functions for generating random numbers and making random choices.
import turtle
import random

def side():
    """
    The function `side()` moves the turtle forward by 100 units and then turns it left by 90 degrees.
    
    Author - 8FA
    Last update - 01/19/2024
    
    """
    turtle.forward(100)
    turtle.left(90)

def fill():
    """
    The function `fill()` sets the fill color of a turtle object to orange and begins filling a shape.
    
    Author - 8FA
    Last update - 01/19/2024
    
    """
    turtle.fillcolor("orange") 
    turtle.begin_fill()
    # color = turtle.fillcolor()
    # print("set Color " + color)

def reset():
    """
    The function "reset" resets the turtle's pen size to 1 and lifts the pen up.
    
    Author - 8FA
    Last update - 01/19/2024
    
    """
    turtle.pensize(1)
    turtle.up()

def big_pen():
    """
    The function sets the pen size to 12 and puts the pen down.
    
    Author - 8FA
    Last update - 01/19/2024
    
    """
    turtle.pensize(12)
    turtle.down()


def end_fill():
    """
    The function `end_fill()` is used to end the filling of a shape in turtle graphics.
    
    Author - 8FA
    Last update - 01/19/2024
    
    """
    turtle.end_fill()

def T_sign():
    """
    The function draws a T-shaped sign using the turtle module in Python.
    
    Author - 8FA
    Last update - 01/19/2024
    
    """
    turtle.left(90)
    turtle.forward(25)
    big_pen()
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(25)
    turtle.backward(50)
    turtle.forward(25)
    reset()
    turtle.right(90)
    turtle.pensize(1)
    turtle.backward(100)
    turtle.right(90)
    

def x_sign():
    """
    The function draws an "X" shape using the turtle module in Python.
    
    Author - 8FA
    Last update - 01/19/2024
    
    """
    turtle.left(45)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(15)
    big_pen()
    turtle.forward(70)
    turtle.backward(35)
    turtle.right(90)
    turtle.forward(35)
    turtle.backward(70)
    reset()
    turtle.backward(15)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(45)

 
def t_sign():
    """
    The function draws a T-shaped sign using the turtle module in Python.
    
    Author - 8FA
    Last update - 01/19/2024
    
    """
    turtle.left(90)
    turtle.forward(30)
    big_pen()
    turtle.forward(75)
    turtle.backward(35)
    turtle.right(90)
    turtle.forward(35)
    turtle.backward(75)
    reset()
    turtle.backward(30)
    turtle.right(45)
    turtle.forward(100)
    turtle.left(45)
   
def o_sign():
    """
    The function draws the letter "O" using the turtle module in Python.
    
    Author - 8FA
    Last update - 01/19/2024
    
    """
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    big_pen()
    turtle.circle(30)
    turtle.right(90)
    turtle.forward(15)
    turtle.up()
    turtle.backward(75)
    turtle.down()
    turtle.backward(15)
    turtle.up()
    turtle.forward(45)
    turtle.dot()
    turtle.left(90)
    turtle.forward(30)
    turtle.down()
    turtle.forward(15)
    turtle.up()
    turtle.backward(90)
    turtle.down()
    turtle.forward(15)
    reset()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)  


def sign():
    """
    The function draws a sign using the turtle module in Python.
    
    Author - 8FA
    Last update - 01/19/2024
    
    """
    fill()
    turtle.left(45)
    turtle.down()
    side()
    side()
    side()
    side()
    turtle.up()
    turtle.right(45)
    end_fill()
    
def start_up(sign_count):
    """
    The function sets up the turtle graphics window with a specific width and height based on the number
    of signs.
    
    Author - 8FA
    Last update - 01/19/2024
    @param sign_count () - The parameter "sign_count" represents the number of signs that will be
    displayed in the program.
    
    """
    turtle.speed(20)
    turtle.left(180)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.speed(5)
    window_width = 400 + 150 * int(sign_count)
    window_height = 450
    turtle.setup(width=window_width, height=window_height)
    turtle.setworldcoordinates(-100, 0, 550, 250)
    print("setup complete!")

def random_sign():
    """
    The function `random_sign` randomly selects and executes one of four sign functions.
    
    Author - 8FA
    Last update - 01/19/2024
    
    """
    sign_functions = [T_sign, x_sign, t_sign, o_sign]
    random.choice(sign_functions)()
    
def main():
    """
    The main function creates a specified number of signs using turtle graphics, with the option to
    create a random design if the number of signs is more than 4.
    
    Author - 8FA
    Last update - 01/19/2024
    
    """
    sign_count = input("How many Signs do you want to make? (anything more then 4 will be a random design!) ")
    start_up(sign_count)
    n = 0 
    while(n < float(sign_count)):
        sign()
        if n == 0:
            T_sign()
        if n == 1:
            x_sign()
        if n == 2:
            t_sign()
        if n == 3:
            o_sign()
        if n > 3:
            random_sign()

        turtle.forward(150)
        n += 1
        print("Done with sign: " + str(n))
    print("Done with all signs!")    
    turtle.done()

# The `main()` function is the entry point of the program. It prompts the user to input the number of
# signs they want to create. It then calls the `start_up()` function to set up the turtle graphics
# window based on the number of signs.
main()

