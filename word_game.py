"""
File: word_guess.py
-------------------
My project is an improved version of the Word Guessing Game.
It allows a multiplayer mode (up to 4 players)
"""

import random

LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with
NUM_OF_PLAYERS = 3
DEFAULT_FILE = 'word-guessing-banner.jpg'


def play_game(secret_word):
    secret_word_length = len(secret_word)
    hidden_string = ""
    new_list = []
    guesses = INITIAL_GUESSES
    correct_guesses = 0
    score = 100

    for i in range(secret_word_length):
        new_list.append("-")

    new_string = ""

    for elem in new_list:
        new_string += str(elem)

    print("The word now looks like this: " + new_string)
    print("You have " + str(INITIAL_GUESSES) + " guesses left")

    while guesses != 0 and str(new_list) != secret_word:
        # do not allow user to enter more than one character
        user_guess = input("Type a single letter here, then press enter: ")
        new_string = ""
        found = False

        for i in range(secret_word_length):
            if secret_word[i] == user_guess.upper():
                new_list[i] = user_guess.upper()
                found = True
        if found:
            print("That guess is correct.")
                
        correct_guesses += 1

        for elem in new_list:
            new_string += str(elem)

        if secret_word.find(user_guess.upper()) == -1:
            guesses -= 1
            print("There are no "+ user_guess.upper() + "'s in the word")
            score = score - (score * 0.2) #with each incorrect guess, we remove 20% of the score

        if new_string == secret_word:
            print("Congratulations, the word is: " + new_string)
            break;
        else:
            if guesses == 0:
                print("Sorry, you lost. The secret word was: " + secret_word)
            else:
                print("The word now looks like this: " + new_string)
                print("You have " + str(guesses) + " guesses left")
    return score

def open_lexicon_file(filename):
    cs_words = []
    with open(filename) as f:
        for line in f:
            cs_words.append(line.strip())
    return cs_words


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    cs_words = open_lexicon_file(LEXICON_FILE)
    random_choice = random.choice(cs_words)

    return random_choice

def return_highest_scoring_player(score_list):
    """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
    v = list(score_list.values())
    max_val = max(v)
    min_val = min(v)
    k = list(score_list.keys())
    if max_val != min_val:
        return k[v.index(max(v))] + " wins!"
    else:
        return "It's a tie!"

def output_game_intro():
    print("WELCOME TO MY WORD GUESSING GAME!")
    print("-----------------------------------")
    print("--------                    -------")
    print("------------            -----------")
    print("--------------        -------------")
    print("--------                    -------")
    print("-----------------------------------")


    print("Rules are simple: the computer will generate a random word for you to guess. Enter one character at a time, until you guess the final word. The player who guesses more words, or in less steps wins the round.")
    print("Each player has a maximum of " + str(INITIAL_GUESSES) + " guesses.")
    print("Ready?? Let's get started!!")
    print("-----------------------------------")

def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    output_game_intro()
    score_list = {}

    for i in range(NUM_OF_PLAYERS):
        print("This is Player " + str(i+1) + "'s turn.")
        secret_word = get_word()
        current_player = "Player " + str(i+1)
        score_list[current_player] = play_game(secret_word)
        print(str(current_player) + " scored: " + str(score_list[current_player]))
        print("-----------------------------------")
    print("At the end of this round, here are the results: ")
    print(return_highest_scoring_player(score_list))

    


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
