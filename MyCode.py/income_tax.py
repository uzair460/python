"""
Name: Uzair Anjum
Date: 20220930
Purpose: income tax calculator 
 
"""

# Output purpose of program
print('''
this programe will help you calculate:
tax rate based on salary,
taxable income after personal allowance,
and your tax ''')
#give user a choice to quit progarame 
choice= (input("would you like to coninue:(Y/N)"))
if choice== "N":
    quit
    #store value
salary= float(input("please enter your salary:"))

if salary <= 12570:
    print ('''your tax rate is: 0%
    your taxable income after alowence is: £0
    your tax is £0
    ''')
elif salary >12570 and salary<= 50270:
    tax_rate= 20
    t_after_al= (salary-12570)
    tax= float(t_after_al/tax_rate)*100
    print(f'''
    your tax rate is: {tax_rate}%
    your taxable income after alowence is:{t_after_al}
    your tax: {tax}'''
    )
elif salary >50270 and salary <= 150000:
    tax_rate= 40
    t_after_al=(salary-12570)
    tax= float(t_after_al/tax_rate)*100
    print(f'''
    your tax rate is: {tax_rate}%
    your taxable income after alowence is:{t_after_al}
    your tax: {tax}'''
    )
elif salary >150000:
    tax_rate=45
    t_after_al=(salary-12570)
    tax= float(t_after_al/tax_rate)*100
    print(f'''
    your tax rate is: {tax_rate}%
    your taxable income after alowence is:{t_after_al}
    your tax: {tax}''')





