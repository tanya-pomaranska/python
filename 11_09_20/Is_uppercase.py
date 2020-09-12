#Create a method is_uppercase() to see whether the string is ALL CAPS.

def is_uppercase(inp):
    return True if inp.isupper() else False



print(is_uppercase("c")) # False
print(is_uppercase("C")) # True
print(is_uppercase("hello I AM DONALD")) # False
print(is_uppercase("HELLO I AM DONALD")) # True
print(is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ")) # False
print(is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ")) # True