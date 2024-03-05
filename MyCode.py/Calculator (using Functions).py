'''Uzair anjum
28/10/2022
purpose: make a calculator using funsions'''


# Create an application to calculate sums of two fractional numeric values (floats).
# The end user should be able to choose either addition, subtraction, division, multiplication, exponentiation and modulus.
def sum(a, b):
    result= a+b
    return print(result)

def sub(a, b):
    result=a-b
    return print(result)

def div(a, b):
    result=a/b
    return print(result)

def mult(a, b):
    result=a*b
    return print(result)

def exp(a, b):
    result= (a)**b
    return print(result)

while True:
    try:
        a=float(input("please enter the fist number:"))
        break
    except:
        a= input("wrong format, please enter number agaim:")

a= float(a)

operation= input("please choose +,-,x,/,exponentiation")

while True:
    try:
        b= float(input("please enter second number"))
        break
    except:
        print("wrong format, please enter number agaim:")

b=float(b)

if operation== "+":
    sum(a, b)
if operation=="-":
    sub(a, b)
if operation=="x":
    mult(a, b)
if operation=="/":
    div(a,b)
if operation=="exponentiation":
    exp(a, b)










