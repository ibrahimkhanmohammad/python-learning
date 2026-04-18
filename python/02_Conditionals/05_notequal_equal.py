# Read two integers from the user.
# int(...) converts the text from input() into a whole number.

num_1 = int(input("enter num 1: "))
num_2 = int(input("enter num 2: "))

# --- Example 1: using != (not equal) ---
# If the numbers are different, the condition is True.
# Otherwise (they are equal), Python runs the else block.
#
# Note: != checks "not equal". == checks "equal".

if num_1 != num_2:
    print(f"{num_1} and {num_2} are different")

else:
    print(f"{num_1} and {num_2} are same")

# --- Example 2: using == (equal) ---
# This is the SAME logic as Example 1, just written the opposite way:
# - First branch runs when they ARE equal
# - else runs when they are NOT equal
#
# Important: Python runs BOTH examples in this file, so you will see TWO prints.


if num_1 == num_2:
    print(f"{num_1} and {num_2} are same")

else:
    print(f"{num_1} and {num_2} are different")