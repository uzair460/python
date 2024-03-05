'''
Uzair Anjum
21/11/22
purpose: shape calculator
'''

def choice():
    choice1=input('''this progame will help you calculate the surface of a chosen shape.
    would you like to continue?(yes/no)''').lower
    if choice1== 'no':
        return quit

def check_int(a):
    while True:
        try:
            a == int(a)
            break
        except:
            a=input("wrogn formate try again")
            return a

def check_str(a):
    while True:
        try:
            a == str(a)
            break
        except:
            a=input("wrogn formate try again")
            return a



def trapezoid():
    b1=int(input("please enter base:"))
    check_int(b1)
    b2= int(input("please enter the second base:"))
    check_int(b2)
    h= int(input("please enter hight:"))
    check_int(h)
    surface = b1+b2/2*h 
    return print(f"the surface area is {surface}")

def paralelegram():
    b= int(input("please enter base:"))
    check_int(b)
    h= int(input("please enter the hight:"))
    check_int(h)
    surface= b*h
    return print(f"the surface area is {surface}")

def rectagle():
    b= int(input("please enter base:"))
    check_int(b)
    h= int(input("please enter the hight:"))
    check_int(h)
    surface= b*h
    return print(f"the surface area is {surface}")

def circle():
    r= int(input("please enter the rediuce:"))
    check_int(r)
    surface= 3.14* r**2
    return print(f"the surface area is {surface}")



def shape_choice():
    shape= input("please choose a shape:")
    check_str(shape)
    if shape== "trapezoid":
        return trapezoid()
    elif shape== "paralelegram":
        return paralelegram()
    elif shape== "rectagle":
        return rectagle()
    elif shape== "circle":
        return circle()
    
choice()
shape_choice()







