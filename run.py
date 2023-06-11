# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import hangman
import os

from english_words import get_english_words_set
web2set = get_english_words_set(['web2'])

from pyfiglet import Figlet
f = Figlet(font='slant')

def clear():
    os.system("clear")

def pick_random_word(web2set):
    word = random.choice(web2set).upper()
    while len(word) < 7:
        word = random.choice(web2set).upper()
    return word


def users_level_choice():
    while True:
        game_level = input('Enter 1 for begginers or 2 for advanced level: ')
        print()
        try:
            game_level = int(game_level)
        except ValueError:
            print('Numbers only')
            continue
        if  1 <= game_level <=2:
            return game_level
            break
        else:
            print('Please check your options, number outside the allowed range')
    
    clear()
    


def print_the_word(correct_guess, word):
    for i in word:
        if i in correct_guess:
            print(f' {i} ',end='')
        else:
            print(' _ ', end='')
    
def letter_choice():
    letter= input('  Enter the letter here:')
    while len(letter) != 1 or not letter.isalpha():
        print('  Please enter only single letters')
        letter= input('  Enter the letter here:')
    return (letter.upper())

def start_again():
    while True:
        new_game = input('Press 1 if you want to start again!: ')
        try:
            new_game = int(new_game)
        except ValueError:
            print('Incorrect input, try again')
            continue
        if new_game == 1:
            main()
            break
        else:
            print('Invalid number')
        

def game_over(word, chances):
    if chances == 7:
        clear()
        print()
        print(f.renderText(' game  over '))
        print(f'                 The word was: {word}  ')
        return True
    else:
        return False

def winner(word, correct_guess):
        if len(set(word)) == len(correct_guess):
            clear()
            print()
            print('                                 CONGRATULATIONS!') 
            print(f.renderText('       you won ! '))
            print(f'                         {word} is the correct guess!')
            return True
        else:
            return False

def game_loop(word):
    chances= 0
    lives = 7
    correct_guess= []
    incorrect_guess= []
    hangman_values = ['O','/','|','\\','|','/','\\']
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while True:
        print(word) #to be removed before submitting
        hangman.print_hangman(show_hangman_values)
        print_the_word(correct_guess, word)
        print('\n')
        print('  Letters you guessed incorrectly: ', incorrect_guess)
        print()
        print(f'  You have {lives} lives left!')
        print()
        letter=letter_choice()
        if letter in word:
            if letter in correct_guess:
                clear()
                print()
                print("  You have already used this letter! Try again")
                continue
            else:
                clear()
                print()
                print('  Yeey! Great job!')
                correct_guess += letter
                if winner(word, correct_guess):
                    hangman.print_hangman_win(hangman_values)
                    start_again()
                    break
                continue
        else:
            if letter in incorrect_guess:
                clear()
                print()
                print('  You have already used this letter. Try again!')
                continue
                
            else:
                show_hangman_values[chances]= hangman_values[chances]
                chances += 1
                lives -= 1
                if game_over(word,chances):
                    hangman.print_hangman(show_hangman_values)
                    start_again()
                    break
                else:  
                    clear()
                    print()
                    print("  Bad luck! Try again, this letter doesn't exist inside the word")
                    incorrect_guess += letter
                    continue
        clear()


def main():
    clear()
    print()
    print(f.renderText('. . Welcome to . .'))
    print(f.renderText(' H a n g m a n !'))
    word_list= list(web2set)
    game_level=users_level_choice()
    clear()
    word=pick_random_word(word_list)
    game_loop(word)


main()
#print(web2set)

