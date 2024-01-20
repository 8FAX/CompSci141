import turtle

def side():
    turtle.forward(100)
    turtle.left(90)

def fill():
    turtle.fillcolor("orange") 
    turtle.begin_fill()
    color = turtle.fillcolor()
    print("set Color " + color)

def end_fill():
    turtle.end_fill()

def sign():
    fill()
    turtle.left(45)
    turtle.down()
    side()
    side()
    side()
    side()
    turtle.up()
    turtle.right(45)
    end_fill()

def main():
    n = 0 
    while(n < 4):
        sign()
        turtle.forward(150)
        n += 1
        print("Done with sign: " + str(n))
    print("Done with all signs!")    
    turtle.done()

main()

