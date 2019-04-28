import bcrypt

def bcrpytchecker(): #hashcheck to encode password
    password=input("Enter pass")
    hashed=bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
    print(hashed)
    print(len(hashed))

bcrpytchecker()    
