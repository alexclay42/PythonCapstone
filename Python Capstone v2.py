#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Get word
def get_word():
    while True:
        secret_word = str(input("Please Enter a Word..."))
        if secret_word.isalpha:
            return secret_word
                   

#get the guess and check it hasn't already been made
def get_guess(guess_list):
    print("get guess")
    while True:
        guess = str(input('Guess a letter: '))
        if guess_list.count(guess) > 0:
            print("Already guessed, choose another letter")
        elif guess.isalpha:
            return guess
                  

#Check if the game is over            
def game_end(word_blanks, guesses_left):
    game_over = False
    if guesses_left == 0: 
        game_over = True
        print("Game End: You Lost", "\n","The Secret Word Was: ", secret_word)     
    elif word_blanks.count('_') == 0:
        game_over = True
        print("Game End: You Won")
    return game_over
        
#Play the Game       
def play_game(guesses_left, secret_word, guess_list, word_blanks):
    print("play game")
    game_over = False
    while game_over == False: 
        print(game_over)
        print(guesses_left)
        guess = get_guess(guess_list)
        print(guess)
        guess_list.append(guess)
        print(guess_list)
        if secret_word.count(guess) > 0:
            i = 0
            while i < secret_word.count(guess):
                for x in secret_word: 
                    if x == guess:
                            word_blanks[secret_word.index(x,secret_word.index(x)+i)] = x   
                            i += 1
            print(word_blanks)
        else:
            print("Letter {} not in word".format(guess))
            guesses_left -= 1
            print("Guesses left: {}".format(guesses_left))
        game_over = game_end(word_blanks, guesses_left)
        
    
def __main__():
    print("main")
    word_blanks = []
    guess_list = []
    guesses_left = 5
    secret_word = get_word()
    
    for x in secret_word:
        word_blanks.append('_')
    print(word_blanks)
    print("Guesses Left: ", guesses_left)
    
    play_game(guesses_left, secret_word, guess_list, word_blanks)
    
        
    
    
if __name__ == "__main__":
    while True:
        if str(input("Play Game Y or N")) == "Y":
            __main__()
        else:
            break

    
    
# In[ ]:


# In[ ]:





# In[ ]:




