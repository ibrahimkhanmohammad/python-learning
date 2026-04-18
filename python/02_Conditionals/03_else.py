num_1 = int(input("enter num 1: "))
num_2 = int(input("enter num 2: "))


# `else` is the "default" branch.
# It runs only if all previous conditions were False.
# Here, if num_1 is not greater and not smaller than num_2,
# the only remaining possibility is that they are equal.


if(num_1 > num_2):
    print(f"{num_1} is greater than {num_2}")
elif(num_1 < num_2):
    print(f"{num_1} is smaller than {num_2}")
else:
    print(f"{num_1} is equal to {num_2}")


