# =============================================================================
# for loops — repeat once per item in a sequence
# =============================================================================
#   for <name> in <iterable>:
#       ... block ...
#
# Each time through, <name> is bound to the next value from the iterable, and
# the block runs. When there are no more values, the loop ends.
#
# A literal list works for a few steps, but for "do this N times" you usually
# use range(...) instead of typing [1, 2, 3, ..., 10000].

# Example with a small list (same idea as three separate prints):

# for i in [1, 2, 3]:
#     print("meow")

# =============================================================================
# range — counts for you (no huge list in source code)
# =============================================================================
# range(n) yields 0, 1, ..., n-1  →  n iterations.
# So range(5) runs the loop body five times; the variable i is 0..4 if you use it.
#
# (Running below plus the string example prints 5 + 3 lines; comment one out if you want.)

for i in range(5):
    print("meow")

# =============================================================================
# Another style — repeat a string (only when one print with newlines is OK)
# =============================================================================
# Multiplying a string by k repeats it k times. "meow \n" * 3 is three lines.
# end="" avoids an extra blank line after print (default end is newline).

print("meow \n" * 3, end="")
