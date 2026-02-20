import random

#making a random word bank
word_bank = ['rizz', 'vote', 'nepal', 'love', 'heart', 'india']

#choosing the random word from word bank
word = random.choice(word_bank)

guess_word = ['_'] * len(word)

#how many attempt can player make 
attempt = 10

while attempt>0:
    print('\nCurrent word: ' + ' '.join(guess_word))

    #asking user for the guess for
    guess = input("Enter a word : ").lower()
    #checking weather the guess word is correct or not 
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guess_word[i] = guess
        print('Great guess!')
    else:
        attempt -= 1
        print('Wrong guess! Attempts left: ' + attempt)

    
    #checking weather there is a blank space or not
    if '_' not in guess_word:
        print('\nCongratulations You guessed the word: ' + word)
        break

    #in case of loss
    if attempt == 0 and '_' in guess_word:
        print(f"You've run out of attempts! The word was:  {word}")

    



    




