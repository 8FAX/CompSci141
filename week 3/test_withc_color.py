import turtle as t

def cer(h):
    t.fillcolor("PINK")
    t.down()
    t.begin_fill()
    t.circle(h/4)
    t.up()
    t.end_fill()

def bow(h):
        t.pencolor("Green")
        t.pendown()
        t.left(30)
        t.forward(h)
        t.right(120)
        t.forward(h)
        t.right(120)
        t.forward(2*h)
        t.left(120)
        t.forward(h)
        t.left(120)
        t.forward(h)
        t.penup()
        t.right(90+ 30)
        t.forward(h/4)
        t.left(90)
        cer(h)
        t.penup()
        t.left(90)
        t.forward(h/4)
        t.right(90)
        

def draw_one_bow(h,d):
    if d <=0:
        print("All done!")
        t.done()
    else:
        bow(h)
        t.left(30)
        t.forward(2*h)
        draw_one_bow(h/3,d-1)
        t.backward(2*h)

        t.right(120)
        t.forward(h)
        t.forward(2*h)
        draw_one_bow(h/3,d-1)
        t.backward(2*h)

        t.right(120)
        t.forward(2*h)
        t.forward(2*h)
        draw_one_bow(h/3,d-1)
        t.backward(2*h)
        t.left(120)
        t.forward(h)
        t.forward(2*h)
        draw_one_bow(h/3,d-1)
        t.backward(2*h)
        t.left(120)
        t.forward(h)
bow(100)

