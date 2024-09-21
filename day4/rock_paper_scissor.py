rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
images_options = [rock,paper,scissors]
user_choice = int(input("What do you choose ? Type 0 for rock , 1 for paper and 2 for scissors.\n"))
print(f"You choose: {user_choice}")
print(images_options[user_choice])
# if user_choice == 0:
    # print(rock)
# elif user_choice == 1:
    # print(paper)
# elif user_choice == 2:
    # print(scissors)
# else:
    # print("You Entered The Wrong Value!!")

computer_choice = random.randint(0,2)
print(f"Computer chose: {computer_choice}")
print(images_options[computer_choice])

# test cases
if user_choice >= 3 or user_choice < 0:
    print("You entered the wrong value, You loose!!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win !")
elif user_choice == 1 and computer_choice == 0:
    print("You Win !")
elif user_choice == 2 and computer_choice == 1:
    print("You Win !")
elif computer_choice == 0 and user_choice == 2:
    print("You Loose !")
elif computer_choice == 1 and user_choice == 0:
    print("You Loose !")
elif computer_choice == 2 and user_choice == 1:
    print("You Loose !")
elif computer_choice == user_choice:
    print("It's A Draw !")


