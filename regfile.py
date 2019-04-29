import sqlite3 as sql
from tkinter import messagebox
import string
import bcrypt
import re

import datetime as dt
#for login, do same for leaderboard

with sql.connect("ChemVision.db") as db:
    global cursor
    cursor=db.cursor()
print("Cursor up")
current_date = dt.date.today().strftime("%d-%m-%Y")
print(current_date)
shared_data= {"forename":"blank", "surname":"blank", "dob":"blank", "class/year":"blank" }


createStudent=('''CREATE TABLE IF NOT EXISTS users(userID PRIMARY KEY,forename VARCHAR(40),surname VARCHAR(20),dob CHAR(10), classyear VARCHAR(10),username VARCHAR(40),password VARCHAR(60),email VARCHAR(255))''')
createTeachers=("""CREATE TABLE IF NOT EXISTS teachers (teachersID INTEGER PRIMARY KEY, forename VARCHAR(40),surname VARCHAR(40), classyear VARCHAR(10), username VARCHAR(40), password VARCHAR(60), email VARCHAR(255))""")

cursor.execute(createStudent)
cursor.execute(createTeachers)

db.commit() #saves changes

def calculate_age(born): #calculates age from the date of birth given by the user
    today = dt.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def date_validate(dob): #calculates if the user is allowed to have this account
    try:
        dt.datetime.strptime(dob, "%d-%m-%Y")
        value = dob.split("-")[::-1]
        newlist = list(map(int,value))
        if calculate_age(dt.date(newlist[0],newlist[1],newlist[2])) < 16:
            messagebox.showerror("Age", "To use ChemVision you need to be in sixth form")
        else:
            return True
    except:
        messagebox.showerror("Date", "Invaild Date please enter a valid date DD-MM-YYYY")
        
        
def details(forename, surname, dob, classyear, var1):
    if forename.isalpha() is True:  #The isalpha() method returns true if all characters in the string are alphabets. 
        forename.title()
        if surname.isalpha() is True:
            surname.title()
            if date_validate(dob) is True:
                if classyear.isalnum() is True:
                    if (var1 == 1 ) or (var1 == 2 ): #var1 student,var2 teacher
                        shared_data["forename"] = forename
                        shared_data["surname"] = surname
                        shared_data["dob"] = dob
                        shared_data["Class/Year"] = classyear
                        return True
                    else:
                        messagebox.showerror("School","Please select whether you are a student or a teacher")

                else:
                    messagebox.showerror("Class/Year","Please select what class you are in")

        else:
            messagebox.showerror("Surname", "Please enter a real Surname")
    else:
        messagebox.showerror("Forename", "Please enter a real Forename")


def check1(username):  #returns different values, will check the database for usernames
    getstudent=("SELECT DISTINCT users.username from users WHERE username=?")
    getteach=("SELECT DISTINCT teachers.username from teachers WHERE username=?")
    cursor.execute(getstudent,[(username)])
    cursor.execute(getstudent,[(username)])
    user1=cursor.fetchall()
    user2=cursor.fetchall()
    if user1 or user2:
        messagebox.showerror("Username","This username is already taken!")
    else:
        return True

def check2(password, confirm_password):#help from https://trinket.io/embed/python3/6807e33204#.XLjcVehKhPY
    if password==confirm_password:

        if len(password) >= 8:

            if len(password) < 20:

                if len(set(string.digits).intersection(password)) > 0:

                    if len(set(string.ascii_uppercase).intersection(password)) > 0:

                        if len(set(string.ascii_lowercase).intersection(password)) > 0:

                            if len(set(string.punctuation).intersection(password)) > 0:
                                return True


                            else:
                                messagebox.showerror("Password","Password should contain atleast one of the symbols to be more secure")
                                return False

                        else:
                            messagebox.showerror("Password","Password should contain at least one lowercase letter to be more secure")
                            return False

                    else:
                        messagebox.showerror("Password","Password should contain at least one uppercase letter to be more secure")
                        return False

                else:
                    messagebox.showerror("Password","Password should should contain a number to be more secure")
                    return False

            else:
                messagebox.showerror("Password","Password should not be greater than 20 characters")
                return False

        else:
             messagebox.showerror("Password","Password should be greater than 8 characters")
             return False

    else:
        messagebox.showerror("Password", "Password don't match one stored in database")  
        return False
                                


#for email validation i got help from stack overflow, as I was struggling to understand what to do for this part
#a useful regex was used for email validation, it is a string patternt that descibe text :'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'

def check3(email):
    if len(email)>7:

        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',email):
            return True

        else:
            messagebox.showerror("Email", "Please enter a valid email address ")
    
    else:
        messagebox.showerror("Email", "Email address should be more than 7 characters")
    
    
    
def register(username, password,confirm_password,email,var1):  #help from https://stackoverflow.com/questions/40577867/bcrypt-checkpw-returns-typeerror-unicode-objects-must-be-encoded-before-checkin

    if check1(username):
        if check2(password, confirm_password):
            store = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
            if check3(email):
                   if var1 == 1:  # inserts one whole record into student table
                    insert_student = ("INSERT INTO users(username,password,email,forename,surname,dob,classyear) VALUES (?, ?, ?, ?,?, ?, ?)")
                    cursor.execute(insert_student, [(shared_data["forename"]), (shared_data["surname"]),(shared_data["dob"]), (shared_data["class/year"]),(username), (store), (email)])
                    

                   elif var1 == 2:
                       insert_teacher = ("INSERT INTO teachers(forename,surname,username,password,email,classyear) VALUES (?, ?, ?, ?, ?, ?)")
                       cursor.execute(insert_teacher, [(shared_data["forename"]), (shared_data["surname"]),(shared_data["dob"]), (shared_data["class/year"]),(username), (store), (email)])
                   db.commit()
                   return True
            
            else:
                return False

        else:
            return False
    else:
        return False    
    
