'''Uzair Anjum
08/11/2022
purpose:make a database
Course / Programme: 	BEng Software Engineering 
BSc Computing 
Module name and code: 	Computer Science Fundamentals (SWE4207) 
Student ID 	 2204968
Tutor:  	Francis Morrissey 
Dr Mohammed Benmubarak 
Aamir Abbas 
'''
import sqlite3
import bcrypt
import getpass
from tabulate import tabulate

conn= sqlite3.connect('swe4207.db')
cur = conn.cursor()

def create_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS user (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS customer (
        customerid INTEGER PRIMARY KEY AUTOINCREMENT,
        forename TEXT NOT NULL
        ,surname TEXT,
        dob TEXT NOT NULL)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS address (
        addressid INTEGER PRIMARY KEY AUTOINCREMENT,
        streetnumber TEXT,
        firstline TEXT NOT NULL,
        postcode TEXT,
        region TEXT NOT NULL,
        country TEXT NOT NULL,
        customerid INTEGER NOT NULL,
        FOREIGN KEY(customerid) REFERENCES customer(customerid))''')

    cur.execute('''CREATE TABLE IF NOT EXISTS account (
        accountid INTEGER PRIMARY KEY AUTOINCREMENT,
        balance REAL NOT NULL,
        opendate TEXT NOT NULL,
        closedate TEXT,
        status TEXT NOT NULL DEFAULT "ACTIVE",
        customerid INTEGER NOT NULL,
        FOREIGN KEY(customerid) REFERENCES customer(customerid))''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS transact (
        transactid INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        type TEXT NOT NULL,
        date TEXT NOT NULL,
        accountid INTEGER NOT NULL,
        FOREIGN KEY(accountid)REFERENCES account(accountid))''')



    conn.commit

create_table()

def try_str(str1):
    try:
        str(str1)
    except:
        print("wrong formate try again")
        main_menu()




def hash_password(plain_password:str):
    """Hashandreturnuser_password"""
    salt=bcrypt.gensalt()
    hashed_passsword=bcrypt.hashpw(plain_password,salt)
    return hashed_passsword

def registrasion():
    user_name = input("please enter a user name: ")
    cur.execute('SELECT* FROM user where username=?',(user_name,))
    result=cur.fetchall()
    for x in result:
        x= result[0][0]
        print (x)
        if user_name == x:
            print("user name alredy in use, please try again")
            registrasion()
    else:
        user_name=user_name.lower().strip()
        plain_pasword= getpass.getpass('please enter a pasword:').lower().encode('utf-8').strip()
        user_pasword= hash_password(plain_pasword)
        cur.execute('INSERT INTO user VALUES (?,?)',(user_name,user_pasword),)
        conn.commit()
        login_menu()
        return

def login_menu():
    choice=input('''please select what would you like to do:
    1) registrasion 
    2) log in
    ''')
    if choice == '1':
        registrasion()
    elif choice== '2':
        input_user_name= input("please enter your user name:").lower().strip()
        password_to_check= getpass.getpass("Enter password for user:").strip().lower().encode('utf-8')
        cur.execute('SELECT password FROM user WHERE username = ?',(input_user_name,))
        result= cur.fetchall()
        fetched_password= result[0][0]
        while True:
            if bcrypt.checkpw(password_to_check,fetched_password):
                main_menu()
            else:
                print("Record not found. Possibly incorrect email or password.")
                login_menu()


def main_menu():
    choice=input('''please enter what would you like to do:
    1)search customers 
    2)add new customer
    3)transactions menu
    4)open accounts
    5)close account
    6)view all accounts
    7)delete customers
    8)update customers
    9)all customers
    10)search accounts
    11)delete accounts
    ''')
    
    if choice== '1':
        search_customer=input('''please enter surname, forname or customer id:''')
        cur.execute('SELECT * FROM customer  WHERE forename=? OR customerid=? OR surname=?',(search_customer,search_customer,search_customer))
        result= cur.fetchall()
        print(result)
        print(tabulate(result, headers=["customer id","forename","suname","DOB"],tablefmt="fancy_grid"))
        main_menu()
    elif choice =='2':
        forname=input("please add forname:")
        surname=input('please add surname:')
        dob=input('please add date of birth:')
        street_number=input('please enter street number:')
        first_line=input('please enter your firstline:')
        postcode=input("please enter your post code:")
        region =input("please enter your region:")
        country=input("please enter your country")
        cur.execute('INSERT INTO customer (forename, surname, dob) VALUES (?,?,?)',(forname,surname,dob))
        conn.commit()
        cur.execute('SELECT customerid FROM customer WHERE forename=? AND surname=? AND dob=?',(forname,surname,dob))
        result=cur.fetchall()
        customer_id=result[0][0] 
        cur.execute("INSERT INTO address (streetnumber, firstline, postcode, region, country, customerid) VALUES (?,?,?,?,?,?)",(street_number,first_line,postcode,region,country,customer_id))
        conn.commit()
        main_menu()
    elif choice=='3':
        choice2=input('''
        1)add a new transaction
        2)would you like all the transacsin
        3)search transaction of customer
        4)transaction of a date
        5)delete transaction
        ''')
        if choice2=='1':
            amount=input("please enter amount")
            type=input("please enter type")
            date= input("please enter date")
            account=input("please enter account id:")
            cur.execute('INSERT INTO transact(amount, type, date, accountid) VALUES(?,?,?,?)',(amount,type,date,account))
            conn.commit()
            main_menu()

        elif choice2== "2":
            cur.execute('SELECT transactid,amount,type,date,accountid FROM transact')
            result=cur.fetchall()
            print(tabulate(result, headers=["transaction id","amount","type","date","accountid"],tablefmt="fancy_grid"))
            main_menu()
        elif choice2=='3':
            customer_id=input('please enter account id:')
            cur.execute('SELECT transactid,amount,date FROM transact WHERE accountid=?',(customer_id,))
            result=cur.fetchall()
            print(tabulate(result, headers=["transaction id","amount","date"],tablefmt="fancy_grid"))
            main_menu()
        elif choice2=='4':
            date2=input('please enter date:')
            cur.execute('SELECT transactid,amount,accountid FROM transact WHERE date=?',(date2,))
            result=cur.fetchall()
            print(tabulate(result, headers=["transaction id","amount","account id"],tablefmt="fancy_grid"))
            main_menu()
        elif choice2=='5':
            transaction_id=input("please enter transaction id:")
            cur.execute("DELETE FROM transact WHERE transactid=? ",(transaction_id))
            conn.commit()
            print("done")
            main_menu()

    elif choice== "4":
        balance= input("please enter balance:")
        opendate=input("please enter open date:")
        customer_id_input=input("please enter customer id, forename or surname:")
        cur.execute('SELECT customerid FROM customer WHERE customerid=? OR surname=? OR forename=?',(customer_id_input,customer_id_input,customer_id_input))
        result=cur.fetchall()
        print(result)
        customer_id=result[0][0] 
        cur.execute('INSERT INTO account(balance,opendate,customerid) VALUES(?,?,?)',(balance,opendate,customer_id))
        conn.commit()
        main_menu()

    elif choice=='5':
        search_account3=input("please enter account id:")
        date1=input("please enter date:")
        cur.execute('UPDATE account SET closedate=? WHERE accountid=?', (date1,search_account3))
        cur.execute(' UPDATE account SET status = "closed" WHERE accountid=?', (search_account3,))
        conn.commit()
        main_menu()

    elif choice=="6":
        cur.execute('SELECT accountid, balance,opendate, closedate, status, customerid FROM account')
        result=cur.fetchall()
        print(tabulate(result, headers=["account id","balance","opendate","closedate","status","customer id"],tablefmt="fancy_grid"))
        main_menu()

    elif choice=="7":
        input_delete=input("please enter customer id, forname or surname:")
        ask= input("are you sure?(yes/no)").strip().lower()
        try_str(ask)
        if ask == "yes":
            cur.execute('DELETE FROM customer WHERE forename=? OR surname=? OR customerid=?',(input_delete,input_delete,input_delete))
            conn.commit()
            main_menu()
        else:
            main_menu()

    elif choice=="8":
        choice_update=input('''please select what would you like to update:
        1)update forename
        2)surname
        3)dob
         ''')
        search_customer=input('''please enter surname, forname or customer id of customer:''')
        if choice_update=="1":
            new_forename=input("please enter new forename:")
            cur.execute('UPDATE customer SET forename=? WHERE forename=? OR customerid=? OR surname=?',(new_forename,search_customer,search_customer,search_customer))
            conn.commit()
            main_menu()
        elif choice_update=="2":
            new_surname=input("please enter new surname:")
            cur.execute('UPDATE customer SET surname=? WHERE forename=? OR customerid=? OR surname=?',(new_surname,search_customer,search_customer,search_customer))
            conn.commit()
            main_menu()
        elif choice_update=="3":
            new_dob=input("please enter new dob:")
            cur.execute('UPDATE customer SET dob=? WHERE forename=? OR customerid=? OR surname=?',(new_dob,search_customer,search_customer,search_customer))
            conn.commit()
            main_menu()


    if choice=="9":
        cur.execute('select*from customer INNER JOIN address ON customer.customerid = address.customerid')
        result=cur.fetchall()
        print(tabulate(result, headers=["customer id","fist name","last name","dob","adress id","street n.","street name","post code","city","country",""],tablefmt="fancy_grid"))
        main_menu()

    if choice=="10":
        customer_id_input=input("please enter customer id, forename or surname:")
        cur.execute('SELECT customerid FROM customer WHERE customerid=? OR surname=? OR forename=?',(customer_id_input,customer_id_input,customer_id_input))
        result=cur.fetchall()
        customer_id=result[0][0]
        cur.execute('SELECT accountid, balance, status, forename, surname from account INNER JOIN customer ON account.customerid= customer.customerid WHERE account.customerid=?',(customer_id,))
        result=cur.fetchall()
        print(tabulate(result, headers=["account id","balance","status","name","surname"],tablefmt="fancy_grid"))
        main_menu()

    if choice=="11":
        search_account4=input("please enter account id:")
        cur.execute("DELETE FROM account WHERE accountid=?",(search_account4,))
        conn.commit()
        print("done")
        main_menu()


login_menu()
        
main_menu()
            
