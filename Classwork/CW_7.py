from functools import reduce
import math

# names = ['Sam', 'Don', 'Daniel']
# print(list(map(lambda nameshash: hash(nameshash), names)))
# print(list(map(hash, names)))

#__________________________________________________________________________________________________________________________
#All these numbers in the list have a string data type, for example ['1', '2', '3', '4', '5', '7'],
# convert this list to a list, all numbers of which have the data type integer :
# 1) using the append method

string_numbers = ['1','2','3','4','5','7']
digital_numbers = []
for next in string_numbers:
   digital_numbers.append(int(next))
print("With append method ",digital_numbers)

# 2) using the map method
print("With map ", list(map(int,string_numbers)))


#__________________________________________________________________________________________________________________________
#Display a list of list items that have the values ​​"red",
# ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", “yellow”] using the filter function.
colors = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
print(list(filter(lambda x: x=='red',colors)))


#__________________________________________________________________________________________________________________________
#Convert list containing miles to list containing kilometers (1 mile = 1.6 kilometers)
# a) using the map function
def miles_to_kilometer(miles):
   return round(miles*1.6,2)

miles = [1.5, 2.78, 6.67, 7.8, 8.6, 9.5]
print("Convert list in kilometers using map function", list(map(miles_to_kilometer, miles)))

# b) using the map and lambda function
print("Convert list in kilometers using map and lambda function", list(map(lambda x: round(x*1.6,2), miles)))


#__________________________________________________________________________________________________________________________
#Find the largest item in the list using the reduce function

list_numbers = [2, 4, 6, 3, 10]
print("Max is :", reduce(lambda x,y: x if x>y else y, list_numbers))

#__________________________________________________________________________________________________________________________
#Create a simple generator function similar to the range iterator.
def my_range(stop,start=0,step=1):
    n = start
    while n < stop:
        yield  n
        n += step
print("My simple generator function work like range:")
for num in my_range(10,3):
     print(num)

#__________________________________________________________________________________________________________________________

def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return
      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

# a, b = list(map(int, input("Enter a multiple value through a space: ").split()))

# print(f"Divide of numbers: {divide(a,b)}")

#__________________________________________________________________________________________________________________________
#Using several decorators, create a sandwich consisting of lettuce, tomatoes and meat.
# <\ ^^^^^^^ />
# # tomato #
# --meat–
# ~ salad ~
#  <\ ______ />

def put_ingredients(func):
   def inner(ingredients):
      print(r"<\ ^^^^^^^ />")
      func(ingredients)
      print(r"<\ ______ />")
   return inner


@put_ingredients
def my_sandwich(ingredients):
   deco = ['#', '--', '~']
   i = 0
   for next in ingredients:
       print(f"  {deco[i]}{next}{deco[i]}")
       i +=1


ingredients = ['lettuce', 'tomatoes','meat']
my_sandwich(ingredients)

#__________________________________________________________________________________________________________________________
def smart_divide_sqrt(func):
   def inner(a,b):
      print("I am going to divide sqrt",a,"and",b)
      if a < 0:
         print("Whoops! Сannot root of a negative number")
         return
      return func(a,b)
   return inner

@smart_divide_sqrt
def divide_(a,b):
    return math.sqrt(a)/b

a, b = list(map(int, input("Enter a multiple value through a space: ").split()))

print(f"Divide the root of a number to a number: {divide_(a,b)}")



