def createpassword(user):
    newpwd = input(f'''\nenter new password for user \'{user}\'
Note:  -password should be atleast 8 characters long
       -password should include a upper case letter
       -password should include a lower case letter
       -password should include a number
       -password should include a special character !, £, $, €, %, &, *, #
       : ''')
    while False in checkpassword(newpwd):
        check = checkpassword(newpwd)
        print(problems(newpwd,check))
        newpwd = input('enter new password')
    return newpwd

def is8(pwd):
    if len(pwd) < 8:
        return False
    else:
        return True
    
def hasupper(pwd):
    y = 0
    for x in pwd:
        if x.isupper() == True:
            y +=1
    if y >= 1:
        return True
    elif y == 0:
        return False

def haslower(pwd):
    y = 0
    for x in pwd:
        if x.islower() == True:
            y +=1
    if y >= 1:
        return True
    elif y == 0:
        return False

def hasnumber(pwd):
    x = 0
    for y in pwd:
        if y.isdigit() == True:
            x +=1
    if x >= 1:
        return True
    elif x == 0:
        return False

def hasspecial(pwd):
    y = 0
    for x in pwd:
        if x == '!' or x == '%' or x == '&' or x == '*' or x == '#' or x == '$' or x == '£' or x == '€':
            y +=1
    if y >= 1:
        return True
    elif y == 0:
        return False

def checkpassword(newpwd): #checks if password is valid or not
    conditions = [is8(newpwd),hasupper(newpwd),haslower(newpwd),hasnumber(newpwd),hasspecial(newpwd)]
    return conditions # returns list saying if conditions were met or not

def problems(newpwd,check): #returns problems with password
    check = checkpassword(newpwd)
    if False in check:
        sent = '\nPASSWORD INVALID \n'
    if check[0] == False:
        sent += '- password must contain abe atleast 8 characters long \n'
    if check[1] == False:
        sent += '- password must contain a capital letter \n'
    if check[2] == False:
        sent += '- password must contain a lowercase letter \n'
    if check[3] == False:
        sent += '- password must contain a number\n'
    if check[4] == False:
        sent +='- password must contain one of following !, £, $, €, %, &, *, # n'
    return sent

def createuserid(userlist):
    newuser = input('enter a new User ID: ')
    while newuser in userlist:
        newuser = input('USER ID EXISTS, enter new one: ')
    return newuser

def existinguserid(userlist):
    user = input('enter an existing User ID: ')
    while user not in userlist:
        user = input('USER ID DOES NOT EXIST, enter new one: ')
    return user

userids = [] # stores user ids
pins = []    # stores corresponding password

while 1:
    choice = input('''1) Create a new User ID
2) Change a password
3) Display all user IDs
4) Quit
    enter a menu number (1-4): ''')
    

    #new user id
    if choice  == '1':
        userid = createuserid(userids)
        userids.append(userid) # creating new user id
        
        pins.append(createpassword(userid))#creating password
        print(f'\npassword set \nuser \'{userid}\' created')
    
    #change password
    elif choice == '2':
        user = existinguserid(userids)
        pins[userids.index(user)] = createpassword(user)
        
    #quit
    elif choice == '4':
        print('Logout succesful')
        break
    
    else:
       print('\nINVALID INPUT')
    print('\n')
