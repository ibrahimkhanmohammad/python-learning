# Compare two styles: classic if/else vs Python 3.10+ match/case

name = input("enter any country name: ").strip()

# if / or chain (CORRECT version)
# Each comparison must involve `name`, like:
#   name == "India" or name == "Japan" ...
# WRONG version people sometimes write:
#   if name == "India" or "Japan" or "Palestine":
# because `"Japan"` is a non-empty string and is always "truthy", so the condition
# can become misleading / always True.

if name == "India" or name == "Japan" or name == "Palestine":
    print("Good!")
else:
    print("check once!")

# Same idea using `match` (requires Python 3.10+)
# `case "A" | "B"` means: match A OR B
# `case _:` is the default branch (like `else`)

country_name = input("enter the name: ").strip()

match country_name:
    case "India" | "Japan" | "Palestine":
        print("Good!")
    case _:
        print("check once!")

