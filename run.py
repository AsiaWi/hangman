# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random, hangman
from english_words import get_english_words_set
web2set = get_english_words_set(['web2'])


def pick_random_word(web2set):
    word = random.choice(web2set).upper()
    while len(word) < 6:
        word = random.choice(web2set).upper()
    return word

def print_randomly_selected_word(word):
    print(' _ '* len(word))
    
def letter_choice():
    hangman_values = ['O','/','|','\\','|','/','\\']
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    hangman.print_hangman(show_hangman_values)
    letter= input('Enter the letter here:')
    while len(letter) != 1 or not letter.isalpha():
        print('Please enter only single letters')
        letter= input('Enter the letter here:')
    return (letter.upper())

def check_letter(letter, word):
    display_character= []
    chances= 6
    max_chances= 6
    correct_guess= []
    incorrect_guess= []
    hangman_values = ['O','/','|','\\','|','/','\\']
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

    if letter in word:
        correct_guess += letter
        return correct_guess
    else:
        show_hangman_values[0]= hangman_values[0]
        chances -= 1
        incorrect_guess += letter
        
        hangman.print_hangman(hangman_values)
        print('no')
        if chances == 0:
           print('GAME OVER!')
          
           print('The word was {word}')

def print_guessed_letter(word, correct_guess):
    for letter in word:
        if letter in word:
            print('{}'.format(letter),end='')
        else:
            print('_', end='')    

def main():
    print('Welcome to Hangman game! Guess the word:)')
    word_list= list(web2set)
    word=pick_random_word(word_list)
    print(word)
    print_randomly_selected_word(word)
    letter=letter_choice()
    correct_guess=check_letter(letter, word)
    #print_guessed_letter(word, correct_guess)
   
main()

