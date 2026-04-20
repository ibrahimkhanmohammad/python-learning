message = "Hello"

# Core Cpncept: [start : end : step]

# [:] → full slice → returns entire string
print(message[:])        # "Hello"


# [0] → index 0 → first character
print(message[0])        # "H"


# [:4] → from start (0) to index 4 (exclusive)
print(message[:4])       # "Hell"


# [::2] → step = 2 → take every 2nd character
print(message[::2])      # "Hlo"


# [-1] → last character
print(message[-1])       # "o"


# [-5:] → from index -5 to end
# -5 = start of string here
print(message[-5:])      # "Hello"


# [-4:-1] → from index -4 to -1 (exclusive)
# -4 = "e", -1 excluded ("o")
print(message[-4:-1])    # "ell"


# [::-1] → reverse string
# step = -1 → go backwards
print(message[::-1])     # "olleH"