
first = float(input("First Number: "))
opporater = input("what opprater do you want to use? ")
second = float(input("Second Number: "))
if opporater == "-":
    sum = first - second
if opporater == "+":
    sum = first + second
if opporater == "*":
    sum = first * second
if opporater == "/":
    sum = first / second
if opporater == "//":
    sum = first // second


eql_ten = sum == 10
bigger_then_twenty = sum > 10
print("-----------------")
print("sum: " + str(sum))
print("-----------------")
print("Does sum = 10: " + str(eql_ten))
print("IS sum > 10: " + str(bigger_then_twenty))