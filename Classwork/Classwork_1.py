#Роздрукувати всі парні числа менші 100
# (написати два варіанти коду: один використовуючи цикл while,
# а інший з використанням циклу for).

print(f"All even numbers in the range from 0 to 100 using for:")
for number in range(0,101,2):
    print(number, end =' ')

print(f"\n\nAll even numbers in the range from 0 to 100 using while:")
number = 0
while number<=100:
     print(number, end =' ')
     number+=2


#Роздрукувати всі непарні числа менші 100.
# (написати два варіанти коду: один використовуючи оператор continue,
# а інший без цього оператора).

print(f"\n\nAll odd numbers in the range from 0 to 100:")
for number in range(101):
    if number%2 == 0:
        continue
    print(number, end =' ')


#Перевірити чи список містить непарні числа.
#(Підказка: використати оператор break)
my_list = [int(item) for item in input("\nEnter the list items : ")]

for number in my_list:
    if number%2 != 0:
        print("I found odd number")
        break
else :  print("I don't found any odd number")

#Створити список, який містить елементи цілочисельного типу,
# потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою.
#(Підказка: використати вбудовану функцію float ()).
my_list = [int(item) for item in input("Enter the list items : ")]

list_of_floats = [float(item) for item in my_list]

print(f"List of Float: {list_of_floats}")


#Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли.
# (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
fib_number = [0,1]
n = int(input("Enter n number for a series of Fibonacci numbers: "))
for next in range(0,n+1):
    fib_number.append(fib_number[next]+fib_number[next+1])

print(fib_number, sep=' ')