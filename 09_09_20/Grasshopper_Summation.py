#Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.
def summation(num):
    sum = 0
    for next in range(1,num+1):
        sum += next
    return sum


print(summation(1)) # 1
print(summation(8)) # 36
print(summation(22)) # 253
print(summation(100)) # 5050
print(summation(213)) # 22791

#Another variant  return sum(range(1,num+1))