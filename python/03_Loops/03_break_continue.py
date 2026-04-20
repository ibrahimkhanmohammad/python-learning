# =============================================================================
# break  — exit the nearest enclosing loop immediately
# continue — skip the rest of the current iteration; go back to the loop check
# =============================================================================
# This pattern asks for a number until it is positive, then uses it.

while True:  # loop "forever" until we explicitly break out
    n = int(input("enter n "))

    if n <= 0:
        # Invalid: do not leave the loop — ask again from the top.
        continue

    else:
        # Valid positive n: stop asking and run the code after this while-loop.
        break

# =============================================================================
# Use n (must be > 0 here because we only broke out when n was positive)
# =============================================================================
# _ is a normal variable name; by convention it means "I don't use this value."
# range(n) still runs n times (0 .. n-1 internally; we only care about the count).

for _ in range(n):
    print("meow")