import turtle as t
import meteo as met

def get_num(weather):
    new_str = ""
    for i in weather:
        if i.isdigit() or i == '-':
            new_str += i
        else:
            break
    return int(new_str) 

def white_box():
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
    x_cord = 0
    y_cord = 0

    if weather_string[0] in ['S', 'P', 'C', 'R', 'W']:
        map_mark_up(weather_string[0], x_cord, y_cord)
        main_splicer(weather_string[1:])
            
    if weather_string[0] == 'T' or weather_string[0] == 'A':
        number = get_num(weather_string[1:]) 
        map_mark_up(weather_string[0]+str(number), x_cord, y_cord)
        main_splicer(weather_string[1+ len(str(number)):])
    else:
        main_splicer(weather_string)

        
def main_splicer(weather_string):
    i = 0
    x_cord = 0
    y_cord = 0

    while i < len(weather_string):
        if weather_string[i] == "G":
            i += 1
            x_cord = get_num(weather_string[i:])
            i += len(str(x_cord)) + 1
            y_cord = get_num(weather_string[i:])
            print(f"i is {i} ")
            i += len(str(y_cord))
        if i == len(weather_string):
            break
        if weather_string[i] in ['S', 'P', 'C', 'R', 'W']:
            map_mark_up(weather_string[i], x_cord, y_cord)
            i += 1
        if i == len(weather_string):
            break
        if weather_string[i] == 'T' or weather_string[i] == 'A':
            number = get_num(weather_string[i + 1:])
            map_mark_up(weather_string[i] + str(number), x_cord, y_cord)
            i += len(str(number)) + 1 

def go_to(x,y):
    t.penup()
    t.goto(x, y)
    print(f"I am at {x}, {y}")
    t.setheading(0)


def map_mark_up(symbol, x, y):
    go_to(x, y)

    if symbol[0] == "S":
        met.draw_sun()
    elif symbol[0] == "A":
        t.pendown()
        t.color("red")
        rat = int(symbol[1:])
        met.draw_circle(rat)
    elif symbol[0] == "C":
        met.draw_cloud()
    elif symbol[0] == "P":
        met.draw_sun()
        t.forward(6)
        met.draw_cloud()
    elif symbol[0] == "R":
        met.draw_rain()
    elif symbol[0] == "W":
        met.draw_snow()
    elif symbol[0] == "T":
        white_box()
        t.right(90)
        t.forward(16)
        t.left(90)
        t.forward(2)
        t.write(symbol[1:], font=("Arial", 9))


def main():

    met.background()
    # weather_string = input("Enter a weather string... ")
    splicer("RG100,100SG20.200PG10,190T50G-200,-40WG-210,-50T70G20,-200A40")
    t.done()

if __name__ == "__main__":
    main()
