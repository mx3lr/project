import bcrypt

#help from:
#https://stackoverflow.com/questions/40577867/bcrypt-checkpw-returns-typeerror-unicode-objects-must-be-encoded-before-checkin

def bcrpytchecker(): #hashcheck to encode password
    password=input("Enter pass")
    hashed=bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
    print(hashed)
    print(len(hashed))

bcrpytchecker()    
