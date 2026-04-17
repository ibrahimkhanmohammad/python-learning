input("Enter your Name: ")     # basic input() clearly helps you to get the input from the user

name = input("Enter your name: ")   # Ask user for their Name 


# Say Hello to the user
print("Hello,")         # Here "name" is a variable given to input() so that it can store the value from the user and print it when the variables are read or used
print(name)         


print("Hello, " + name)     # passes one argument

print("Hello,", name)       # function passes two arguments

print("Hello ,", end="")       # from the original documentation of the print() in python
print(name)