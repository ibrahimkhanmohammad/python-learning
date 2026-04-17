name = input("Enter your Name: ")


#   Removes white spaces
name = name.strip()

#   uppercase the first character of the whole string, and lowercase the rest.
name = name.capitalize()
print(f"Hello, {name}")  #  f-strings

#    title() capitalizes the first letter of each word (with some rules for apostrophes, etc.). and also indeed in simple terms it means captalize every letter
name = name.title()
print(f"Hello, {name}")

#   We can chain string methods like this:
names = input("Enter your Name: ").strip().capitalize()
print(f"Hello, {names}")