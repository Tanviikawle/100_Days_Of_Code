#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER="[name]"

with open("./Input/Names/invited_names.txt") as names:
    all_names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as template:
    content = template.read()
    for name in all_names:
        new_name=name.strip()
        letter=content.replace(PLACEHOLDER,new_name)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt",mode="w") as new_invitation:
            new_invitation.write(letter)