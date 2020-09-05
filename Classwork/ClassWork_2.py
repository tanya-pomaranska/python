#Створити список цілих чисел, які вводяться з терміналу
# та визначити серед них максимальне та мінімальне число.
my_list = [int(item) for item in input("Enter the list items : ")]
print(f"max in this list is: {max(my_list)}", end='\n')
print(f"min in this list is: {min(my_list)}")

#В інтервалі від 1 до 10 визначити числа
#парні, які діляться на 2,
# непарні, які діляться на 3,
# числа, які не діляться на 2 та 3.
my_list=[int(item) for item in range(1,11)]
list_even_divides_2 = []
list_even_divides_3 = []
list_dosnt_divides_2_3 = []
for number in my_list:
    if number%2 == 0 :list_even_divides_2.append(number)
    elif number%3 == 0 :list_even_divides_3.append(number)
    else : list_dosnt_divides_2_3.append(number)

print(f"Even number which divides on 2 is {' '.join(str(num) for num in list_even_divides_2)}", end="\n")
print(f"Odd number which divides on 3 is {' '.join(str(num) for num in list_even_divides_3)}", end="\n")
print(f"Number which dosnt divides on 2 and 3 is {' '.join(str(num) for num in list_dosnt_divides_2_3)}", end="\n")

#Написати програму, яка обчислює факторіал числа,
# яке користувач вводить.(не використовувати рекурсивного виклику функції)
factorial_number = 1
n = int(input("Enter number for Factorial: "))

for next_number in range(1,n+1):
    factorial_number*=next_number

print(f"Factorial {n}! is {factorial_number}")

#Напишіть скрипт, який перевіряє логін, який вводить користувач.
# Якщо логін вірний (“First”), то привітайте користувача.
# Якщо ні, то виведіть повідомлення про помилку.
# (необхідно використати цикл while)

right_login = False

while not right_login:

    my_login = input("Enter your login: ")

    right_login = True  if my_login == "First" else  print("Login is wrong")

else: print("Hello. You are in")

