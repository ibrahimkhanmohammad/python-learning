''' Why functions are used in Python? 

  Functions let you package a piece of logic once and then reuse it by calling it with different inputs.
 
  Applications (where functions are used)

  Reuse repeated code, Organize programs, Build APIs, Automation/scripts
'''


#   basics of function
def add():  # defininga function named add() without passing any paarameter
    # block of code which is re-usable
    a = 4
    b = 5
    print(a * b)

#  prints 20
add()   # function call

add()    # function call

add()    # function call


# Task -1 
def welcome_message():
    print("Welcome to Python programming!")

welcome_message()     # funct is being called
welcome_message()
welcome_message()

# Task-2
def good_morning():
    print("Good Morning, Ibrahim!")

good_morning()
good_morning()

# Task-3
def inspire():
    print("As Long as I'm Alive, I have Infinite Chances.  :Ibrahim")

inspire()