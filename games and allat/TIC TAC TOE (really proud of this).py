import random
a = ['_','_','_']
b = ['_','_','_']
c = ['_','_','_']
pcount = 0
print('----TIC TAC TOE----');print('')
game = input('Play against (c)omputer or another (p)erson? ')
if game != 'c' and game != 'p':
    game = input('INVALID INPUT. enter either \'c\' for computer or \'p\' for person: ')





# playing against a friend
elif game == 'p':
    while True:
        
        print('a',a);print('b',b);print('c',c);print('')
        
        # checking for a win
        if a[0] == a[1] == a[2] == 'x'  or  b[0] == b[1] == b[2]== 'x'  or  c[0] == c[1] == c[2]== 'x'  or  a[1] == b[1] == c[1]== 'x'  or  a[2] == b[2] == c[2]== 'x'   or  a[0] == b[0] == c[0]== 'x'  or  a[0] == b[1] == c[2]== 'x'  or  a[2] == b[1] == c[0]== 'x':
            print('GAME OVERRRR THE WINNER IS PLAYER 1')
            again = input('play again? (y/n): ')
            if again != 'y' and again != 'n':
                again = input('bro i said enter \'y\' if you wanna play again and \'n\' if you dont it is NOT that hard. try again: ')
            elif again == 'y':
                a = ['_','_','_']
                b = ['_','_','_']
                c = ['_','_','_']
                pcount = 0
                print('a',a);print('b',b);print('c',c);print('')
            elif again == 'n':
                break
            
        elif a[0] == a[1] == a[2] == 'o'  or  b[0] == b[1] == b[2]== 'o'  or  c[0] == c[1] == c[2]== 'o'  or  a[1] == b[1] == c[1]== 'o'  or  a[2] == b[2] == c[2]== 'o'   or  a[0] == b[0] == c[0]== 'o'  or  a[0] == b[1] == c[2]== 'o'  or  a[2] == b[1] == c[0]== 'o':
            print('GAME OVERRRR THE WINNER IS PLAYER 2')
            again = input('play again? (y/n): ')
            if again != 'y' and again != 'n':
                again = input('bro i said enter \'y\' if you wanna play again and \'n\' if you dont it is NOT that hard. try again: ')
            elif again == 'y':
                a = ['_','_','_']
                b = ['_','_','_']
                c = ['_','_','_']
                pcount = 0
                print('a',a);print('b',b);print('c',c);print('')
            elif again == 'n':
                break
            
        elif a[0] != '_'  and  a[1] != '_'  and  a[2] != '_'  and  b[0] != '_'  and  b[1] != '_'  and  b[2] != '_'  and  c[0] != '_'  and  c[1] != '_'  and  c[2] != '_'  and  '_'  and  a[1] != '_'  and  b[1] != '_'  and  c[1] != '_'  and  a[2] != '_'  and  b[2] != '_'  and  c[2] != '_'  and  a[0] != '_'  and  b[0] != '_'  and  c[0] != '_'  and  a[0] != '_'  and  b[1] != '_'  and  c[2] != '_'  and  a[2] != '_'  and  b[1] != '_'  and  c[0] != '_':
            print('GAME OVERRRR no one wins (yall boooringgg D:)')
            again = input('play again? (y/n): ')
            if again != 'y' and again != 'n':
                again = input('bro i said enter \'y\' if you wanna play again and \'n\' if you dont it is NOT that hard. try again: ')
            elif again == 'y':
                a = ['_','_','_']
                b = ['_','_','_']
                c = ['_','_','_']
                pcount = 0
                print('a',a);print('b',b);print('c',c);print('')
            elif again == 'n':
                break
        
        #getting player number
        pcount += 1
        p = pcount % 2
        if pcount % 2 == 0:
            p = 2
            
        #entering character
        print(f'PLAYER {p}:')
        r = input('choose a row (a, b, c) ')
        cl = input('choose a column (1, 2, 3) ')
        if cl == '1' or cl == '2' or cl == '3':
            cl  = int(cl)
            cl -= 1
            if r.lower() == 'a':
                if a[cl] == '_':
                    if p == 1:
                        a[cl] = 'x'
                    else:
                        a[cl] = 'o'
                else:
                    print('spot is FULL you BOZO. I am SKIPPING YOUR TURN cause you are an IDIOT')
                    
            elif r.lower() == 'b':
                if b[cl] == '_':
                    if p == 1:
                        b[cl] = 'x'
                    else:
                        b[cl] = 'o'
                else:
                    print('spot is FULL you BOZO. I am SKIPPING YOUR TURN cause you are an IDIOT')
            elif r.lower() == 'c':
                if c[cl] == '_':
                    if p == 1:
                        c[cl] = 'x'
                    else:
                        c[cl] = 'o'
                else:
                    print('spot is FULL you BOZO. I am SKIPPING YOUR TURN cause you are an IDIOT')
            else:
                print('INVALID INPUT, YOUR TURN IS SKIPPED CAUSE YOURE AN IDIOT')
        else:
            print('INVALID INPUT, YOUR TURN IS SKIPPED BECAUSE YOURE SILLY')
        
        
        print('')





# playing against comp
print('NOTE: YOU ARE \'x\'')
letters = ['a','b','c']
while True:
    
    # checking for a win
    if a[0] == a[1] == a[2] == 'x'  or  b[0] == b[1] == b[2]== 'x'  or  c[0] == c[1] == c[2]== 'x'  or  a[1] == b[1] == c[1]== 'x'  or  a[2] == b[2] == c[2]== 'x'   or  a[0] == b[0] == c[0]== 'x'  or  a[0] == b[1] == c[2]== 'x'  or  a[2] == b[1] == c[0]== 'x':
        print('GAME OVERRRR YOU WIN nice')
        again = input('play again? (y/n): ')
        if again != 'y' and again != 'n':
            again = input('bro i said enter \'y\' if you wanna play again and \'n\' if you dont it is NOT that hard. try again: ')
        elif again == 'y':
            a = ['_','_','_']
            b = ['_','_','_']
            c = ['_','_','_']
            pcount = 0
            print('a',a);print('b',b);print('c',c);print('')
        elif again == 'n':
            break
        
    elif a[0] == a[1] == a[2] == 'o'  or  b[0] == b[1] == b[2]== 'o'  or  c[0] == c[1] == c[2]== 'o'  or  a[1] == b[1] == c[1]== 'o'  or  a[2] == b[2] == c[2]== 'o'   or  a[0] == b[0] == c[0]== 'o'  or  a[0] == b[1] == c[2]== 'o'  or  a[2] == b[1] == c[0]== 'o':
        print('Goddamn the computer beat you.')
        again = input('play again? (y/n): ')
        if again != 'y' and again != 'n':
            again = input('bro i said enter \'y\' if you wanna play again and \'n\' if you dont it is NOT that hard. try again: ')
        elif again == 'y':
            a = ['_','_','_']
            b = ['_','_','_']
            c = ['_','_','_']
            pcount = 0
            print('a',a);print('b',b);print('c',c);print('')
        elif again == 'n':
            break
        
    elif a[0] != '_'  and  a[1] != '_'  and  a[2] != '_'  and  b[0] != '_'  and  b[1] != '_'  and  b[2] != '_'  and  c[0] != '_'  and  c[1] != '_'  and  c[2] != '_'  and  '_'  and  a[1] != '_'  and  b[1] != '_'  and  c[1] != '_'  and  a[2] != '_'  and  b[2] != '_'  and  c[2] != '_'  and  a[0] != '_'  and  b[0] != '_'  and  c[0] != '_'  and  a[0] != '_'  and  b[1] != '_'  and  c[2] != '_'  and  a[2] != '_'  and  b[1] != '_'  and  c[0] != '_':
        print('GAME OVERRRR no one wins')
        again = input('play again? (y/n): ')
        if again != 'y' and again != 'n':
            again = input('bro i said enter \'y\' if you wanna play again and \'n\' if you dont it is NOT that hard. try again: ')
        elif again == 'y':
            a = ['_','_','_']
            b = ['_','_','_']
            c = ['_','_','_']
            pcount = 0
            print('a',a);print('b',b);print('c',c);print('')
        elif again == 'n':
            break
    
    #getting player number
    pcount += 1
    p = pcount % 2
    if pcount % 2 == 0:
        p = 2
        
    #entering character
    if p == 1:
        print('a',a);print('b',b);print('c',c);print('')
        r = input('choose a row (a, b, c) ')
        cl = input('choose a column (1, 2, 3) ')
        if cl == '1' or cl == '2' or cl == '3':
            cl  = int(cl)
            cl -= 1
            if r.lower() == 'a':
                if a[cl] == '_':
                    a[cl] = 'x'
                else:
                    print('spot is FULL you BOZO. I am SKIPPING YOUR TURN cause you are an IDIOT')
                    
            elif r.lower() == 'b':
                if b[cl] == '_':
                    b[cl] = 'x'
                else:
                    print('spot is FULL you BOZO. I am SKIPPING YOUR TURN cause you are an IDIOT')
            elif r.lower() == 'c':
                if c[cl] == '_':
                    c[cl] = 'x'
                else:
                    print('spot is FULL you BOZO. I am SKIPPING YOUR TURN cause you are an IDIOT')
            else:
                print('INVALID INPUT, YOUR TURN IS SKIPPED CAUSE YOURE AN IDIOT')
        else:
            print('INVALID INPUT, YOUR TURN IS SKIPPED BECAUSE YOURE SILLY')
    elif p == 2:
        while 1:
            r = random.choice(letters)
            cl = random.randint(0,2)
        
            if r == 'a':
                if a[cl] == '_':
                    a[cl] = 'o'
                    break
            elif r == 'b':
                if b[cl] == '_':
                    b[cl] = 'o'
                    break
            elif r == 'c':
                if c[cl] == '_':
                    c[cl] = 'o'
                    break
    
    
    print('')
