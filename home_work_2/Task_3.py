# Change values in variables without third variable
first_variable = input("Enter value for first variable: ")
second_variable = input("Enter value for second variable: ")

print(f"first_variable: {first_variable} second_variable: {second_variable}", end="\n\n")

first_variable, second_variable = second_variable, first_variable

print(f"After changing \nfirst_variable: {first_variable} second_variable: {second_variable}", end="\n\n")