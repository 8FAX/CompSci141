import random

names = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
# This code snippet is generating fake data by randomly selecting a name from the `names` list and a
# number between 1 and 300. It then writes this data to a file named `input.txt`. The `with
# open('input.txt', 'w') as f:` statement opens the file in write mode and assigns it to the variable
# `f`.
with open('input.txt', 'w') as f:
    i = 0
    for _ in range(30000): 
        name = random.choice(names)
        i += 1
        number = random.randint(1, 300)
        f.write(f"{name}{i} {number}\n")
    print("Fake data generated and saved to input.txt")