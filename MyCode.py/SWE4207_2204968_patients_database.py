'''Uzair Anjum
08/11/2022
purpose:make a database'''
import sqlite3

conn= sqlite3.connect('M:\DBEVERS_MSQLlite\patients_databse.db')
cur = conn.cursor()

# Using Python, write a programme to do the following:
# 1. a welcome function to explain the purpose of the programme and check if the user wants to continue or not
def check_continue():
    choice=print((input("would you like to continue:(Y/N)")))
    if choice == "N".upper:
        return quit
# 2. a function to create a table (if it does not exist) called patients. The table has 7 attributes, as below:
# patient_id INTEGER (a unique value). It is primary key and cannot be None value (AUTOINCREMENT can be used)
# patient_fname VARCHAR(30)
# patient_sname VARCHAR(30)
# city TEXT
# patient_DOB TEXT
# Tel_no TEXT
# email  TEXT
def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS patients (patient_id INTEGER not NULL, patient_fname VARCHAR(30),patient_sname VARCHAR(30), city TEXT, patient_DOB TEXT,Tel_no TEXT,email  TEXT)')
# 3. a function to insert patients; the function will ask the user to enter patient details and check if the user wants to enter more patients or not.
def insert_details():
    while True:
        patients_id=int(input("please enter patients id:"))
        patients_fname=input("please enter patients fist name:")
        patients_sname=input("please enter patients surname:")
        city=input("please enter city:")
        patients_DBO=input("please enter patients DOB:")
        tel_no=input("please enter patients tel no:")
        email=input("please enter patients email:")
        cur.execute('INSERT INTO patients VALUES(?,?,?,?,?,?,?)',(patients_id, patients_fname, city, patients_sname,patients_DBO,tel_no,email))
        choice=input("would like to add another patients(yes/No)").upper()
        if choice == "NO":
            break
        conn.commit()
# 4. a function to retrieve and print all patients' data.
def retrive_data():
    records= cur.execute('SELECT* FROM patients')
    for a in records:
        print(a)

# 5. a function to delete a patient based on the patient's first name.
def delete():
    k= input("do you need to delete a patient?(yes/no)").upper()
    if k == "YES":
        name=(input("enter fist name:"))
        cur.execute('DELETE FROM patients WHERE patient_fname=?',(name,))
        conn.commit()



# Then call all the functions from the main programme in the same order.

m=check_continue()
print(m)
w=create_table()
print(w)
e=insert_details()
print(e)
r=retrive_data()
print(r)
t=delete()
print(t)