'''
============ String in python=============
A string is a data type in python use to write or manuplate a text, name, address, 
sentence and number as a text.

------there is three wah to write a string in a python
..using triple quotes (''' ''')
..using double quotes (" ")
.. using single quotes (' ')

------- String indexing
is use to access a indivusual text from string using its postion
The two type indexing in python
1. positive indexing: start from 0 not 1
    example:    p y t h o n
                0 1 2 3 4 5
2. negetive indexing : start form -1
    example:    p    y    t    h    o    n
                -6  -5   -4   -3   -2   -1

------- string slicing
mean accessing a partcular portion from a string.
structure of string slicing
name[start:end:step]
. start mean start from postion
. end mean on postion
. stem mean move forward step
    example 1
    varname = "Mohamad Aslam"
    print(varname[1:4])
output:
    oham
(Here its extract a particula portion from string)

    example 2:
    print(varname[1:6:2])
output:
    oaa
(here its start with postion 1(o) to 6(d) and step forwar 2 position )

-------String concatenation and repetition
These are operation use to concatenate or repeat string
A. Concatenation (+): + operator is use to concatenate the string, normally its help us to add 
two string
    exaple:
    var1="Mohamad"
    var2= "Aslam"
    print(var1 + var2)
Output:
MohamadAslam
(Here the + operator is use to concatenate the two string data type variable)

B. Repeat (*): * operator is use to repeat the string
    example:
    print(var1 *3)
Output:
MohamadMohamadMohamad
(Here the string is repeting three times)

---------6. Most commonly used Python string functions and methods
This is one of the most important parts of learning strings.

First, understand the difference:
- A function is a built-in operation that can work with different types of data.
- A method is an operation associated with an object, called using dot notation.

Here is a compact reference table you can use while coding.
Method/function	        Purpose
len()	                Count characters
upper()	                Convert to uppercase
lower()	                Convert to lowercase
capitalize()	        Capitalize first character
title()	                Capitalize each word
swapcase()	            Reverse letter cases
find()	                Find substring position
index()	                Find position or raise error
count()	                Count occurrences
replace()	            Replace text
split()	                Convert string into a list
join()	                Join list elements
strip()	                Remove surrounding whitespace
startswith()        	Check beginning
endswith()          	Check ending
isdigit()	            Check digits
isalpha()	            Check alphabetic characters
isalnum()	            Check letters and numbers
format()	            Insert values into a string

8. Escape characters in Python strings
Escape characters allow you to include special formatting or characters inside a string.
Escape character	Purpose
# \n	New line
# \t	Horizontal tab
# \\	Backslash
# \'	Single quotation mark
# \"	Double quotation mark

'''
# crerating string data type variable
FirstName="Mohamad"
LastName="Aslam"
Address="Chandrapur-4,Rautahat"
# printing the string variable
print("I love Python")

# =========practice

# Question 1. Convert the following string into uppercase.
# text = "python programming"
a="python programming"
print(a.upper())



# Question 2. Find the total number of characters in the given string.
# text = "Hello World"
text="Hello World"
print(len(text))



# Question 3. Extract the word Python using slicing.
# text = "I love Python"
text1= "I Love Python"
print(text1[-1:6])



# Question 4. Replace Java with Python.
# text = "I am learning Java"

text2 = "I am learning Java"
print(text2.replace("Java", "Python"))



# Question 5. Count how many times the letter a appears.
# text = "banana"
text3 = "Banana"
print(text3.count("a"))