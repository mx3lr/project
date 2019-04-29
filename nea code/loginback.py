iimport bcrypt
import tkinter as tk
from tkinter import messagebox
from regfile import check2


def logins(username, password):  #checks if the students and teachers usernmae is correct
    if users_check(username, password) is True and teachers_check(username, password) is False:
        return MainMenu
    elif users_check(username, password) is False and teachers_check(username, password) is True:
        return TeachersComment
    else:
        return False


def forgot(email, np, confirm_password):  #storing the users new password, using a hash check
    if check2(np, confirm_password) is True: 
        store = bcrypt.hashpw(np.encode("utf8"), bcrypt.gensalt())
        if (users_email(email) is not False and teachers_email(email) is False):  #CHECK 3 EMAIL CHANGE
            update = ("UPDATE users SET password=? WHERE email=?")
            cursor.execute(update, [(store), (email)])
            db.commit()
            return True 
        elif (users_email(email) is False and teachers_email(email) is not False):
            update1 = ("UPDATE teachers SET password=? WHERE email=?")
            cursor.execute(update1 [(store), (email)])
            db.commit() 
            return True
        else:
            messagebox.showerror("Email", "Email doesn't exist") 
    else:
        pass 


def user_check(username, password):
    # Used for the login function this checks against the username and password the user enters in students table
    studentfinder = ("SELECT username,password FROM users WHERE username = ?")
    # sql statement for getting the username and password
    cursor.execute(studentfinder, [(username)])
    check1 = cursor.fetchone()
    if check1 is not None:
        user1, db_password = check1
        if (username == user1) and (bcrypt.checkpw(password.encode("utf8"), db_password) is True):
            return True 
    else:
        return False


def teacher_check(username, password):#checks the username and password entered with the teachers table
    teacherfinder = ("SELECT username,password FROM Teachers WHERE username = ?")
    cursor1.execute(teacherfinder, [(username)]) 
    check2 = cursor1.fetchone() 
    if check2 is not None: 
        user2, db_password1 = check2 
        if (username == user2) and (bcrypt.checkpw(password.encode("utf8"), db_password1) is True):
            return True
    else:
        return False
