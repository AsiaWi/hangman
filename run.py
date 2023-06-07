# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import hangman
import os

from english_words import get_english_words_set
web2set = get_english_words_set(['web2'])

def clear():
    os.system("clear")

def pick_random_word(web2set):
    word = random.choice(web2set).upper()
    while len(word) < 7:
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
    display_word=[]
    chances= 0
    max_chances= 6
    correct_guess= []
    incorrect_guess= []
    hangman_values = ['O','/','|','\\','|','/','\\']
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if letter in word:
        return True
    else:
        show_hangman_values[chances]= hangman_values[chances]
        hangman.print_hangman(hangman_values)
        return False
        
    if True:
           if letter in correct_guess:
               print('You have already used this letter {}'.format(letter))
           else:
               print('Yeey! Great job the letter {} exists in the word'.format(guess))
               correct_guess += letter
               print('yeeeeeeey', correct_guess)
    else:
        print("Bad luck! Try again, this letter doesn't exist inside the word")
        incorrect_guess += letter
        chances -= 1
        print(incorrect_guess)
          

        
def main():
    print('Welcome to Hangman game! Guess the word:)')
    word_list= list(web2set)
    word=pick_random_word(word_list)
    print(word)
    print_randomly_selected_word(word)
    letter=letter_choice()
    check_letter(letter, word)
   
    
   
main()

