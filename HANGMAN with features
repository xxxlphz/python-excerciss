#hangman
import random as r
import time as t
choices = []
f = open('C:\\Users\\19AAbdallah.ACC\\thonny\\hangmanwords.txt','r')

for line in f:
    choices.append(line)
print('--------HANGMAN---------\n\n')
f.close()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lives = 7
score = 0
correct = []
current = []
incorrectguesses = []
for x in r.choice(choices):
    correct.append(x)
    current.append('_')
    
while current != correct:
    ind = -1
    print(*current,'     incorrect guesses:',*incorrectguesses)
    print('\nlives left:',lives)
    guess = input('\nim thinking of a word. guess a letter in the word: ')
    guess = guess.lower()
    t.sleep(0.3)
    
    if len(guess) > 1:
        print('\n---->thats more than one character, go again: \n\n\n')
        t.sleep(0.8)
    
    elif guess not in alphabet:
        print('\n---->that is NOT a letter lil bro, go again: \n\n\n')
    
    
    elif guess in incorrectguesses or guess in current:
        print('\n---->you already guessed that, go again\n\n\n')
        t.sleep(0.8)
    
    elif guess in correct:
        print('\nCORRECT! go again\n\n\n')
        t.sleep(0.6)
        score +=1
        for x in correct:
            ind += 1
            if guess == x:
                current.pop(ind)
                current.insert(ind,guess)
    
    else:
        print('\n---->nope! sorry, try again\n\n\n')
        lives -= 1
        incorrectguesses.append(guess)
        t.sleep(1)
    if lives == 0:
        word = ''
        for x in correct:
            word = word + x
        print(f'\nlol u lost \nthe word was', word)
        break
if lives > 0:
    print(*current)
    print('\ncongratulations! you got the word :)')
