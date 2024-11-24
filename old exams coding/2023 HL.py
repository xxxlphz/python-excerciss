#2023 HL, Ahmed, revision

# Section (a)
from random import randint
def guess_game(max_guesses_allowed):
    
    diff = input('Enter difficulty E(asy) or H(ard): ')
    if diff == 'H':
        secret_number = randint(1, 100)
    else:
        secret_number = randint(1, 5)
    guess_count = 0
    user_guess = 0
    guessed = []
    while (user_guess != secret_number) and (guess_count != max_guesses_allowed):
        
        user_guess = int(input("Enter your guess: "))
        guess_count += 1 #Increase guess_count by 1
        if user_guess in guessed:
            print('You already guessed this number.')
        else:
            guessed.append(user_guess)
            
        if user_guess == secret_number:
            print("Congratulations! You win!")
            print(f'You took {guess_count} guesses.')
        elif user_guess > secret_number:
            print('Sorry! Your guess was too high')
        elif user_guess < secret_number:
            print('Sorry! Your guess was too low')

print("Welcome to the guessing game!")
max_guesses = int(input('Enter max number of guesses allowed: '))
guess_game(max_guesses)


# Section (b)
from random import randint
user_score = 0 # sored outiside while loop so it doesnt reset every round
while True:
    secretnumber = randint(1, 100) # randomly chosen number; resets every round
    userguess = int(input("Enter your guess: ")) # variable to store the user's guess
    difference = userguess - secretnumber
    if difference < 0: # to avoid a negative difference
        difference *= -1
    
    print(f'Secret number is {secretnumber}. You guessed {userguess}. Difference is {difference}.')
    
    if secretnumber == userguess:
        print('JACKPOT!!! You score 100 points')
        user_score += 100
    elif difference <= 20: # for when difference is within 20 of the secret number
        print('You score 20 points')
        user_score += 20
    elif difference > 20: # when the difference is more than 20 away 
        print('You lose 30 points')
        user_score -= 30
    
    print(f'Your total score is {user_score}')
    
    playagain = input('Play again? (Y/N): ')
    if playagain != 'Y': # loop ends when user enters something other than 'Y'
        break
