import turtle as tur
import math as mat
import random as ran

class data:
    def __init__(self):
        self.oak_count = 0
        self.pine_count = 0
        self.q_pos = 0

data_count = data()

min = 50
pine_max = 200
oak_max = 150
pi = mat.pi
pine_h = ran.randint( min, pine_max )
oak_h = ran.randint( min, oak_max )
oak_c = 0
pine_c = 0
oak_ink = (oak_h * 2.8) * oak_c
pine_ink = (0.8*pi* pine_h + pine_h) * pine_c
house_ink = (100 * 3) + (70.12 * 2)
base_ink = 500
total_ink = oak_ink + pine_ink + house_ink + base_ink

def setup():
    tur.setworldcoordinates(-5,-5,505,305)


def base():
    tur.down()
    tur.pencolor('GREEN')
    tur.forward(500)
    tur.up()
    tur.backward(400)
    tur.pencolor('black')

def house_side():
    tur.forward(100)
    tur.left(90)

def is_valid_color(q_color):
    try:
        tur.colormode(1.0)
        tur.pencolor(q_color)
        return True
    except tur.TurtleGraphicsError:
        return False
    
def house(q_color):  
    tur.down()
    tur.pencolor(q_color)
    house_side()
    house_side()
    tur.right(45)
    tur.forward(70.12)
    tur.left(90)
    tur.forward(70.12)
    tur.left(45)
    house_side()
    tur.up()
    tur.pencolor('black')
    tur.forward(100)


def pine_side():
    tur.left(120)
    tur.forward(0.6 * pine_h)

def pine_reset():
    tur.up()
    tur.right(90)
    tur.forward(pine_h)
    tur.left(90)
    tur.pencolor('black')

def oak_reset():
    tur.up()
    tur.right(90)
    tur.forward(oak_h)
    tur.left(90)
    tur.pencolor('black')
    global oak_c
    oak_c += 1

def pine():
    tur.pencolor('green')
    tur.left(90)
    tur.down()
    tur.forward(pine_h)
    tur.right(90)
    tur.forward(0.3 * pine_h)
    pine_side()
    pine_side()
    tur.left(120)
    tur.forward(0.3 * pine_h)
    pine_reset()
    global pine_c
    data_count.pine_count += 1

def oak():
    tur.pencolor('green')
    tur.down()
    tur.left(90)
    tur.forward(oak_h)
    tur.right(90)
    tur.circle(0.4 * oak_h)
    oak_reset()
    data_count.oak_count += 1

def random_tree():
    tree_functions = [oak, pine]
    ran.choice(tree_functions)()

def pos():
    try:
        q_pos = int(input("What position would you like it? 1/2/3: "))
        if 1 <= q_pos <= 3:
            print("The house will be put in space #" + str(q_pos))
            data_count.q_pos += q_pos
        else:
            print("You can't use \"" + str(q_pos) + "\"! Please use: 1/2/3 ")
            pos()
    except ValueError:
        print("Invalid input. Please enter a number.")
        pos()

def main():
    setup()
    q_house = str.upper(input("Would you like a house? y/n: "))
    if q_house == "Y" or q_house == "YES":
        pos()   
        while True:
            q_color = input("What color would you like the house: ")
            if is_valid_color(q_color):
                print("Thats a good color! We will paint the house \"" + str(q_color) + "\"")
                if data_count.q_pos == 1:
                    base()
                    tur.backward(50)
                    house(q_color)
                    tur.forward(150)
                    random_tree()
                    tur.forward(150)
                    random_tree()
                if data_count.q_pos == 2:
                    base()
                    random_tree()
                    tur.forward(100)
                    house(q_color)
                    tur.forward(100)
                    random_tree()
                if data_count.q_pos == 3:
                    base()
                    tur.backward(50)
                    random_tree()
                    tur.forward(150)
                    random_tree()
                    tur.forward(150)
                    house(q_color)
                total_ink = (oak_height * 2.8) * data_count.oak_count + (0.8 * pi * pine_height + pine_height) * data_count.pine_count + (100 * 3) + (70.12 * 2) + 500
                print("Ink used:", total_ink)
                tur.done()
                break
            else:
                print("You cant use \"" + str(q_color) + "\"! Please use: A color name supported by Turtle or 6-digit Hexadecimal number! ")
    elif q_house == "N" or q_house == "NO":
        print("A tree has grown where the house would have been!")
        base()
        random_tree()
        tur.forward(150)
        random_tree()
        tur.forward(150)
        random_tree()
        tree_ink = (oak_height * 2.8) * data_count.oak_count + (0.8 * pi * pine_height + pine_height) * data_count.pine_count
        print("Ink used:", tree_ink)
        tur.done()
    else:
        print("You cant use \"" + str(q_house) + "\"! Please use: yes/no or y/n")
        main()

if __name__ == '__main__':
    oak_height = ran.randint(min, oak_h)
    pine_height = ran.randint(min, pine_h)
    main()  
