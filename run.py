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
    print('_'* len(word))
    
def letter_choice():
    letter= input('Enter the letter here:')
    while len(letter) != 1 or not letter.isalpha():
        print('Please enter only single letters')
        letter= input('Enter the letter here:')
    print (letter.upper())

def check_letter(letter, word):
    chances= 6
    correct_guess= []
    incorrect_guess= []
    if letter in word:
        correct_guess += letter
    else:
       chances -= 1
       incorrect_guess += letter
       if chances == 0:
        print('sorry,,,,,')

            

def main():
    print('Welcome to Hangman game! Guess the word:)')
    word_list= list(web2set)
    word=pick_random_word(word_list)
    print_randomly_selected_word(word)
    letter=letter_choice()
    check_letter(letter, word)
    
main()

