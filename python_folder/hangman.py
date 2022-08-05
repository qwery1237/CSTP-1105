import os
import time
import random
# clear the console   os.system('cls')
# wait to be excuted for x ms time.sleep(x)
# Hangman

# Select a word computer_word
# get_random_word()
def get_random_word():
    word_list = ["pokemon", "eggplant", "hacker", "computer","cricket","recursion"]
    return random.choice((word_list))

# Global Variables
#game_word = get_random_word()
game_word = "battle"
guess_limit = 6
guess_count = 0
guesses_prev = []


# call this every game turn
def game_turn():
    global game_word, guess_limit, guess_count


    guess_count +=1
    print(f"{guess_count}/{guess_limit} Guess a letter")
    # Display guesses
    display_word = display_guess_word(game_word,guesses_prev)
    print(display_word)
    # Ask user for letter
    user_letter = input("Pick a letter: ").lower()
    guess_count -=1 if user_letter in game_word else 0
    guesses_prev.append(user_letter)
    check_if_game_has_ended(guess_count, game_word, guesses_prev)
    
   
    # Check to see if game has won or not



def display_guess_word(game_word, prev_guesses = []):
    player_word = []
    
    for letter in game_word:
        if letter in prev_guesses:
            player_word.append(letter)
            

        else:
            player_word.append('_')
    return " ".join(player_word)

def check_if_game_has_ended(guess_count, game_word, guesses_prev):
    guessed_word = display_guess_word(game_word, guesses_prev)
    if "_" not in guessed_word:
        print("You have won")
    elif guess_count>= guess_limit:  
        print("You have lost")
    else:
        #print("Next Turn")
        game_turn()

display_guess_word(game_word)
game_turn()


# display previous guesses
# including first attempt when there
# are no letters
# display_prev_guess()

# guess_limit(6)

# guess_count(max 6)

# check to see if game is won
# check_game_won()

# on each game turn
# game_turn() a function called each turn

# display win or lose and display the correct word at the end

# reset() reset game back to original