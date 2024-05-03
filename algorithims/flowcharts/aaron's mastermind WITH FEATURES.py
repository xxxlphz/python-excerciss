import colorama
from colorama import Fore, Back, Style
import random
guesses = 0

dim = Fore.WHITE + Style.NORMAL
green = Fore.GREEN + "(g)reen"
red = Fore.RED + "(r)ed"
blue = Fore.BLUE + "(b)lue"
yellow = Fore.YELLOW + "(y)ellow"
purp = Fore.MAGENTA + Style.BRIGHT + "(p)urple"
norm = Fore.WHITE + Style.BRIGHT
possiblecolors = [red,green,blue,yellow,purp]
colors = []

print(norm)

for x in range(4):
    z = random.randint(0,3)
    colors.append(possiblecolors[z])
    
rules = '''
-------MASTERMIND-------

RULES:
    1. Computer will chose a random arrangement of colours from the list provided
    2. User will enter four colours one by one and try to guess the computers arrangement in the least number of guesses
    3. At the end of each turn, the user will be told if each color was correct & in the right place, correct & in the wrong place, or not in the computers arrangement
*Note that colours can be repeated

'''
print(rules)
print('POSSIBLE COLOURS: ',end='');print(*possiblecolors, norm)
print('*For rules, enter \'rules\'')
print(' For list of colours, enter \'colours\'\n', norm)
while True:
    guess = []
    for x in range(4):
        mycolour = input(f'enter colour {x+1}: ')
        while 1:
            if mycolour.lower() == 'rules':
                print(rules)
                break
            elif mycolour.lower() == 'colours' or mycolour.lower() == 'colors':
                print(*possiblecolors,norm)
                break
            elif mycolour.lower() == 'red' or mycolour.lower() == 'r':
                guess.append(red)
                break
            elif mycolour.lower() == 'green' or mycolour.lower() == 'g':
                guess.append(green)
                break
            elif mycolour.lower() == 'blue' or mycolour.lower() == 'b':
                guess.append(blue)
                break
            elif mycolour.lower() == 'purple' or mycolour.lower() == 'p':
                guess.append(purp)
                break
            elif mycolour.lower() == 'yellow' or mycolour.lower() == 'y':
                guess.append(yellow)
                break
            else:
                mycolour = input(f'!!! INVALID: ')
    returned = []
    guesses += 1
    for i in range(4):
        if guess[i] == colors[i]:
            returned.append(f'{dim}correct')
        else:
            if guess[i] in colors:
                returned.append(f'{dim}partial')
            else:
                returned.append(f'{dim}incorrect')
    print('your guess:',*guess,norm)
    print(*returned,end=('\n\n'))
    
    if guess == colors:
        break
 
print('YOU WIN WOOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!! :D')
print(f'guesses taken: {guesses}')
