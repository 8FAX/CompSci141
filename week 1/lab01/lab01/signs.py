import turtle

def side():
    """
    The function `side()` moves the turtle forward by 100 units and then turns it left by 90 degrees.
    """
    turtle.forward(100)
    turtle.left(90)

def fill():
    """
    The function `fill()` sets the fill color to orange and begins filling a shape.
    """
    turtle.fillcolor("orange") 
    turtle.begin_fill()


def reset():
    """
    The function "reset" resets the turtle's pen size to 1 and lifts the pen up.
    """
    turtle.pensize(1)
    turtle.up()

def big_pen():
    """
    The function sets the pen size to 12 and puts the pen down.
    """
    turtle.pensize(12)
    turtle.down()


def end_fill():
    """
    The function `end_fill()` is used to end the filling of a shape in turtle graphics.
    """
    turtle.end_fill()

def T_sign():
    """
    The function draws a T-shaped sign using the turtle module in Python.
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
    The function draws a t-shaped sign using the turtle module in Python.
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
    The function draws the letter "O" in a roundabout style sign using the turtle graphics module in Python.
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
    
def start_up():
    """
    The function "start_up" sets up the turtle graphics environment and prints a message indicating that
    the setup is complete.  
    """
    turtle.speed(20)
    turtle.left(180)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.speed(5)
    turtle.setup(width=1200, height=450)
    turtle.setworldcoordinates(-100, 0, 550, 250)
    print("setup complete!")

    
def main():
    """
    The main function creates four different signs using turtle graphics and prints a message when each
    sign is done.
    """
    start_up()
    n = 0 
    while(n < 4):
        sign()
        if n == 0:
            T_sign()
        if n == 1:
            x_sign()
        if n == 2:
            t_sign()
        if n == 3:
            o_sign()
        turtle.forward(150)
        n += 1
        print("Done with sign: " + str(n))
    print("Done with all signs!")    
    turtle.done()

# The `main()` function is the entry point of the program. It sets up the turtle graphics environment,
# creates four different signs using turtle graphics, and prints a message when each sign is done.
# Finally, it prints a message indicating that all signs are done and calls the `turtle.done()`
# function to finish the turtle graphics program.
main()


"""
Author - 8FA
Last update - 01/19/2024
"""