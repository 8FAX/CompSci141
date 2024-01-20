weight = float(input("weight: ")) 
input_unit = input("input unit (K)g or (L)bs: ")
output_unit = input("output unit (K)g or (L)bs: ")

input_unit = input_unit.lower()
output_unit = output_unit.lower()

if input_unit == "l":
    if output_unit == "l":
        print("your weight is: " + str(weight) + "Lbs")
    elif output_unit == "k":
        new_weight = weight * 0.45359237
        print("your weight is: " + str(new_weight) + "Kg")

elif input_unit == "k":
    if output_unit == "k":
        print("your weight is: " + str(weight) + "Kg")
    elif output_unit == "l":
        new_weight = weight * 2.20462262
        print("your weight is: " + str(new_weight) + "Lbs")
     

