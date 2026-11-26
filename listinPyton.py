'''
List is a inbuilt data type in python that allow us to store a multiple element in single
variable.
        list is created by using square bracket [] and seprated element by coma ,
Example of making list.
'''
student=["Mohamad Aslam","Amrit Swar","Sabindra parajuli","Aashiq Habib","Mobish Pokhrel"]
print(student)

# ====== Characterstick of list
# 1. Ordered: list maintain the order of element in list, Eash element have specific postion
# 2. Mutable: meain it allow us to modify, remove, add, after create list.
# 3. Allow different data type
# 4. Allow dublication
# 5. Allow Nested list: A list contain another list as element
    # Example:
student1=[["Mohamad Aslam",20],["Amrit Swar",21]]
# -------------------------------------------------------
# ===== List indexing
'''is use to extract the particular element form the list 
there are to method to extract the element
1. Using positive indexing: Start form 0 
2. Using negetive indexing: Start form -1
'''
# Example
print(student[2])
# (Here we extract the 2nd position element)

# --------------------------------------------------------
# =====String slicing
''' is use to extart the partcular portion from list
student[star:end:skip]
this structure is use to extract the particular portion form string
'''
# Example
print(student[1:4:2])
# ------------------------------------------------------
# =========Quick Revision: Python List Cheat Sheet
'''Keep this table as a quick reference when programming.
Task	                   Syntax
Create list	                a = [10, 20, 30]
Access element	            a[0]
Negative indexing	        a[-1]
Slice list	                a[1:3]
Change element	            a[0] = 100
Add element	                a.append(40)
Insert element	            a.insert(1, 15)
Add multiple elements	    a.extend([40,50])
Remove element	            a.remove(20)
Remove by index	            a.pop(0)
Empty list	                a.clear()
Find length	                len(a)
Find maximum	            max(a)
Find minimum	            min(a)
Find sum	                sum(a)
Sort list	                a.sort()
Reverse list	            a.reverse()
Count element	            a.count(10)
Find index	                a.index(20)
Copy list	                a.copy()
'''
# ------------------------------------------------------

# =======Practice Questions
# Try solving these questions yourself. They will help you understand lists practically.

# Q1. Create a list containing five different numbers and print it.
studentMark=[55,60,58,47,53]
print("Here the mark of 5 student: ",studentMark)


# Q2. Print the first and last elements of a list.
numbers = [10, 20, 30, 40, 50]
print("The first element of list is: ",numbers[0])
print("The last element of list is: ",numbers[-1])



# Q3. Add 60 at the end of a list.
numbers1=[40,30,70,45]
numbers1.append(60)
print(numbers1)


# Q4. Remove the element 30 from a list.
numbers1.remove(30)
print("the 30 is remove form the list: ",numbers1)


# Q5. Find the sum and average of list elements.
print("Theu sum of list is: ",sum(numbers1))
print("The average of list is: ",sum(numbers1)/len(numbers1))