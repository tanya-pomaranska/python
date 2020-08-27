# Sum digits of number
my_number = int(input("Enter the four-digit number  "))
sum_of_number = int(my_number%10) + int(my_number/10)%10 + int(my_number/100)%10 + int(my_number/1000)
print(f"Sum digits of number : {my_number} is {sum_of_number}", end ="\n\n")

# Digit in reverse two variants

# print(f"Number : {my_number} is reverse to  {int(str(my_number)[::-1])}", end="\n\n")

my_number_list = list(str(my_number))
my_number_list.reverse()

print(f"Number : {my_number} is reverse to {''.join(my_number_list)}", end ="\n\n")

# Sort digit in number
my_number_list.sort()
print(f"Sort number : {my_number} : {''.join(my_number_list)}", end ="\n\n")

#Convert list to int
my_number = int("".join(map(str, my_number_list)))
print(f"{my_number} + 5 = {my_number + 5}")