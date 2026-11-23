# ======Short introduction==========
# Python is powerful high level, interpreted, general purpose programming
# language, invet by Guido Van Rossum and first released on 1991 in Neatherland.
# Mainly kwon for its prtabilyty, flexibility and extensive library support,
# widly used in web development, machine learning, automation, data anylytic
# and many more.  

# ____First hello world program
print("Hello! World")
#=========== Variable===========
# Variable in a Python is name refer to object sotored in a memory. It is use to
# access, identify and manipulating data during program execution.
# in simple its allocate the storage from our secondary memory(RAM) to store the data.

# In python variable are commonly discussed in two different way:
# 1. Bsed on its scope and uses
# 2. Based on data type and object refer to.

# _______ 1. Bsed on its scope and uses
# .......Local variable:-
#        is declare inside function, can be only accessible within
#        that function scope and inside that function.
# example
def Student():
    name="Aslam"
    print(name)

Student()

# .......Global variable:-
#        is declare outside all function and can be accessed from different part of module
# Example
college="Mega college"
def insitute():
    print(college)

insitute()
