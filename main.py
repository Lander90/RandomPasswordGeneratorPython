import random

#Definitions-----------------------
password = ''
alwaysTrue = True
opt = 0
chars = ["1","2","3","4","5","6","7","8","9","0","!","@","#", "$", "%","^", "&", "*", "(", ")"]
#Functions-------------------------
def promptMenu():
    global password
    while alwaysTrue == True:
        opt = input("Would you like to generate a password? (Y/N) ")
        if opt == 'Y':
            password = ''
            generatePassword()
        elif opt == 'N':
            break
            password = ''
        else:
            print("That's not an option! Try again")
def generatePassword():
    global password
    for i in range(1,16):
        password += chars[random.randint(0,16)]
    print(password)
    password= ''
#Code------------------------------
promptMenu()
