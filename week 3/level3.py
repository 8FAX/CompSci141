import turtle as t

def bow3(size, depth, color1, color2):
    """
    The function `bow3` recursively draws a pattern of bows using turtle graphics.
    
    Author - Liam Scott
    Last update - 02/02/2024
    @param size () - The size parameter determines the size of the bow. It is used to calculate the size
    of each subsequent smaller bow in the recursive calls.
    @param depth () - The parameter "depth" represents the number of times the function will recursively
    call itself. It determines the level of detail or complexity of the bow shape.
    @param color1 () - The color of the outer part of the bow.
    @param color2 () - The parameter "color2" is used to specify the color of the second part of the
    bow.
    
    """
    if depth == 1:
        bow(size, color1, color2)
    else:
        bow(size, color1, color2)
        t.left(30)
        t.forward(2*size)
        bow3(size/3, depth-1, color1, color2)
        t.backward(2*size)
        t.left(120)
        t.forward(2*size)
        t.right(180)
        bow3(size/3, depth-1, color1, color2)
        t.right(180)
        t.backward(2*size)
        t.right(150)

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
    The main function prompts the user for input and then calls the bow3 function to draw a bow with the
    specified depth.

    
    # Get user input for depth !!NO ERROR CORRECTION!! per request of the lab 03 assignment, HEX will work.
    # Note: yes it would be so easy if i set the color as static, then i could set the color 1 time in the bow and cer function and forget it, but i think this is more fun!
    
    Author - Liam Scott
    Last update - 02/02/2024
    
    """
    depth = int(input("Enter the depth: "))
    size = int(input("Enter the size of the bows: "))
    color1 = input("Enter outline color for the bows: ")
    color2 = input("Enter fill color for the bows: ")
    bow3(size, depth, color1, color2)
    t.done()


# The `if __name__ == '__main__':` statement is used to check if the current script is being run
# directly or if it is being imported as a module.
if __name__ == '__main__':
     main()