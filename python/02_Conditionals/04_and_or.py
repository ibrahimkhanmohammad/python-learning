num_1 = int(input("enter num 1: "))
num_2 = int(input("enter num 2: "))


# `or` combines two boolean checks.
# Here, (num_1 > num_2) OR (num_1 < num_2) is True whenever the numbers are different.
# If they are the same, both checks are False, so we go to `else` (equal case).

if(num_1 > num_2) or (num_1 < num_2):
    print(f"{num_1} and {num_2} are not equal.")

else:
    print(f"{num_1} and {num_2} are equal.")



# Special case: if num_1 is negative and smaller, print a specific message.

# `and` requires BOTH conditions to be True.
# If the first condition is False, Python skips checking the second (short-circuit).

if num_1 < num_2 and num_1 < 0:
    print(f"{num_2} is greater than {num_1}")
elif num_1 < num_2:
    print(f"{num_1} is smaller than {num_2}")
elif num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
else:
    print(f"{num_1} and {num_2} are equal")