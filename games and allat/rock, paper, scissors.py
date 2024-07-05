# rock, paper, scissors

import random
list = ['r','p','s']
comp = random.choice(list)
uscore = 0
cscore = 0

while 1:
    user = input('choose (r)ock, (p)aper or (s)cissors: \n')
    comp = random.choice(list)
    print(comp)
    if user == comp:
        print('draw. no one wins')
    elif user == 'r':
        if comp == 's':
            print('WOOOOO you won')
            uscore += 1
        else:
            print('dang you lost')
            cscore += 1
    elif user == 's':
        if comp == 'p':
            print('WOOOOO you won')
            uscore += 1
        else:
            print('dang you lost')
            cscore += 1
    elif user == 'p':
        if comp == 'r':
            print('WOOOOO you won')
            uscore += 1
        else:
            print('dang you lost')
            cscore += 1
    
    print(f'your score: {uscore}')
    print(f'comp score: {cscore}')
    print('\n')
        

