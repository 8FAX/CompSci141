"""
    meteo.py
    assignment: lab 4
    language: python3
    author: YOUR NAME GOES HERE

"""

import turtle as t
num = 6
def background():
    """
    load the background for the meteo weather map and
    set up the turtle window size and position in the screen's upper left.
    """
    screen = t.Screen()
    screen.bgpic("simland.png")
    t.setup(1100, 650, 0, 0)
    t.tracer(False)
    t.speed(0)
    t.hideturtle()
    

def draw_rectangle(length, width):
    """
    draws a rectangle with the given length and width
    :param length:
    :param width:
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    t.pendown()
    t.forward(width)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(length)
    pass # YOUR CODE GOES HERE



def snowflake(length=8):
    """
    draws a 6-arms snowflake
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    arms = 0
    while arms <= num:
        t.pendown()
        t.color("Blue")
        t.forward(length)
        t.penup()
        t.backward(length)
        t.right(360//num)
        arms += 1
    t.setheading(90)
    t.color("black")
    pass # YOUR CODE GOES HERE


def draw_sun(r=16):
    t.pencolor("ORANGE")
    t.fillcolor("Yellow")
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.pencolor("black")

    pass # YOUR CODE AND DOCSTRING  GOES HERE

def draw_rain(size=16):
    draw_cloud(16)
    t.pencolor("blue")
    t.right(90)
    t.forward(8)
    t.pendown()
    t.right(45)
    t.forward(size)
    t.penup()
    t.right(45) 
    t.forward(8)
    t.left(45)
    t.pendown()
    t.backward(size)
    t.penup()
    t.right(45) 
    t.forward(8)
    t.left(45)
    t.pendown()
    t.forward(size)
    t.penup()
    t.right(45)
    t.forward(8)
    t.left(45)
    t.pendown()
    t.backward(size)
    t.penup()


    pass # YOUR CODE AND DOCSTRING  GOES HERE
    
def draw_cloud(r=16):
    """
    draws a pretty cloud as a combination of: 1 circle of radius r,
    2 circles of radius r/2 and a rectangle 2r x r
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up, pencolor black
    """
    t.pencolor("blue")
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(r/2)
    t.forward(1.2*r)
    t.circle(r)
    t.forward(1.2*r)
    t.circle(r/2)
    t.backward(2.2*r)
    t.end_fill()
    t.left(90)
    t.begin_fill()
    draw_rectangle(2.2*r, r)
    t.end_fill()
    t.penup()
    t.right(180)
    t.forward(2.2*r)
    t.pencolor("black")
    

def draw_snow(size=8):
    """
    draws 3 snowflakes and a cloud
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    draw_cloud(2*size)
    t.up()
    t.backward(4*size)
    t.right(90)
    t.forward(size)
    t.left(90)
    snowflake(size)
    t.right(135)
    t.forward(2*size)
    t.left(135)
    snowflake(size)
    t.left(135)
    t.forward(2*size)
    t.right(135)
    snowflake(size)
    t.setheading(0)
    

if __name__ == "__main__":
    background()
