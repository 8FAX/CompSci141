import turtle as t
import random

tot = 0
width = 400
height = 400

def set_up_window():    
    t.setup(width + 100, height + 100)
    t.hideturtle()

def random_spin():
    return random.randint(-30, 30)

def random_length():
    return random.randint(1, 20)

def random_thickness():
    return random.randint(1, 10)

def generate_random_color():
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return random_color

def box():
    t.penup()
    t.goto(-190,-190)
    t.pendown()
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

def check_boundary(pos, heading, length): 
    sensitivity = length / 100  
    new_x = pos[0] + length * (1 if heading % 180 == 0 else -1)
    new_y = pos[1] + length * (1 if (heading + 90) % 180 == 0 else -1)
    if abs(new_x) > width / 2 - length or abs(new_y) > height / 2 - sensitivity:
        
        new_heading = (heading + 180) % 360 
        t.setheading(new_heading)
        t.right(random_spin())
        t.forward(length)
        return True, new_heading
    
    return False, heading

def snake_while(seg):
    t.pendown()
    global tot
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

def main():
    set_up_window()
    seg = int(input("How many segments do you want? (0-500) "))
    box()
    t.speed(10)
    print(snake_while(seg))
    t.done()

main()