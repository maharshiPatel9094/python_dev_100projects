import random
from game_data import data
from art import logo,vs

# functions
def format_data(account):
    """Format the data into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def get_follower_count(account):
    """Get the followers count."""
    follower_count = account['follower_count']
    return follower_count

def check_answer(user_guess,a_followers,b_followers):
    """Take a user's guess and the followers count and return if they got it right."""
    if a_followers > b_followers:
        return user_guess == "A"
    else:
        return user_guess == "B"

    # if a_followers > b_followers:
    #     if user_guess=='A':
    #         if user_guess=="B":
    #             return False
    #         else:
    #             return True
    #     else:
    #         return False


print(logo)
score = 0
game_continue = True
# meking account at position B become the next account at position a
account_b = random.choice(data)

while game_continue:
    # generating a random data from data
    account_a = account_b
    account_b = random.choice(data)
    # check if both are not same
    if account_a == account_b:
        account_b = random.choice(data)
    # print(account_a)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # ask the user for a guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # check if the user is correct or not
    # -get the followers count of each account
    a_follower_count = get_follower_count(account_a)
    b_follower_count = get_follower_count(account_b)

    # -chek if user is correct or not
    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    # give the user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        game_continue = False

