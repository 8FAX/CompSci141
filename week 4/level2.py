import turtle as t
import random

# These variables are used to set the dimensions and parameters for the turtle graphics window and the
# snake drawing.
width = 400
height = 400
max_seg = 500
min_seg = 0
max_lag = 20
min_lag = 1
max_thick = 10
min_thick = 1
max_angle = 30
min_angle = -30
buffer = 100

def set_up_window():    
    """
    The function sets up the window for turtle graphics by adjusting the width and height and hiding the
    turtle.
    
    Author - Liam Scott
    Last update - 02/12/2024
    
    """
    t.setup(width + buffer, height + buffer)
    t.hideturtle()

def random_spin():
    """
    The function "random_spin" returns a random integer between the values of "min_angle" and
    "max_angle".
    
    Author - Liam Scott
    Last update - 02/12/2024
    @returns a random integer between the values of `min_angle` and `max_angle`.
    
    """
    return random.randint(min_angle, max_angle)

def random_length():
    """
    The function "random_length" returns a random integer between the values of "min_lag" and "max_lag".
    
    Author - Liam Scott
    Last update - 02/12/2024
    @returns a random integer value between the minimum lag and maximum lag.
    
    """
    return random.randint(min_lag, max_lag)

def random_thickness():
    """
    The function "random_thickness" returns a random integer between the values of "min_thick" and
    "max_thick".
    
    Author - Liam Scott
    Last update - 02/12/2024
    @returns a random integer value between the minimum thickness (min_thick) and the maximum thickness
    (max_thick).
    
    """
    return random.randint(min_thick, max_thick)

def generate_random_color():
    """
    The function generates a random color in hexadecimal format.
    
    Author - Liam Scott
    Last update - 02/12/2024
    @returns a randomly generated color in hexadecimal format.
    
    """
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return random_color

def box():
    """
    The function `box()` draws a red square with a black border using the turtle graphics module in
    Python.
    
    Author - Liam Scott
    Last update - 02/12/2024
    
    Postcondition: Pen up facing down at 0,0 tracer on speed set to 10 pen set to black and set to size 1
    """
    t.penup()
    t.clear()
    t.setheading(0)
    t.speed(0)
    t.tracer(False)
    t.goto(0,0)
    t.goto(-190,-190)
    t.pendown()
    t.pensize(3)
    t.pencolor("RED")
    t.forward(400)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(400)
    t.penup()
    t.pencolor("black")
    t.goto(0,0)
    t.pensize(1)
    t.tracer(True)
    t.speed(10)

def check_boundary(pos, heading, length): 
    """
    The function checks if a turtle's next move will go beyond the boundaries of a given width and
    height, and adjusts the turtle's heading accordingly.
    
    Author - Liam Scott
    Last update - 02/12/2024
    @param pos () - The `pos` parameter represents the current position of an object. It is a tuple
    containing the x and y coordinates of the object's position.
    @param heading () - The heading parameter represents the current direction the object is facing,
    measured in degrees.
    @param length () - The length parameter represents the distance that the turtle will move forward.
    @returns a tuple containing two values. The first value is a boolean indicating whether the boundary
    has been reached or not. The second value is the new heading after adjusting for the boundary.
    
    Precondition: 'seg' from 'snake_FUNCTION()' must be grater then 0 and not less then 0 
    """
    sensitivity = length / 2  
    new_x = pos[0] + length * (1 if heading % 180 == 0 else -1)
    new_y = pos[1] + length * (1 if (heading + 90) % 180 == 0 else -1)
    if abs(new_x) > width / 2 - sensitivity or abs(new_y) > height / 2 - sensitivity:
        
        new_heading = (heading + 180) % 360 
        t.setheading(new_heading)
        t.right(random_spin())
        t.forward(length)
        return True, new_heading
    
    return False, heading

def snake_while(seg):
    """
    The function `snake_while` draws a snake with a given number of segments using a while loop.
    
    Author - Liam Scott
    Last update - 02/12/2024
    @param seg () - The parameter "seg" represents the number of segments that the snake will have.
    @returns the total distance traveled by the snake, which is stored in the variable "tot".
    
    Precondition: turtle is reset by 'box()' (set to black, pen size 1, facing down, at 0,0)
    """
    t.pendown()
    tot = 0
    while seg > 0:
        length = random_length()
        t.pencolor(generate_random_color())
        t.pensize(random_thickness())
        pos = t.position()
        heading = t.heading()
        if check_boundary(pos, heading, length):
            t.forward(length)
            t.left(random_spin())
            tot += length
            seg -= 1
            continue
        t.forward(length)
        t.left(random_spin())
        tot += length
        seg -= 1
    return tot

def snake_rec(seg, tot):
    """
    The function `snake_rec` recursively draws segments of a snake, each with a random length, color,
    and thickness, and returns the total length of the snake.
    
    Author - Liam Scott
    Last update - 02/12/2024
    @param seg () - The parameter "seg" represents the number of segments or sections of the snake that
    will be drawn.
    @param tot () - The parameter "tot" represents the total length of the snake.
    @returns the total length of the snake after all segments have been drawn.
    
    Precondition: turtle is reset by 'box()' (set to black, pen size 1, facing down, at 0,0)
    """
    t.pendown()
    if seg == 0:
        return tot 
    length = random_length()
    t.pencolor(generate_random_color())
    t.pensize(random_thickness())
    pos = t.position()
    heading = t.heading()
    if check_boundary(pos, heading, length):
        t.forward(length)
        t.left(random_spin())
    else:
        t.forward(length)
        t.left(random_spin())
    return length + snake_rec(seg - 1 , tot)

def snake_tail(seg, tot):
    """
    The function `snake_tail` draws a snake tail by recursively moving the turtle forward and changing
    its direction.
    
    Author - Liam Scott
    Last update - 02/12/2024
    @param seg () - The parameter "seg" represents the number of segments or sections of the snake's
    tail. It determines how many times the function will recursively call itself to draw each segment of
    the tail.
    @param tot () - The `tot` parameter represents the total length of the snake's tail.
    @returns the total length of the snake's tail.
    
    Precondition: turtle is reset by 'box()' (set to black, pen size 1, facing down, at 0,0)
    """
    t.pendown()
    if seg == 0:
        return tot 
    length = random_length()
    t.pencolor(generate_random_color())
    t.pensize(random_thickness())
    pos = t.position()
    heading = t.heading()
    if check_boundary(pos, heading, length):
        t.forward(length)
        t.left(random_spin())
    else:
        t.forward(length)
        t.left(random_spin())
    return  snake_rec(seg - 1 , length + tot)


def main():
    """
    The main function prompts the user for the number of segments they want, checks if it is within the
    valid range, and then proceeds to create an iterative snake, a recursive snake, and a tail recursive
    snake.
    
    Author - Liam Scott
    Last update - 02/12/2024
    
    """
    seg = int(input("How many segments do you want? (0-500) "))
    if seg > max_seg or seg < min_seg:
        print("You cant use \"" + str(seg) + "\"! Please use: A number from 0 to 500! ")
        main()
    else:
        set_up_window()    
        box()
        t.speed(10)
        print("Now making iterative snake! ")
        tail_ink = snake_while(seg)
        print("The iterative snake is done and used " + str(tail_ink) + " ink!") 
        input("Press the ENTER key to continue... ")
        box()
        print("Now making recursive snake! ")
        rec_ink = snake_rec(seg, 0)
        print("The recursive snake is done and used " + str(rec_ink) + " ink!")
        input("Press the ENTER key to continue... ")
        box()
        print("Now making tail recursive snake! ")
        rec_ink = snake_tail(seg, 0)
        print("The tail recursive snake is done and used " + str(rec_ink) + " ink!")
        t.done()


# The `if __name__ == '__main__':` statement is used to check if the current script is being run as
# the main module. If it is, then the `main()` function is called. This allows the script to be
# imported and used as a module in other scripts without automatically executing the `main()`
# function.
if __name__ == '__main__':  
    main()