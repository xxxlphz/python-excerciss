import random as r

possiblecolors = ['red','green','blue','yellow']

colors = [r.choice(possiblecolors) for x in range(4)]

while True:
    
    print(possiblecolors)

    guess = [input(f'input color {x+1}: ') for x in range(4)]

    returned = []

    for i in range(4):

        if guess[i] == colors[i]:

            returned.append('correct')

        else:

            if guess[i] in colors:

                returned.append('partial')

            else:

                returned.append('incorrect')

    print(returned,end=('\n\n'))

    if guess == colors:

        break
 
print('YOU WIN WOOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!! :D')

