words = ["Hi", "this is a test", "i hope you like this"]
words.insert(-1,"wow so cool!")

def world():
    for text in words:
        print(text)
i = 0
while i < len(words):
    print(words[i])
    i = i + 1
world()