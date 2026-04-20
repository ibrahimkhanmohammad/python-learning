# =============================================================================
# Repeating actions
# =============================================================================
# You *could* print three times by repeating the same line (works, but does not
# scale to 100 or 500 times — use a loop instead):

# print("meow")
# print("meow")
# print("meow")

# =============================================================================
# while loop — what it does
# =============================================================================
#   while <condition>:
#       ... indented block ...
#
# Each time: if <condition> is True, Python runs the block, then checks again.
# If <condition> becomes False, Python skips the block and continues below.
# The block must eventually make the condition False (e.g. change a counter),
# or the loop never stops (infinite loop).
#
# This file runs *both* examples below, so you will see six "meow" lines.
# Comment out one block if you only want to try the other.

# =============================================================================
# Method 1 — count down: i goes 3 → 2 → 1 → 0, then stop
# =============================================================================
i = 3  # number of iterations left

while i != 0:  # repeat while i is not zero
    print("meow")
    i -= 1  # decrease i so we eventually reach 0 and exit the loop

# =============================================================================
# Method 2 — count up: j goes 0 → 1 → 2 → 3, stop when j is 3
# =============================================================================
j = 0  # how many times we have printed so far

while j < 3:  # repeat while j is less than 3 (so j = 0, 1, 2 runs three times)
    print("meow")
    j += 1  # increase j so we eventually reach 3 and exit the loop
