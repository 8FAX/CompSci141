import math
import turtle as tur
import math as mat
h = 100

def side():
    tur.left(120)
    tur.forward(0.6 * h)

def reset():
    tur.up()
    tur.right(90)
    tur.forward(h)
    tur.left(90)
def pine():
    tur.left(90)
    tur.down()
    tur.forward(h)
    tur.right(90)
    tur.forward(0.3 * h)
    side()
    side()
    tur.left(120)
    tur.forward(0.3 * h)
    reset()

def oak():
    tur.down()
    tur.left(90)
    tur.forward(h)
    tur.right(90)
    tur.circle(0.4 * h)
    reset()
pi = mat.pi
oak_ink = h * 2.8
pine_ink = 0.8*pi* h + h
house_ink = (100 * 3) + (70.12 * 2)
total_ink = oak_ink + pine_ink + house_ink

def main():
    q_house = input("Would you like a house? y/n: ")
    if q_house == "y":
        q_pos = input("what position would you like it? 1/2/3: ")
        q_color = input("what colour would you like the house: ")
    else:
        print("no house")
    tur.pencolor('green')
    oak()
    tur.forward(100)
    pine()
    print("Ink used: " +str(total_ink) + " " +str(house_ink) + " of witch is from the house!")
    tur.done()
if __name__ == '__main__':
    main()