#Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

def double_char(s):
    return ''.join([next_str + next_str for next_str in s])


print(double_char("String"))      #  "SSttrriinngg"
print(double_char("Hello World")) #"HHeelllloo  WWoorrlldd"
print(double_char("1234!_ "))     #"11223344!!__  "