#  input type 
def addition() -> int:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a + b)


addition()

# return basic
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

ans = add(2, 3)          # 5
ans = multiply(ans, 10)  # 50 (uses previous result)
print(ans)

# Task -1 == write a function square(num) that returns the square of the num ==

def square(num = 10):
    return num**2

print(square(9))


# Task -2 == Define a function convert_to_upper (word) that returns the uppercase version of the string ==

def convert_to_upper(word):
    return word.upper()

name = input()
print(convert_to_upper(name))

#  Task -3 == Create a function full_name(fname, lname) that returns the full name joined with a space ==


def full_name(fname, lname):
    return fname + " " + lname

f = input("First name: ")
l = input("Last name: ")
print(full_name(f, l))

'''Variable Scope (Local vs Global)

. Local Variable: Defined inside a function - accessible only within it.

. Global Variable: Defined outside any function -- accessible everywhere. '''