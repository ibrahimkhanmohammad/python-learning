# 🔹 STRINGS:
# A string is a sequence of characters (text)
# Written inside quotes: " " or ' '
# Example:
name = "Ibrahim"

# IMPORTANT:
# Strings are IMMUTABLE → cannot be changed after creation

# ❌ Not allowed (will give error):
# name[0] = "A"

# ✅ Instead, create a new string:
name = "A" + name[1:]

print(name)

# 🔹 VARIABLES:
# Variables are containers to store data

name = "strings"

# 🔹 COMMENTS:
# Comments are used to explain code
# Python ignores them during execution


# Print statement
print("Hello, World")   # prints text to output


# 🔹 ESCAPE SEQUENCE '\':
# Used for special characters
print("This is a backslash: \\")


# 🔹 ESCAPE SEQUENCE '\n':
# New line
print("Hello\nWorld")


# 🔹 ESCAPE SEQUENCE '\t':
# Tab space
print("Hello\tWorld")