import random


print("Welcome to hangman!")
word_list = []

# Prints out the main menu for the game.
# Allows user to choose to either work with word list, play, or terminate the program.
def main_menu():
    print("Menu: ")
    print("1. Word list")
    print("2. Play")
    print("3. Exit")
    choice = input("Please enter your selection: ")
    return choice

# Prints out the menu for the word list option.
# Allows user to either view the current word list, modify the word list, or return to the main menu.
def word_list_menu():
    print("Menu: ")
    print("1. View word list")
    print("2. Modify")
    print("3. Return to Main Menu")
    choice = input("Please enter your selection: ")
    return choice

# Allows user to add words to the word list and converts all to capital letters.
def add_word(word_list):
    word_input = input("Please enter a list of words you wish to add separated by space ")
    word_upper = word_input.upper().split()
    word_list = word_list + word_upper
    return list(set(word_list))

# Takes user's input during the word list menu and performs code accordingly.
def main_menu_choice_1(word_list):
    while True:
        try:
            list_choice = word_list_menu()
            if int(list_choice) == 1:
                print(word_list)
            elif int(list_choice) == 2:
                word_list = word_list_choice_2(word_list)
            elif int(list_choice) == 3:
                break
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid selection.")
    return word_list

# Selects a random word from the word list and prints out spaces respective to the word's length.
# Main code of the program and runs the game until user runs out of lives or completes the word.
def play(word_list):
        random_word = random.choice(word_list)
        split_word = list(random_word)
        letter_number = '_ ' * len(split_word)
        word_length = letter_number.strip().split(' ')
        print("A random word has been selected. The word contains {} letters.".format(len(split_word)))

        x = 0
        while x < 7:
            guess = " ".join(word_length)
            guess_remain = 7 - x
            if word_length == split_word:
                print("Congraduations! You've successfully guessed the word!")
                break
            guess_letter = input(
                "{}       You have {} tries remaining. Please enter a letter to guess: ".format(guess, guess_remain))
            guess_letter = guess_letter.upper()
            if guess_letter == random_word:
                print("Congraduation! You've successfully guessed the word!")
                break
            elif guess_letter in split_word:
                for y in range(len(split_word)):
                    if split_word[y] == guess_letter:
                        word_length[y] = guess_letter
            else:
                x = x + 1

# Pulls up menu when users select modify.
def modify_menu(word_list):
    print("Menu: ")
    print("1. Add words")
    print("2. Remove specific word")
    print("3. Clear word list")
    print("4. Return to word list menu")
    modify_choice = input("Please enter your selection: ")
    return modify_choice

# Allows users to input words to remove from the current word list.
def remove_word(word_list):
    word_input = input("Please enter a list of words you wish to remove separated with space: ")
    word_upper = word_input.upper().split()
    for word in word_upper:
        if word in word_list:
            word_list.remove(word)
    return word_list

# Checks user's selection within the modify menu and runs code accordingly.
def word_list_choice_2(word_list):
    while True:
        try:
            modify_choice = modify_menu(word_list)
            if int(modify_choice) == 1:
                word_list = add_word(word_list)
            elif int(modify_choice) == 2:
                word_list = remove_word(word_list)
            elif int(modify_choice) == 3:
                word_list.clear()
            elif int(modify_choice) == 4:
                break
            else:
                modify_choice = input("Invalid selection. Please enter a valid selection: ")
        except ValueError:
            print("Invalid selection.")
    return word_list

while True:
    main_choice = main_menu()
    try:
        if int(main_choice) == 1:
            word_list = main_menu_choice_1(word_list)
        elif int(main_choice) == 2:
            if len(word_list) == 0:
                print("Word list is empty. Please add words to the word list to play")
            else:
                play(word_list)
        elif int(main_choice) == 3:
            break
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid selection.")





