#Bob is working as a bus driver.
# However, he has become extremely popular amongst the city's residents.
# With so many passengers wanting to get aboard his bus,
# he sometimes has to face the problem of not enough space left on the bus!
# He wants you to write a simple program telling him if he will be able to fit all the passengers.
# return max(on + wait - cap, 0)
def enough(cap, on, wait):
    if cap >= on+wait:
        return 0
    else: return (on + wait)-cap


print(enough(10, 5, 5)) # 0
print(enough(100, 60, 50)) # 10
print(enough(20, 5, 5)) # 0