#2023 HL
# Section (a)
from random import randint
def guess_game(max_guesses_allowed):
    
    diff = input('Enter difficulty E(asy) or H(ard): ')
    if diff.lower() == 'H':
        secret_number = randint(1, 100)
    else:
        secret_number = randint(1, 5)
    guess_count = 0
    user_guess = 0
    guessed = []
    while (user_guess != secret_number):
        
        user_guess = int(input("Enter your guess: "))
        guess_count += 1 #Increase guess_count by 1
        if user_guess in guessed:
            print('You already guessed this number.')
        elif user_guess > secret_number:
            print('Sorry! Your guess was too high')
        elif user_guess < secret_number:
            print('Sorry! Your guess was too low')
            
        if user_guess == secret_number:
            print("Congratulations! You win!")
            print(f'You took {guess_count} guesses.')
            
        if guess_count == max_guesses_allowed:
            break
        guessed.append(user_guess)
            
print("Welcome to the guessing game!")
max_guesses = int(input('Enter max number of guesses allowed: '))
guess_game(max_guesses)



# Section (b)
import random as r
user_score = 0
while True:
    secretnumber = r.randint(1, 100)
    userguess = int(input("Enter your guess: "))
    
    if userguess > secretnumber: #to avoid negatives when calculating difference
        difference = userguess - secretnumber
    elif secretnumber > userguess:
        difference = secretnumber - userguess
    
    print(f'Secret number is {secretnumber}. You guessed {userguess}. Difference is {difference}.')
    
    if secretnumber == userguess:
        print('JACKPOT!!! You score 100 points')
        user_score += 100
    elif difference < 20:
        print('You score 20 points')
        user_score += 20
    elif difference > 30:
        print('You lose 30 points')
        user_score -= 30
    
    print(f'Your total score is {user_score}')
    
    playagain = input('Play again? (Y/N): ')
    if playagain != 'Y': # loop ends when user enters something other than 'Y'
        break
    
    

        
    
    
    
    
    
    
    
    
    
    
