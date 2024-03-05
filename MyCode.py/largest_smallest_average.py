'''
Uzair Anjum
10/10/2022
pursopse: print the largest, smaller and average number
'''
#Provide instructions to the end user explaining the purpose of the application.
print("this programe will help you show the average,largest and smallest number based on your marks.")

#Allow the user to exit the application if they do not wish to continue (quit)
choice= print(input("would you like to continue?(Yes/No)"))
if choice == ("NO"):
    print("goodbey")
    quit
#Repeatedly prompts/asks a user for his/her marks in various modules until the user enters "done"
largest = None
smallest = None
count = 0
sum = 0
while True:
    marks = input("Enter your mark: ")
    #Once 'done' is entered, print out the largest mark, the smallest mark, and the average of all marks.
    if marks == 'done':
        break
    #Handle the error. If the user enters anything other than a valid number, catch it with a try/except and put out an appropriate message and ignore the number.
    try:
        marks= int(marks)
    except:
        print('Invalid input, please try again')
        continue
    if largest is None or largest < marks:
        largest = marks
    elif smallest is None or smallest > marks:
        smallest = marks
    elif marks < smallest:
        smallest = marks


    count = count + 1
    sum = sum + marks  
    average = sum/count
    
print(f"your largest marks is:{largest}")
print(f"your smallest mark is:{smallest}")
print(f"your avaerge is:{average}")

