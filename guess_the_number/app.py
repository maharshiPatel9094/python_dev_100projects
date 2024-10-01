import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# function to check the user guess and the actual guess
def check_answer(user_guess,actual_guess):
    if user_guess > actual_guess:
        print("Too High!")
    elif user_guess < actual_guess:
        print("Too Low!")
    else:
        print(f"Your Guess is Right!, The answer was {actual_guess}")


# function to set the difficulty
def set_difficulty():
    difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if difficulty_level == "easy":
        attempts = EASY_LEVEL_TURNS
        return attempts
    else:
        attempts = HARD_LEVEL_TURNS
        return attempts


# choosing a random number between 1 to 100
# random_number = random.random() * 100
# random_number = round(random_number)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# include both a and b
random_number = random.randint(1,100)
turns = set_difficulty()
game_continue = True
while game_continue:
    print(f"You have {turns} attempts remaining to guess the number.")
    # LET USER GUESS A NUMBER
    guess = int(input("Make a guess: "))
    check_answer(guess, random_number)
    turns -= 1
    # Check if the player has run out of turns or guessed correctly
    if guess == random_number:
        game_continue = False
    elif turns == 0:
        print(f"You've run out of guesses! The number was {random_number}.")
        game_continue = False