'''⚡ CHEAT SHEET

abs(x)          # remove negative
round(x, n)     # round to n decimals
int(x)          # convert to int
float(x)        # convert to float
min(a, b, c)    # smallest
max(a, b, c)    # largest
pow(x, y)       # x^y
type(x)         # data type'''


# 🔹 abs() → absolute value (removes negative sign)
print(abs(-10))        # 10


# 🔹 round() → rounds number to nearest integer (or decimal)
print(round(3.6))      # 4
print(round(3.2))      # 3
print(round(3.14159, 2))  # 3.14


# 🔹 int() → converts to integer
print(int(3.9))        # 3 (cuts decimal, not rounding)
print(int("10"))       # 10


# 🔹 float() → converts to decimal number
print(float(5))        # 5.0
print(float("3.14"))   # 3.14


# 🔹 min() and max() → smallest and largest value
print(min(1, 5, 2))    # 1
print(max(1, 5, 2))    # 5

nums = [10, 20, 5]
print(min(nums))       # 5
print(max(nums))       # 20


# 🔹 pow() → power (x^y)
print(pow(2, 3))       # 8


# 🔹 type() → tells data type
print(type(10))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Hello"))   # <class 'str'>


#  METHOD COMBINATIONS 

print(round(abs(-3.7)))   # 4
print(int(float("10.8")))  # 10