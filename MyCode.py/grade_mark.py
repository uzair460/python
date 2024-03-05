"""
Name: Uzair Anjum
Date: 20220930
Purpose: Provide Letter grade based on mark
 
"""

# Output purpose of program
from operator import and_


def new_func():
    return ("provide letter grade based on marks")

outout: new_func()

# Ask user if they would like to continue
choice = input("would you like to continue (yes/no)")
if (choice=="no"):
    print("goodbey")
    quit
else: print("what are your marks")
student_marks= float(input())
if (student_marks<40):
    F= print("sorry you have failed")
    print (F)
    quit
elif(student_marks>=40 and student_marks<=49):
    D= print("good job, you got D")
    print(D)
elif(student_marks>=50 and student_marks<=59):
    C= ("great job, you got C")
    print(C)
elif(student_marks>=60 and student_marks<=69):
    B= ('great job, you got B')
    print(B)
elif(student_marks>=70):
    A= ('great job, you have A')
    print(A)





# Print "Goodbye" and quit if user indicates no
# Ask user for mark
# Store in variable and cast as integer
# If mark is less than 40 print F

# Else if mark is between 40 and 50 print D

# Else if mark is between 40 and 50 print C
# Else if mark is between 40 and 50 print B
# Else print A
