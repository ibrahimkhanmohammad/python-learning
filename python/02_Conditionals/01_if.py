num_1 = int(input("enter num 1: "))
num_2 = int(input("enter num 2: "))

# We use three separate `if` statements here.
# Each `if` is checked independently, so Python evaluates all of them.
# In this specific case, only ONE condition can be True (>, <, or ==),
# but Python will still check the remaining `if`s after printing.

if(num_1 > num_2):
    print(f"{num_1} is greater than {num_2}")
if(num_1 < num_2):
    print(f"{num_1} is smaller than {num_2}")
if(num_1 == num_2):
    print(f"{num_1} is equal to {num_2}")


