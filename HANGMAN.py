#hangman
import random as r
import time


choices = ['banana','motorbike','car','book','desk','baskemtball','table','mercedes','ferrari','america','ireland','watermelon','apple','stupendous','extravagant']
lives = 4
score = 0
correct = []
current = []
incorrectguesses = []
used = []
for x in r.choice(choices):
    correct.append(x)
    current.append('_')
    
print('--------HANGMAN---------\n\n')
while current != correct:
    ind = -1
    print(*current,'     incorrect guesses:',*incorrectguesses)
    print('\nlives left:',lives)
    guess = input('\nim thinking of a word. guess a letter in the word: ')
    
    if guess in correct:
        print('\nCORRECT! go again\n\n')
        score +=1
        for x in correct:
            ind += 1
            if guess == x:
                current.pop(ind)
                current.insert(ind,guess)
    else:
        print('\nnope! sorry, try again\n\n\n')
        lives -= 1
        incorrectguesses.append(guess)
        time.sleep(0.75)
    if lives == 0:
        print('lmao u lost')
        break
if lives > 0:
    print(*current)
    print('\ncongratulations! you got the word :)')
