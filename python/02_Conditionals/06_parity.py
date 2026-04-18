# =============================================================================
# CONTEXT (read this first)
# This file demonstrates TWO ways to check if an integer is even or odd.
#
# Part A (top): "script style" — quick and direct, good for tiny examples.
# Part B (below): "function style" — splits logic into reusable pieces; closer
# to how real programs are organized (helper + main entry point).
#
# NOTE: As written, running this file asks for input TWICE (Part A runs first,
# then main() runs). That's fine for learning; for a single demo, keep only one.
# =============================================================================

# -----------------------------------------------------------------------------
# Part A — Inline check (no functions)
# What it does:
# - Reads an integer from the user.
# - Uses modulo (%) to test divisibility by 2:
#     num % 2 == 0  → even
#     otherwise     → odd
# - Prints a message immediately.
# Why it exists:
# - Shows the core idea in the smallest amount of code.
# -----------------------------------------------------------------------------

num = int(input("enter num: "))

if num % 2 == 0:
    print(f"{num} is an even number")

else:
    print(f"{num} is an odd number")


# -----------------------------------------------------------------------------
# Part B — Function style: main() + is_even()
# What it does:
# - main() controls the program flow: input → decision → output.
# - is_even(n) is a reusable "rule" that returns True/False.
#
# How the call works:
# - When main runs `if is_even(nums):`, Python first evaluates is_even(nums).
# - is_even returns a boolean, and if/else chooses which print to run.
#
# Why it exists:
# - Reusable: you can call is_even(...) anywhere, not only in one if-block.
# - Readable: `if is_even(num)` reads like English.
# - Easier to extend later (more checks, tests, or multiple callers).
# -----------------------------------------------------------------------------

def main():
    nums = int(input("enter num: "))
    if is_even(nums):
        print(f"{nums} is even")
    else:
        print(f"{nums} is odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Start the "function-style" program (this runs after Part A already executed).
main()