'''
Uzair Anjum
18/10/20022
purpose: Write a pay computation programme using functions:
'''

# Create a function called “check_continue” that allow the end user to exit the application if they do not wish to continue (quit) by entering Y/N (the function should handle the case sensitivity issue).



def check_continue():
    choice= input("would you like to continue:(Yes/No)").upper
    if choice == "NO":
        return quit


   
# Create a function called “check_numeric” to check that if the input is a numeric number, if not the function should ask the user to re-enter the number again and the cast/convert the input to int.
def check_numeric(a):

        try:
            a == int(a)
        except:
            print(("error, wrong formate please enter number again:"))
            
             
    



# Create a a function called "computepay" which takes two parameters (hours and rate) and if the rate is not provided the function will assumed that the default parameter rate is £10. Also, If the total number of working hours is more than 40 hours, the rate of the extra hours is 1.5 times of the normal rate.
def computepay (hours, rate="10"):
    hours=int(hours)
    rate=int(rate)
    if hours< 40:
        pay= (hours* rate)
    if hours > 40:
        extra_hr = (hours-40)*(rate*1.5)
        pay=hours*rate + extra_hr
    return pay

# In the main programme:

# Provide instructions to the end user explaining the purpose of the application.
print("this programe will help you calculate your pay")
# Check if the user wants to continue or not using check_continue function.
check_continue()

# Repeatedly prompts/asks a user to enter the working hours and rate (the rate is optional) until the user enters "done“, and in every iteration check the inputs using check_numeric functions and compute the pay using computepay function.

while True:
    hours= input(("please enter your hours:"))
    check_numeric(hours)
    hours= int(hours)
    rate= input("please enter your rate:")
    rate=int(rate)
    check_numeric(rate)
    choice= input("are you done?(yes/no)")
    if choice == "yes":
        break
    
pay=computepay(hours, rate)
print(pay)

    

# Once 'done' is entered, print the payment.
# Please use comments wherever is needed and use suitable variable names.
# Create an application to calculate sums of two fractional numeric values (floats).
