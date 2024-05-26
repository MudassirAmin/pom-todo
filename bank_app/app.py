#login data
accounts={}

#login and signup
print('[1]login\n[2]signup')
def entry():
    choice=input(':')
    return choice

#signup
def signup():
    full_name=input('Full name:')
    dob=input('D.O.B.:')
    



#choice check
while True:
    if choice=='1':
        login()
    elif choice=='2':
        signup()
    else:
        entry()