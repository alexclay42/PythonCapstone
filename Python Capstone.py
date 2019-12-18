#!/usr/bin/env python
# coding: utf-8

# In[1]:



#Get word
while True:
    secret_word = str(input("Please Enter a Word..."))
    if secret_word.isalpha:
        break
#return length and number of guesses - use blank spaces to show number of letters
word_blanks = []
guess_list = []
guess = ' '
guesses_left = 5

#guess = ''
for x in secret_word:
    word_blanks.append('_')
print(word_blanks)
print(guesses_left)



while True:
    while True:
        guess = str(input('Guess a letter: '))
        if guess_list.count(guess) > 0:
            print("Already guessed, choose another letter")
        elif guess.isalpha:
            break
    if secret_word.count(guess) > 0:
        guess_list.append(guess)
        i = 1
        while i <= secret_word.count(guess):
            for x in secret_word: 
                if x == guess:
                    if i == 1:
                        word_blanks[secret_word.index(x)] = x   
                        i += 1
                    elif i == 2:
                        word_blanks[secret_word.index(x, secret_word.index(x)+1)] = x   
                        i += 1
        print(word_blanks)
    else:
        print("Letter {} not in word".format(guess))
        guesses_left -= 1
        print("Guesses left: {}".format(guesses_left))
    if guesses_left == 0 or word_blanks.count('_') == 0:
        print("Game End")
        print(secret_word)
        break
    


# In[ ]:




