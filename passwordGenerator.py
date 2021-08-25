import string                    #for characters
from random import choice        #for choosing at random
import urllib.request            #for reading in website

generate = input("Enter strength of password (weak/medium/strong): ")


characters = string.printable[0:-3]         #all characters
letter_upper = string.ascii_uppercase       #uppercase letters
punct = string.punctuation                  #punctuation characters

#read in word list from website and split into a list
word_list_URL = "https://www.mit.edu/~ecprice/wordlist.10000"
word_list_open = urllib.request.urlopen(word_list_URL)
word_list = word_list_open.read()
word_list = word_list.splitlines()
#filter out extra characters in the concatenated to the word (format: b'word')
word_list_clean = [str(word).replace("b'", "").replace("'", "") for word in word_list]

if generate == "weak":
    #filter out all words that are less than 7 characters
    word_list_filtered = [word for word in word_list_clean if len(word) >= 7]
    #weak strength is a random word of at least 7 characters conconcatenated with 3 numbers
    print(choice(word_list_filtered).capitalize() + str(choice(range(100,1000))))
    
elif generate == "medium":
    #filter out all words that are no 5 characters in length
    word_list_filtered = [word for word in word_list_clean if len(word) == 5]
    #assign 2 empty random words
    rand_word_1 = choice(word_list_filtered)
    rand_word_2 = choice(word_list_filtered)
    
    #concatenate the two words together
    total_word = rand_word_1 + rand_word_2
    
    #dictionary for letters that have lookalike numbers
    leet_speak = {
       "o" : 0,
       "l" : 1,
       "e" : 3,
       "a" : 4,
       "s" : 5,
       "t" : 7,
       "g" : 9
    }
    
    #assign empty string for appending
    leet_word = ""
    
    #replace certain letters with numbers using leet-speak style writing
    #by iterating through the word and comparing if the letter is in the lit
    for char in total_word:
        if char in leet_speak:
            leet_word = leet_word + str(leet_speak[char])
        elif char not in leet_speak:
            leet_word = leet_word + char
    #medium strength password is a random uppercase letter followed by the concatenated word, followed by a random punctuation mark
    print(leet_word + choice(punct) + choice(letter_upper))

#print out 16 random characters including upper/lowercase letters, numbers and punctuation marks
elif generate == "strong":
    for i in range(16):
        print(choice(characters), end="")
