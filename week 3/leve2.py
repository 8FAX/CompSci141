import turtle as t

def bow3(h, depth):
    if depth == 1:
        bow(h)
    else:
        bow(h)
        t.left(30)
        t.forward(2*h)
        bow3(h/3, depth-1)
        t.backward(2*h)
        t.left(120)
        t.forward(2*h)
        t.right(180)
        bow3(h/3, depth-1)
        t.right(180)
        t.backward(2*h)
        t.right(150)

def bow(h):
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
    t.right(30)
    t.penup()

# Get user input for depth
depth = int(input("Enter the depth: "))

# Draw the bow with the specified depth
bow3(100, depth)
t.done()