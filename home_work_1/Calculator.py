while True:
    # Take input from the user
    first_number = float(input("Enter first number: "))
    operand=input("Enter operation +, -, *, /, ** : ")
    # Check if choice is one of the five options
    if operand in ('+', '-', '*', '/', '**'):

        second_number = float(input("Enter second number: "))

        if operand == '+':
            print(first_number, "+", second_number, "=", first_number+second_number)

        elif operand == '-':
            print(first_number, "-", second_number, "=", first_number-second_number)

        elif operand == '*':
            print(first_number, "*", second_number, "=", first_number*second_number)

        elif operand == '/':
            if second_number==0 : print("You can't divide to 0")
            else: print(first_number, "/", second_number, "=", first_number/second_number)

        elif operand == '**':
            print(first_number, "**", second_number, "=", first_number**second_number)
        break
    else:
        if input("Invalid Input. Continue? y/n   ") == 'n':
           break
        else:
            continue
