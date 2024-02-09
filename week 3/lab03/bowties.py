import turtle as t

def setup(size):
    """
    The function sets up the turtle graphics window with a specified size.
    
    Author - Liam Scott
    Last update - 02/04/2024
    @param size () - The size parameter determines the size of the turtle window. The turtle window will
    have a width of size*12 and a height of size*6.
    
    """
    t.setup(size*12, size*6)
    t.speed(0)

def bow3(size, depth, color1, color2):
    """
    The `bow3` function recursively draws a pattern of bows using turtle graphics.
    
    Author - Liam Scott
    Last update - 02/04/2024
    @param size () - The size parameter determines the size of the bow. It is used to calculate the size
    of each subsequent smaller bow in the recursive calls.
    @param depth () - The parameter "depth" represents the number of times the function will recursively
    call itself. It determines the level of detail or complexity of the bow shape.
    @param color1 () - The parameter "color1" represents the color of the outer part of the bow.
    @param color2 () - The parameter "color2" is used to specify the color of the second part of the
    bow. It is a string that represents a valid color in turtle graphics.
    
    postcondition: pen up in the middle of the bow looking east with fill off
    """
    if depth == 1:
        bow(size, color1, color2)
    else:
        bow(size, color1, color2)
        t.left(30)
        t.forward(2*size)
        bow3(size/3, depth-1, color1, color2)
        t.backward(2*size)
        t.right(60)
        t.forward(2*size)
        bow3(size/3, depth-1, color1, color2)
        t.backward(2*size)
        t.right(120)
        t.forward(2*size)
        t.right(180)
        bow3(size/3, depth-1, color1, color2)
        t.forward(2*size)
        t.right(60)
        t.backward(2*size)
        bow3(size/3, depth-1, color1, color2)
        t.forward(2*size)
        t.left(30)


def cer(size, color2):
    """
    The function `cer` draws a filled circle with a specified size and color.
    
    Author - Liam Scott
    Last update - 02/02/2024
    @param size () - The size parameter determines the size of the circle to be drawn. It is used to
    calculate the radius of the circle by dividing it by 4.
    @param color2 () - The parameter "color2" is the color that will be used to fill the circle.
    
    postcondition: pen up in the middle of the bow looking east with fill off
    """
    t.fillcolor(color2)
    t.down()
    t.begin_fill()
    t.circle(size/4)
    t.up()
    t.end_fill()
    

def bow(size, color1, color2):
    """
    The `bow` function draws a bow shape using turtle graphics, with a specified size and two colors.
    
    Author - Liam Scott
    Last update - 02/02/2024
    @param size () - The size parameter determines the size of the bow. It is used to calculate the
    length of the lines and the distance to move the turtle.
    @param color1 () - The parameter "color1" is used to specify the color of the outline of the bow.
    @param color2 () - The parameter "color2" is the color of the center of the bow.
    
    postcondition: pen up in the middle of the bow looking east
    """
    t.pencolor(color1)
    t.pendown()
    t.left(30)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.right(120)
    t.forward(2*size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.penup()
    t.right(90+ 30)
    t.forward(size/4)
    t.left(90)
    cer(size, color2)
    t.penup()
    t.left(90)
    t.forward(size/4)
    t.right(90)



def main():
    """
    The main function sets up the parameters for creating a bow design and then calls the bow3 function
    to draw the design.
    
    Author - Liam Scott
    Last update - 02/04/2024
    
    """
    depth = int(input("Enter the depth: "))
    size = int(input("Enter the size of the bows: "))
    color1 = input("Enter outline color for the bows: ")
    color2 = input("Enter fill color for the bows: ")

    #for quick use comment out the inmput above ^ and uncomment the vars below!

    # color1 = "green"
    # color2 = "blue"
    # depth = 5
    # size = 100
    setup(size)
    bow3(size, depth, color1, color2)
    t.done()


# The `if __name__ == '__main__':` statement is used to check if the current script is being run
# directly or if it is being imported as a module.
if __name__ == '__main__':
     main()