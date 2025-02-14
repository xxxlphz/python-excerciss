# WORDLE

import random as r
import colorama
from colorama import Fore, Back, Style


dim = Fore.WHITE + Style.NORMAL
green = Fore.GREEN + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
ylw = Fore.YELLOW + Style.BRIGHT

bright = Fore.WHITE + Style.BRIGHT
colors = []

f = open('words.txt','r')

wordlist = []
for line in f:
    line = line.strip()
    if len(line) == 5:
        wordlist.append(line)


#functions
def check(ug,wrd): # returns placement/correctness of each letter in the users guess (ug)
    ans = []
    for x in range(5): # checking each letter
        if ug[x] in wrd: 
            if wrd[x] == ug[x]:
                ans.append('c') # correct placement
            else:
                ans.append('w') # wrong placement
        elif ug[x] not in wrd:
            ans.append('i') # not in word
    return(ans)

def colourprint(guesses,checked):
    for i in range(len(guesses)):
        rng = guesses[i] # right now guess (current guess)
        rnc = checked[i] # right now check (current check)
        
        if rnc[0] == 'c':  #######
            first = green
        elif rnc[0] == 'w':
           first = ylw
        elif rnc[0] == 'i':
            first = dim
        if rnc[1] == 'c':  #######
            second = green  
        elif rnc[1] == 'w':
           second = ylw
        elif rnc[1] == 'i':
            second = dim
        if rnc[2] == 'c':  #######
            third = green
        elif rnc[2] == 'w':
            third = ylw
        elif rnc[2] == 'i':
            third = dim
        if rnc[3] == 'c':  #######
            fourth = green
        elif rnc[3] == 'w':
            fourth = ylw
        elif rnc[3] == 'i':
            fourth = dim
        if rnc[4] == 'c':  #######
            fifth = green
        elif rnc[4] == 'w':
            fifth = ylw
        elif rnc[4] == 'i':
            fifth = dim
        
        print(first,rng[0],bright,second,rng[1],bright,third,rng[2],bright,fourth,rng[3],bright,fifth,rng[4],bright)

    
    
def playaround():
    randomchoice = r.choice(wordlist).lower()
    wrd = [x for x in randomchoice]
    guesses = []
    checked = [] 
    lives = 0 # when at 6, end round

    print(bright)
    print('Enter five letter words until you guess the hidden one. \n6 lives btw: \n')

    while 1: 
        userinput = input('')
        while len(userinput) != 5 or userinput.isalpha() == False:
            userinput = input('FIVE LETTERS !!!: \n')
        print('')
        ''' thinking of making another restriction where the user guess has to be in the wordlist from earlier but idk cuz
            maybe the list is missing a real word but that doesnt really matter bc the secret word is defo there? idk'''
        
        
        ug = [x for x in userinput.lower()]
        thisword = check(ug,wrd)
        
        guesses.append(ug)
        checked.append(thisword)
        
        colourprint(guesses,checked)
        
        if ug == wrd:
            print(blue, f'\n	YOU WIN !!!!!!!!!!!! \n 	took {lives} tries', bright)
            break
        
        elif lives  == 6:
            print(red, 'you lose :(', bright)
            break
        
        else:
            lives += 1

        
    

        
    
    
    

while 1:
    playaround()
    yn = input('play again? (y/n):')

    if yn.isalpha == False:
        yn = input('literaly type \'y\' to play again and \'n\' to stop')
    else:
        yn = yn.lower()
    if yn == 'n':
        print(blue, 'Thank you for playing :D')
        break
