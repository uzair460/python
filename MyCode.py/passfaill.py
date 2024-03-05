#name: Uzair Anjum
#date: 30/09/2022
#purpose: practice with selection to check if user passed 

#output porpose of the program 
#ask user if theu would like to continue 
#ask use to enter marks(0-100)
#store marks in variable
#check if marks are less then 40
#if less then 40 print fail
#else print message pas

from secrets import choice


print ("this progrograme will be used to check if student passed or failed based on marks")
choice = input("would you like to continue? (Y/N)")
if (choice == "N"):
    quit
else: print('please enter mark')
student_mark = float(input())
if (student_mark>40):
    print('you have passed the module')
else:
    print('sorry you have failed ')


