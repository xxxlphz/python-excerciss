import colorama
from colorama import Fore, Back, Style
import random
guesses = 0

green = Fore.GREEN + "green"
red = Fore.RED + "red"
blue = Fore.BLUE + "blue"
yellow = Fore.YELLOW + "yellow"
norm = Fore.WHITE
possiblecolors = [red,green,blue,yellow]
colors = []

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
while True:
    guess = []
    for x in range(4):
        mycolour = input(f'enter colour {x+1}: ')
        if mycolour == 'red':
            guess.append(red)
        elif mycolour == 'green':
            guess.append(green)
        elif mycolour == 'blue':
            guess.append(blue)
        elif mycolour == 'yellow':
            guess.append(yellow)
    returned = []
    guesses += 1
    for i in range(4):
        if guess[i] == colors[i]:
            returned.append('correct')
        else:
            if guess[i] in colors:
                returned.append('partial')
            else:
                returned.append('incorrect')
    print('your guess:',*guess,norm)
    print(returned,end=('\n\n'))
    
    if guess == colors:
        break
 
print('YOU WIN WOOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!! :D')
print(f'guesses taken: {guesses}')
