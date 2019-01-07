import hashlib

def hashpass(password):
    hash1=hashlib.sha256(txt.encode(password))
    print('Hashed password:', hash1.hexdigest())

def mainpass():
    password=input('Enter your password:')
    hashpass(password)

if __name__ == '__mainpass__':      #runs the program
    mainpass()
    

    
