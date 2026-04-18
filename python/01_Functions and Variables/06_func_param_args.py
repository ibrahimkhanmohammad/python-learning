'''1. Parameters (in the def): 

Parameters are the variables inside the parentheses when you define a function.

def add(a, b):   # a and b are parameters'''


'''2. Arguments (in the call):

Arguments are the real values you pass when calling the function.

add(2, 3)        # 2 and 3 are arguments'''


#  funct definition with parameters a, b
def avearage_val(a, b):
    avearage_val_val = (a + b)/2
    print(avearage_val_val)


# # funct calling with arguments passing

# avearage_val(2, 3)        # print 2.5
# avearage_val(4, 9)        # print 6.5
# avearage_val(58, 75)      # print 66.5
# avearage_val(84, 2500)    # print 1292.0
# avearage_val()            # print error because no arguments passed => so in this case we by-default define the default arguments inside parameters and if so any arguments later not called by funct then the deafult one's will be operated 


# eg:

def avearage_val(a=10, b=20):    # function defining with parametrs by default arguments
    avearage_val_value=(a+b)/2
    print(avearage_val_value)

avearage_val(2, 4)       # prints the avearage_val of 2, 4
avearage_val(54, 85)     # prints the avearage_val of 54, 85
avearage_val()           # prints the avearage_val of  10, 20 as there are no arguments called by function


# Task -1

def show_age(name="Ibrahim", age=19):
    print(f"{name} is {age} years old.")

show_age("Ibrahim", 19)
show_age()              # in this case the default arguments passed in parameters will be print instead of error
show_age("khan", 50)    # the deafult arguments will be over-write by the arguments which are being known as Calling functions

# Task -2

def fav_food(name, food):
    print(f"{name} loves {food}")

fav_food("Ibrahim", "Ice-Cream")