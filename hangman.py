

hangman_stages = [

    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,

    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,

    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,

    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,

    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,

    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,

    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]





def hangman(word_guess, lives):
    guessed_letters = set()
    if lives == 2:
       print( "Guess the European Capital!\n"
              "Type 'back' to return to difficulty selection \n"
              "Difficulty : Hard\n"
              "Be carefull, you only have 2 lives !!! \n")
    elif lives == 4:
       print( "Guess the European Capital!\n"
              "Type 'back' to return to difficulty selection \n"
              "Difficulty : Medium")
    elif lives == 6:
       print( "Guess the European Capital!\n"
              "Type 'back' to return to difficulty selection \n"
              "Difficulty : Easy")

    original_word = word_guess           # original_word var stores initial casing
    word_guess = word_guess.lower()      # use lower cases to run

    while lives > 0:                     # iterates
        display_word = ""
        for i, letter in enumerate(word_guess):   # letter variable goes through all string characters in word_guess, i takes the index, and we use enumerate() to get both index and letter
            if letter in guessed_letters:
                display_word += original_word[i]  # for loop builds the output, if the letter is guessed, it's displayed, else _
            else:
                display_word += "_"      # first iteration instance we have only ___
        print(display_word)              # stores what will be displayed

        if "_" not in display_word:
            print ("You won!")
            print ( "                                  _    \n   "
                    '                              | |    \n  '
                   "  __ ___  _ __   __ _ _ __ __ _| |_ ___ \n "
                  " / __/ _ \| '_ \ / _` | '__/ _` | __/ __|\n"
                    " | (_| (_) | | | | (_| | | | (_| | |_\__ \n"
                    "  \___\___/|_| |_|\__, |_|  \__,_|\__|___/\n"
                    "                   __/ |                \n  "
                    "                |___/  \n  ")
            return

        guess = input("Enter a letter: ").lower()

        if guess == "quit".lower():
            print ("Good Bye!")
            exit()
        elif guess == 'back':
            return

        if guess in guessed_letters:
            print ("You've already entered that letter!")
            continue                              # skips the rest and jumps to iteration loop

        guessed_letters.add(guess)                # adds guessed letters to set of letters

        if guess in word_guess:
            print ("Correct")
        else:
            lives -= 1
            print(f" You have |-> {lives} <-| lives left. ")
            print(f"Current stage:\n{hangman_stages[6 - lives]}")


    print("You lose. The word was:", word_guess)    # the while loop only ends when you run out of tries and lose the game

import random

capitals_list_1 = ['Bucharest', 'Atena', 'Sofia', 'London', 'Budapest', 'Zagreb', 'Belgrad']
capitals_list_2 = ['Bucharest', 'Atena', 'Sofia', 'London', 'Budapest', 'Zagreb', 'Belgrad', 'Berlin', 'Bratislava', 'Minsk', "Moscova", 'Vatican-City', 'Roma', 'Kiev']
capitals_list_3 = ['Bucharest', 'Atena', 'Sofia', 'London', 'Budapest', 'Zagreb', 'Belgrad', 'Berlin', 'Bratislava', 'Minsk', "Moscova", 'Vatican-City', 'Roma', 'Kiev', 'Varsawa', 'Copenhagen', 'Oslo', 'Stockolm']



while True:
    print("Welcome to Hangman!")
    print("Pick your difficulty:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")
    print("Type 'quit' to exit the game")

    user_input = input().strip().lower()
    if user_input == "quit":
        print("Good Bye!")
        break

    try:
        difficulty = int(user_input)
    except ValueError:
        print ("Invalid input. Please enter a number from 1,2 or 3 for the corresponding difficulty.")
        continue

    if difficulty == 1:
        word_guess = random.choice(capitals_list_1)
        hangman(word_guess, lives=6)
    elif difficulty == 2:
        word_guess = random.choice(capitals_list_2)
        hangman(word_guess, lives=4)
    elif difficulty == 3:
        word_guess = random.choice(capitals_list_3)
        hangman(word_guess, lives=2)
    else:
        print("Invalid difficulty \n"
              "Select again :")







