num_1 = int(input("enter num 1: "))
num_2 = int(input("enter num 2: "))

# Here we use an `if / elif` chain.
# Python checks conditions from top to bottom and runs ONLY the first one that is True.
# After one block runs, the rest of the `elif`s are skipped.
# This is ideal when the conditions are mutually exclusive (>, <, ==).

if(num_1 > num_2):
    print(f"{num_1} is greater than {num_2}")
elif(num_1 < num_2):
    print(f"{num_1} is smaller than {num_2}")
elif(num_1 == num_2):
    print(f"{num_1} is equal to {num_2}")


