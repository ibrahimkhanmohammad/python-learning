#   operators are of (+, -, *, /, %, **, //)

#   integers
x = 1
y = 2

z = x + y
print(z)

#   by taking input from the user
#   we used int because  by default input() takes string as input, so we're telling to the interpreter that we're changing the input() as int
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

print(num_1 + num_2)

#   floating-point numbers
a = float(input("Enter any number: "))
b = float(input("Enter another number: "))

print(a * b)


#   round method == used to round-off the output, also: it's syntax is of like; round(number[, ndigits]) => here we can say that the number parameter tell us that the parameters to be followed are only 1 and also after, [] -> it tells us that it's completely optional but if so we want to specify the digits to round-off then we will use this called (, ndigits) like; => round(a, 4)

e = float(input("Enter any number: "))
f = float(input("Enter another number: "))

g = round(e/f, 2)

print(g)