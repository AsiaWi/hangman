# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from english_words import get_english_words_set
web2set = get_english_words_set(['web2'])

def pick_random_word(web2set):
    word = random.choice(web2set).upper()
    while len(word) < 6:
        word = random.choice(web2set).upper()



    print(word) 
    
def main():
    word_list= list(web2set)
    pick_random_word(word_list)
    
    
main()
