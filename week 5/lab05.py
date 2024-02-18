import turtle as t
import meteo as met
Wether_format_string = []

def clean_aray():
    del Wether_format_string[:]

def get_num(weather):
    new_str = ""
    for i in weather:
        if i.isdigit() or i == '-':
            new_str += i
        else:
            break
    return int(new_str) 
        
        
def splicer(weather):
    i = 0
    x_cord = 0
    y_cord = 0
    if weather[i]=="S":
        i+=1
        Wether_format_string.insert(0,"S")
    if weather[i]=="P":
        i+=1
        Wether_format_string.insert(0,"P")
    if weather[i]=="C":
        i+=1
        Wether_format_string.insert(0,"C")
       
    if weather[i]=="G":
        i+=1
        x_cord = get_num(weather[i:])
        i += len(str(x_cord)) + 1
        y_cord = get_num(weather[i:])
        Wether_format_string.insert(1,x_cord)
        Wether_format_string.insert(2,y_cord)
        return

def go_to():
    t.penup()
    t.goto(Wether_format_string[1],Wether_format_string[2])
    t.setheading(0)


def map_mark_up():
    go_to()
    if Wether_format_string[0] =="S":
        met.draw_sun()
    if Wether_format_string[0] =="C":
        met.draw_cloud()
    if Wether_format_string[0] =="P":
        met.draw_sun()
        t.forward(6)
        met.draw_cloud()



def main():
    met.background()
    weather = input("Enter a weather string... ")
    splicer(weather)
    map_mark_up()
    t.done()

main()

