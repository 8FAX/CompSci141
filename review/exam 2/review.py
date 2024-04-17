'''

1: a break point is a point in the code where the program stops executing and allows the user to inspect the state of the program.

the 3 main types of errors are syntax errors, runtime errors, and logical errors.


data = [1, 2, 3]
data[0] = 3
data[-1] = 1
print(data)
data = (1, 2, 3)
data[0] = 3 {this will give an error because tuples are immutable}
data[-1] = 1
print(data)




'''

L1 = [5, 7, 9]
L2 = [7, 8, 9]
print(L1 + L2)
L1 = L1 + L2
L1.append(L2)
print(L1)
print(L1[6])
print(L1[6][1])

'''
579789789
789
8


0 1 4 6 7 18 20 35

7 18 20 35

20 35

35

O(log n)

 [3, 2, 4, 5, 1]

 2 3 4 5 1
 2 3 4 1 5
 2 3 1 4 5
 2 1 3 4 5
 1 2 3 4 5

 [3, 2, 4, 5, 1]


from dataclasses import dataclass
@dataclass
class Pet:
    name: str
    age: int
    species: str

p = Pet("joe", 5, "dog")

def birthday(pet):
    pet.age += 1

a - none
b - a - none
c - b - a - none
b - a - none
d - b - a - none
e - d - b - a - none

def pop(stack):
    if stack_is_empty(stack):
        return None
    else:
        stack.nodes = stack.nodes.next

def push(stack, value):
    stack.nodes = Node(value, stack.nodes)

def stack_is_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

def dequeue(queue):
    if queue_is_empty(queue):
        return None
    else:
        queue.nodes = queue.nodes.next

def enqueue(queue, value):
    queue.nodes = Node(value, queue.nodes)

  








'''
from dataclasses import dataclass
from typing import Union

@dataclass(frozen=True)
class FrozenNode:
    value: str
    next: Union[None, 'FrozenNode']

lst = FrozenNode("Joey", FrozenNode("doesn't", FrozenNode("share", FrozenNode("food!", None))))

def update(node, value):
    node