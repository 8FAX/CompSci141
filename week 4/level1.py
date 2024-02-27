import turtle as t
import random
tot = 0
max = 500
min = 0

def random_spin():
    r = random.randint(-30, 30)
    t.left(r)

def snake_tail(seg,len,tot):
    if seg == 0:
        return tot
    else:
        t.forward(len)
        random_spin()
        return snake_tail(seg-1,len-1, tot+len)
    
def snake_rec(seg,len):
    if seg == 0:
        return tot
    else:
        t.forward(len)
        random_spin()
        return len + snake_rec(seg - 1, len - 1)


def snake_while(seg, len):
    total_distance = 0
    while seg > 0:
        t.forward(len)
        random_spin()
        total_distance += len
        len -= 1
        seg -= 1
    return total_distance



def main():
    seg = int(input("Enter the number of segments: "))
    if int(seg) > max or int(seg) <= min:
        print("Invalid input")
        main()
    print(snake_tail(seg,100,0))
    input("press enter to clear!")
    t.clearscreen()
    print(snake_rec(seg,100))
    input("press enter to clear!")
    t.clearscreen()
    print(snake_while(seg, 100))
    t.done() 
main()