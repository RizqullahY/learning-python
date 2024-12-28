import re
from queue import Empty

def passwordyangkuat():
    password = input('Masukkan Passwordmu :')
    
    if password == Empty:
        print(0)
    if password ==(r'^[0-9]*$'):
        print(0,8)

passwordyangkuat()


# v=input("Enter the password:")
# if(len(v)>=8):
#     if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',v))==True):
#         print("The password is strong")
#     elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',v))==True):
#         print("The password is weak")
# else:
#     print("You have entered an invalid password.")


# def password():

#     print ('enter password')
#     print ()
#     print ()
#     print ('the password must be at least 6, and no more than 12 characters long')
#     print ()

#     password = input ('type your password    ....')


#     weak = 'weak'
#     med = 'medium'
#     strong = 'strong'

#     if len(password) >12:
#         print ('password is too long It must be between 6 and 12 characters')

#     elif len(password) <6:
#         print ('password is too short It must be between 6 and 12 characters')


#     elif len(password)    >=6 and len(password) <= 12:
#         print ('password ok')

#         if password.lower()== password or password.upper()==password or password.isalnum()==password:
#             print ('password is', weak)

#         elif password.lower()== password and password.upper()==password or password.isalnum()==password:
#             print ('password is', med)

#         else:
#             password.lower()== password and password.upper()==password and password.isalnum()==password
#             print ('password is', strong)
# password()