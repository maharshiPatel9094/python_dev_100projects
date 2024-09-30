import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5]

# making an empty list for adding the user cards and computer cards
user_cards = []
computer_cards = []

# selecting random value cards for user and computer
user_choice = random.choices(cards,weights=weights,k=2)
computer_choice = random.choices(cards,weights=weights,k=2)

# problem - 1
# user_cards.append(user_choice) here the output was list inside list [[10,6]]
# solved by extend method

# adding the randomly selected cards to respective hands
user_cards.extend(user_choice)
computer_cards.extend(computer_choice)

# print the cards
print(f"User cards: {user_cards}")
print(f"Computer cards: {computer_cards}")


# functions to calculate the user and computer score
def calculate_score(chosen_cards):
    """This funtion calculate the sum of cards"""
    return sum(chosen_cards)

# function for checking blackjack in the user and computer cards
def has_blackjack(chosen_cards):
    """This function checks if cards have blackjack or not"""
    # check if 11 and 10 both in cards or not
    return 11 in chosen_cards and 10 in chosen_cards

# function for checking is ace counts as 1 or 11
def adjust_ace(chosen_cards):
    """This function adjusts the ace value"""
    score = calculate_score(chosen_cards)
    if score > 21 and 11 in chosen_cards:
        # index(11) -> find index position of value 11 and change to 1
        chosen_cards[chosen_cards.index(11)] = 1
    return chosen_cards

# calculate the user and computer score
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

# check if user or computer has blackjack or not
user_has_blackjack = has_blackjack(user_cards)
computer_has_blackjack = has_blackjack(computer_cards)

# Display scores and check for Blackjack
if user_has_blackjack:
    print(f"User has Blackjack with {user_cards}!")
else:
    print(f"User score: {user_score}")

if computer_has_blackjack:
    print(f"Computer has Blackjack with {computer_cards}!")
else:
    print(f"Computer score: {computer_score}")

# Determine the winner
if user_has_blackjack and computer_has_blackjack:
    print("It's a tie! Both have Blackjack!")
elif user_has_blackjack:
    print("User wins with a Blackjack!")
elif computer_has_blackjack:
    print("Computer wins with a Blackjack!")
else:
    # No Blackjack, proceed with the game
    # Check if user score is over 21
    # recalculate after adjusting ace value
    user_cards = adjust_ace(user_cards)
    user_score = calculate_score(user_cards)

    if user_score > 21:
        print(f"User busts with score {user_score}. Computer wins!")
    else:
        while True:
            user_choice = input("Do you want to 'hit' or 'stand'? ").lower()
            if user_choice == "hit":
                new_card = random.choice(cards) #3 -> int
                user_cards.append(new_card) #[10,3]
                print(f"New card: {new_card}, User cards: {user_cards}")

                # Adjust for Ace again if needed
                user_cards = adjust_ace(user_cards)
                user_score = calculate_score(user_cards)
                print(f"User score: {user_score}")

                if user_score > 21:
                    print(f"User busts with score {user_score}. Computer wins!")
                    break
            elif user_choice == "stand":
                print(f"User stands with score {user_score}")
                break

            # if user stands, computer plays
            if user_score <= 21:
                while computer_score < 17:
                    new_card = random.choice(cards)
                    computer_cards.append(new_card)
                    print(f"Computer draws a card: {new_card}, Computer cards: {computer_cards}")

                    # adjust for ace again if needed
                    computer_cards = adjust_ace(computer_cards)
                    computer_score = calculate_score(computer_cards)
                    print(f"Computer score: {computer_score}")

                    if computer_score > 21:
                        print(f"Computer busts with score {computer_score}. User wins!")
                        break

                        # If no busts, compare scores
                if computer_score <= 21:
                    print(f"Final User score: {user_score}")
                    print(f"Final Computer score: {computer_score}")

                    if user_score > computer_score:
                        print("User wins!")
                    elif computer_score > user_score:
                        print("Computer wins!")
                    else:
                        print("It's a tie!")