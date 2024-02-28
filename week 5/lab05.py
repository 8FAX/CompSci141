import turtle as t
import meteo as met

def get_num(weather):
    """
    The function `get_num` extracts and returns the numerical value from a given string representing
    weather information.
    
    Author - Liam Scott
    Last update - 02/27/2024
    @param weather () - The `weather` parameter is a string that contains different coordinates, the `get_num` 
    extracts the coordinates from the string.
    @returns The function `get_num` returns an integer value extracted from the input `weather` string.
    The function processes the input string to extract the numerical value present at the beginning of
    the string. If the extracted value is 0 or - with no number value after it, the function prints an
    error message and exits. Otherwise, it returns the extracted integer value.
    
    """
    new_str = ""
    for i in weather:
        if i.isdigit() or i == '-':
            new_str += i
        else:
            break
    new_str = new_str.lstrip('0') if new_str[0] != '-' else '-' + new_str[1:].lstrip('0')
    if new_str == '' or new_str == '-':
        print(f"Invalid number value String can not be 0 or - with no number value after it. {new_str} is not a valid number value.")
        exit()
        return 
    else:
        return int(new_str) 

def white_box():
    """
    The function `white_box` draws a white filled rectangle with black outline.
    
    Author - Liam Scott
    Last update - 02/27/2024

    post-conditions: The turtle will be facing east after drawing the white box.
    post-conditions: The turtle will be pen up after drawing with fill off and pen set to black.
    
    """
    t.fillcolor("white")
    t.pencolor("white")
    t.begin_fill()
    t.down()
    t.forward(36)
    t.right(90)
    t.forward(16)
    t.right(90)
    t.forward(36)
    t.right(90)
    t.forward(16)   
    t.right(90)
    t.end_fill()
    t.up()
    t.pencolor("black")    

def splicer(weather_string):
    """
    The function `splicer` processes a weather string by executing different commands based on the
    characters in the string.
    
    Author - Liam Scott
    Last update - 02/27/2024
    @param weather_string () - Passed in from the main function, the `weather_string` parameter is a string
    that contains different commands and coordinates for different weather types. The function processes.

    Post-conditions: Remove the first character or IF "T, A" removes the numbers aswell from the string and call the main_splicer function with the
    new string.
    
    """
    x_cord = 0
    y_cord = 0

    if weather_string[0] in ['S', 'P', 'C', 'R', 'W']:
        if weather_string[0] == 'S':
            command_S(x_cord, y_cord)
        if weather_string[0] == 'P':
            command_P(x_cord, y_cord)
        if weather_string[0] == 'C':
            command_C(x_cord, y_cord)
        if weather_string[0] == 'R':
            command_R(x_cord, y_cord)
        if weather_string[0] == 'W':
            command_W(x_cord, y_cord)
        main_splicer(weather_string[1:])
            
    if weather_string[0] == 'T' or weather_string[0] == 'A':
        if weather_string[1] == '-' or weather_string[1].isdigit() == True:
            number = get_num(weather_string[1:]) 
            if weather_string[0] == 'T':
                command_T(x_cord, y_cord, str(number))
            if weather_string[0] == 'A':
                command_A(x_cord, y_cord, str(number))
            main_splicer(weather_string[1+ len(str(number)):])
        else:
            print(f"Invalid use of {weather_string[0]}, you must pass in a correct number value after the symbol")
            exit()
    else:
        main_splicer(weather_string)

        
def main_splicer(weather_string):
    """
    The function `main_splicer` parses a weather string to extract coordinates and commands for
    different weather types, executing corresponding functions based on the input.
    
    Author - Liam Scott
    Last update - 02/27/2024
    @param weather_string () - Passed in from the main function, the `weather_string` parameter is a string
    that contains different commands and coordinates for different weather types. The function processes.

    Pre-conditions: The weather_string must be a string that contains different commands and coordinates for different weather types.
    Pre-conditions: The weather_string has been passed through the splicer function and has had the first character removed if needed and the numbers removed if needed.
    
    """
    i = 0
    x_cord = 0
    y_cord = 0

    while i < len(weather_string):
        if weather_string[i] == "G":
            if len(weather_string) >= i:
                if weather_string[i+1] == '-' or weather_string[i+1].isdigit() == True:
                    i += 1
                    x_cord = get_num(weather_string[i:])
                    i += len(str(x_cord)) + 1
                    if x_cord >= 550 or x_cord <= -550:
                        print(f"Invalid X coordinate value ({x_cord}) for G pick a value between -550 and 550")
                        exit()
                    if weather_string[i] == '-' or weather_string[i].isdigit() == True:
                        y_cord = get_num(weather_string[i:])
                        i += len(str(y_cord))
                        if y_cord >= 350 or y_cord <= -350:
                            print(f"Invalid Y coordinate value ({y_cord}) for G pick a value between -550 and 550")
                            exit()
                    else:
                        print(f"Invalid use of {weather_string[i]}, you must pass in 2 correct coordinate values after the symbol")
                        exit()
                    if i == len(weather_string):
                        print("Invalid use of G, you must pass in Type like \"S\" after the correct coordinate values")
                        exit()
                else:
                    print(f"Invalid use of {weather_string[i]}, you must pass in 2 correct coordinate values after the symbol")
                    exit()
            else:
                print(f"Invalid use of {weather_string[i]}, you must pass in 2 correct coordinate values after the symbol")
                exit()
            
            
        if weather_string[i] in ['S', 'P', 'C', 'R', 'W']:
            if weather_string[i] == 'S':
                command_S(x_cord, y_cord)
            if weather_string[i] == 'P':
                command_P(x_cord, y_cord)
            if weather_string[i] == 'C':
                command_C(x_cord, y_cord)
            if weather_string[i] == 'R':
                command_R(x_cord, y_cord)
            if weather_string[i] == 'W':
                command_W(x_cord, y_cord)
            i += 1
        if i == len(weather_string):
            break
        if weather_string[i] == 'T' or weather_string[i] == 'A':
            if len(weather_string)-1 <= i:
                print(f"Invalid use of {weather_string[i]}, you must pass in a correct number value after the symbol")
                exit()
            else:
                if weather_string[i+1] == '-' or weather_string[i+1].isdigit() == True:
                    number = get_num(weather_string[i+1:])
                    if weather_string[i] == 'T':
                        command_T(x_cord, y_cord, str(number))
                    if weather_string[i] == 'A':
                        command_A(x_cord, y_cord, str(number))
                    i += len(str(number)) + 1
                else:
                    print(f"Invalid use of {weather_string[i]}, you must pass in a correct number value after the symbol")
                    exit()

    

def go_to(x,y):
    """
    The function `go_to(x, y)` in Python is used to move the turtle to the specified coordinates (x, y)
    on the screen.
    
    Author - Liam Scott
    Last update - 02/27/2024
    @param x () - The parameter `x` in the `go_to` function represents the x-coordinate where you want
    to move the turtle or cursor to on the screen.
    @param y () - The parameter `y` in the `go_to` function represents the y-coordinate where you want
    to move the turtle to on the screen. It specifies the vertical position on the screen where the
    turtle should go.

    post-conditions: The turtle will move to the specified coordinates (x, y) on the screen.
    post-conditions: The turtle will be facing east after moving to the specified coordinates.
    
    """
    t.penup()
    t.goto(x, y)
    t.setheading(0)

def command_S(x, y):
    """
    This function takes in coordinates (x, y), moves to that position, and then draws a sun using the
    met module.
    
    Author - Liam Scott
    Last update - 02/27/2024
    @param x () - It looks like the function `command_S` takes two parameters `x` and `y`. The `x`
    parameter is likely the x-coordinate where you want to go, typically representing the horizontal
    position on a coordinate plane.
    @param y () - The parameter `y` in the `command_S` function likely represents the y-coordinate where
    you want to move to or draw something. It is a numerical value that specifies the vertical position
    on the screen or canvas.
    
    """
    go_to(x, y)
    met.draw_sun()

def command_P(x, y):
    """
    The function `command_P` moves to a specified position, draws a sun, moves forward, and draws a
    cloud.
    
    Author - Liam Scott
    Last update - 02/27/2024
    @param x () - The parameter `x` in the `command_P` function likely represents the x-coordinate where
    you want to move to. This could be a specific location on a canvas or screen where you want to
    position the drawing elements.
    @param y () - It seems like you might have missed providing the value for the parameter `y`. Can you
    please provide the value for `y` so that I can assist you further with the `command_P` function?
    
    """
    go_to(x, y)
    met.draw_sun()
    t.forward(6)
    met.draw_cloud()

def command_C(x, y):
    """
    The function `command_C` takes two parameters `x` and `y`, moves to the specified coordinates, and
    then draws a cloud using the `met.draw_cloud()` method.
    
    Author - Liam Scott
    Last update - 02/27/2024
    @param x () - The parameter `x` in the `command_C` function likely represents the x-coordinate where
    you want to move to before drawing the cloud.
    @param y () - The parameter `y` in the `command_C` function likely represents the y-coordinate where
    you want to position the cloud to be drawn. It is used as part of the `go_to(x, y)` function to move
    the drawing cursor to the specified position before calling `met.draw_cloud()` to
    
    """
    go_to(x, y)
    met.draw_cloud()

def command_R(x, y):
    """
    The function `command_R` takes two parameters `x` and `y`, moves to the specified coordinates, and
    then draws rain using a method called `met.draw_rain()`.
    
    Author - Liam Scott
    Last update - 02/27/2024
    @param x () - The parameter `x` in the `command_R` function likely represents the x-coordinate where
    you want to move to before drawing the rain. This allows you to specify the horizontal position on
    the screen where the rain should be drawn.
    @param y () - The `y` parameter in the `command_R` function likely represents the y-coordinate where
    you want to position the rain drawing. It is used to specify the vertical position on the screen
    where the rain should be drawn.
    
    """
    go_to(x, y)
    met.draw_rain()

def command_W(x, y):
    """
    The function `command_W` takes two parameters `x` and `y`, moves to the specified coordinates, and
    then draws snow using the `met.draw_snow()` method.
    
    Author - Liam Scott
    Last update - 02/27/2024
    @param x () - It looks like the `command_W` function takes two parameters, `x` and `y`. The `x`
    parameter likely represents the x-coordinate of a location, where the function will move to, and the
    `y` parameter likely represents the y-coordinate of that location.
    @param y () - The parameter `y` in the `command_W` function likely represents the y-coordinate where
    you want to go to in the code. It is used to specify the vertical position or location in the
    coordinate system.
    
    """
    go_to(x, y)
    met.draw_snow()

def command_A(x, y, symbol):
    """
    The function `command_A` takes input parameters `x`, `y`, and `symbol`, then moves to coordinates
    `(x, y)` and draws a circle with a radius specified in the `symbol` parameter.
    
    Author - Liam Scott
    Last update - 02/27/2024
    @param x () - The parameter `x` in the `command_A` function likely represents the x-coordinate where
    the circle will be drawn on the screen.
    @param y () - The `y` parameter in the `command_A` function likely represents the y-coordinate where
    the circle will be drawn on the screen. It is used to specify the vertical position of the circle.
    @param symbol () - The `symbol` parameter is a string that represents a specific symbol being.
    
    """
    go_to(x, y)
    rat = int(symbol[1:])
    met.draw_circle(rat)

def command_T(x, y, symbol):
    """
    The function `command_T` positions the turtle at coordinates (x, y) and writes a symbol in a white
    box.
    
    Author - Liam Scott
    Last update - 02/27/2024
    @param x () - The parameter `x` in the `command_T` function likely represents the x-coordinate where
    the turtle will move to before executing the rest of the commands. It is used to position the turtle
    on the x-axis within the turtle graphics window.
    @param y () - The `y` parameter in the `command_T` function likely represents the y-coordinate where
    the turtle will move to before executing the rest of the function. It specifies the vertical
    position on the screen where the turtle will be positioned.
    @param symbol () - The `symbol` parameter in the `command_T` function is a string that represents a
    symbol. It is used to display the symbol in a white box at the specified coordinates (x, y) on the
    screen. The function will write the symbol starting from the second character of the string using a
    
    """
    go_to(x, y)
    white_box()
    t.right(90)
    t.forward(16)
    t.left(90)
    t.forward(2)
    t.write(symbol[1:], font=("Arial", 9))


def main():
    """
    The main function takes user input for a weather string, processes it using the splicer function,
    and then prints "Done" before waiting for user input to end the program.
    
    Author - Liam Scott
    Last update - 02/27/2024
    
    """


    met.background()
    weather_string = input("Enter a weather string... ")
    splicer(weather_string)
    print("Done")
    input("Press Enter to kill the program... ")
    t.done()
    
#note i tryed very hard to handle every error type i could think of, if you find one i missed please let me know
if __name__ == "__main__":
    main()




# Notes I had a fun function that is shows below, it would handle all of the calls from the main_splicer function and the splicer. so rater then having to make functions for 
# each command, the main splicer would get the cords and type for me then send that to the function below. I had to remove it because in the DOC for the lab it said all commands should be 
# handled by themself "Create a working function for each command" i think by appraoch was better but I had to remove it. a call to the function would look like:
# map_mark_up(weather_string[i] + str(number), x_cord, y_cord) where weather_string[i] is the command ID and str(number) is the number value after the command ID and x_cord and y_cord are the cords


# this is what the function would look like

# def map_mark_up(symbol, x, y):
#     go_to(x, y)

#     if symbol[0] == "S":
#         met.draw_sun()
#     elif symbol[0] == "A":
#         t.pendown()
#         t.color("red")
#         rat = int(symbol[1:])
#         met.draw_circle(rat)
#     elif symbol[0] == "C":
#         met.draw_cloud()
#     elif symbol[0] == "P":
#         met.draw_sun()
#         t.forward(6)
#         met.draw_cloud()
#     elif symbol[0] == "R":
#         met.draw_rain()
#     elif symbol[0] == "W":
#         met.draw_snow()
#     elif symbol[0] == "T":
#         white_box()
#         t.right(90)
#         t.forward(16)
#         t.left(90)
#         t.forward(2)
#         t.write(symbol[1:], font=("Arial", 9))
