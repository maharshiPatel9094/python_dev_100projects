PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as invited_peoples:
    # print the names as it is
    # names = invited_peoples.read()
    # print the names in the format of list
    names = invited_peoples.readlines()
    print(names)
    
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names:
        stripped_names = name.strip()
        new_letter =letter_content.replace(PLACEHOLDER,stripped_names)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_names}.docx",mode="w") as completed_letter:
            completed_letter.write(new_letter)