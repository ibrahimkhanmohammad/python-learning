greet = "Hello"
message = "World"
name = " Hello, World "

# ==============================
# 🔹 BASIC STRING METHODS
# ==============================

print(greet.upper())        # upper() → converts to uppercase → HELLO
print(message.lower())      # lower() → converts to lowercase → world
print(greet.title())        # title() → capitalizes each word → Hello
print(message.capitalize()) # capitalize() → only first letter → World

print(message.count('o'))   # count() → counts occurrences → 1
print(greet.count('g'))     # case-sensitive → 0

print(greet.find('o'))      # find() → index of 'o' → 4
print(message.find('i'))    # returns -1 if not found (no error)

print(message.replace('World', 'Universe'))  # replace() → Universe

# ==============================
# 🔹 CLEANING & FORMATTING
# ==============================

print(name.strip())         # strip() → removes spaces → "Hello, World"
print(name.split())         # split() → string → list → ['Hello,', 'World']

print(name.startswith('H')) # False → because of leading space
print(name.endswith(' '))   # True → ends with space

# ==============================
# 🔥 METHOD CHAINING (IMPORTANT)
# ==============================

print(name.strip().upper())            # "HELLO, WORLD"
print(name.strip().startswith('H'))    # True

# chaining = applying multiple methods in one line (very important in backend)

# ==============================
# 🔥 REAL USE CASE (IMPORTANT)
# ==============================

user_input = "   Ibrahim Khan   "

# Clean input: remove spaces → lowercase → replace spaces with _
clean = user_input.strip().lower().replace(" ", "_")
print(clean)   # ibrahim_khan

# ==============================
# 🔹 SPLIT + JOIN COMBO (POWER TRICK)
# ==============================

text = "hello world python"

# split → ['hello','world','python']
# join → combine with '-'
result = "-".join(text.split())
print(result)   # hello-world-python

# ==============================
# 🧠 IMPORTANT NOTES
# ==============================

# 1. Strings are IMMUTABLE ❗
#    → methods DO NOT change original string
temp = greet.upper()
print(greet)   # still "Hello"

# 2. find() returns -1 if not found (safe)
# 3. count() is case-sensitive
# 4. strip() is heavily used in user input/backend

# ==============================
# ⚡ MINI CHEAT SHEET
# ==============================

s = " Hello World "

s.upper()          # HELLO WORLD
s.lower()          # hello world
s.title()          # Hello World
s.capitalize()     # Hello world

s.find("o")        # index or -1
s.count("o")       # count occurrences

s.replace("World", "Python")

s.strip()          # remove spaces
s.split()          # string → list
" ".join(["Hello","World"])  # list → string

s.startswith("H")
s.endswith("d")