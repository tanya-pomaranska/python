#Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.

def average_ariphmetic(*args):
    return sum(args)/len(args)

# print(f"Average_ariphmetic of 1 2 3 4 5 is {average_ariphmetic(1,2,3,4,5)}")

#Написати функцію, яка знаходить максимальне число з двох чисел,
# а також в функції використати рядки документації DocStrings.

def max(num1,num2):
    """The function takes 2 integer variables and returns a max number"""
    return num1 if num1 > num2 else num2

# numbers=input("Enter two integer number")
# print(f"Max number is {max(int(numbers[0]),int(numbers[1]))}")

#Написати програму, яка обчислює площу прямокутника,
# трикутника та кола (написати три функції для обчислення площі,
# і викликати їх в головній програмі в залежності від вибору користувача)

def Find_Rectangle_Area(a,b):
    return a*b

def Find_Triangle_Area(a,h):
    return (a/2)*h

def Find_Circle_Area(r):
    return (r**2)*3.1415

answer = 0
while True:
    answer = input("Calculate the area for\n\
           1-Rectangle\n\
           2-Triangle\n\
           3-Circle\n\
           0-Exit\n")
    if answer in ('1','2','3','0'):
        if answer == '1':
            a = int(input("Enter length first side of rectangle "))
            b = int(input("Enter length second side of rectangle "))
            print(f"Rectangle area is {Find_Rectangle_Area(a,b)}")
        elif answer == '2':
            a = int(input("Enter the length of the triangle side "))
            h = int(input("Enter the height of the triangle "))
            print(f"Triangle area is {Find_Triangle_Area(a,h)}")
        elif answer == '3':
            r = int(input("Enter circle radius"))
            print(f"Circle area is {Find_Circle_Area(r)}")
        else: break
    else:
        if input("Invalid Input.Continue? y/n   ") == 'n':
           break
        else:
            continue

#Написати функцію, яка обчислює кількість символів, які входять в задану стрічку
def Symbols_Count(str):
    return {symbol:str.count(symbol) for symbol in str}

my_str="method that modifies the list in-place"
print(f"{Symbols_Count(my_str)}")