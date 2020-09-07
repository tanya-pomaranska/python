# Write a Python program to check the validity of a password (input from users).

# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
import re

def Verification_Pasword(passwd):
    """The password check that we get by entering a password like input parameter,
       and returns true if the password matches the check parameters
       or returns false and show all errors"""

    error_list=[]
    if len(passwd)<6 or len(passwd)>16:
        error_list.append("Have to be minimum 6 characters and maximum 16 characters")

    if not re.search("[a-z]",passwd):
        error_list.append("Have to be at least one characters in low")

    if not re.search("[0-9]",passwd):
        error_list.append("Have to be at least one number")

    if not re.search("[A-Z]",passwd):
        error_list.append("Have to be at least one characters in Uppercase")

    if not re.search("[$#@]",passwd):
        error_list.append("Have to be at least one symbol $#@")

    if error_list:
        for next in error_list:
           print(next)

        return False
    else: return True



print("    --> At least 1 letter between [a-z] and 1 letter between [A-Z].\n\
    --> At least 1 number between [0-9].\n\
    --> At least 1 character from [$#@].\n\
    --> Minimum length 6 characters.\n\
    --> Maximum length 16 characters\n")

while True:
    my_passwd= input("Input your password -->")

    if Verification_Pasword(my_passwd):
        print("Very nice password. Much secure")
        break

    else:
        if (input("Not a Valid Password.\nTry again? y/n\n")) =='n':
            break
        else :continue
