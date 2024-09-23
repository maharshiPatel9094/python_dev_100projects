letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


import random
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
# selecting random letters from the letters list
for char in range(0,nr_letters):
    password.append(random.choice(letters))
# print(password)

# selecting random numbers from the numbers list
for num in range(0,nr_numbers):
    password.append(random.choice(numbers))
# print(password)

# selecting random symbols from the symbols list
for sym in range(0,nr_symbols):
    password.append(random.choice(symbols))

# print(password)
random.shuffle(password)
# print(password)


password_list = ""
for char in password:
    password_list += char

print(f"Your final password is {password_list}")