import random
import time 
import sys

name=input("what's your name?")
print(' Hi '+ name +' ❤️ ')
print('')
time.sleep(1)

print("Let's play HANGMAN...")
print('')
time.sleep(1)


def play_again():
    answer = input('Play again? yes/no').lower()
    if answer == 'y' or answer =='yes':
        play_game()
    else:
        pass

def get_word():
    words = ['albatross', 'alligator', 'ant', 'bear', 'bee', 'camel', 'cat', 'chameleon', 'cheetah', 'chicken', 'chimpanzee', 'cow', 
             'crocodile', 'crow', 'deer', 'dog', 'dolphin', 'duck', 'eagle', 'elephant', 'falcon', 'finch', 'fox', 'frog', 'grasshopper',
             'hippopotamus', 'horse', 'kangaroo', 'kitten', 'leech', 'lion', 'lobster', 'monkey', 'octopus', 'owl', 'panda', 'parrot',
             'penguin', 'pig', 'pigeon', 'puppy', 'python', 'rabbit','rat','scorpion', 'snake','spider', 'squirrel','tiger', 'toad','turtle','vulture','wolf','zebra']
    return random.choice(words)

def play_game():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = get_word()
    letters_guessed = []
    tries = 10
    guessed = False

    print('The word contains', len(word), 'letters, related to some animal.')
    print(len(word) * '*')
    while guessed == False and tries > 0:
        print('Guess it, you have ' + str(tries) + ' tries')
        guess = input('Please enter one letter or the full word.').lower()
        
        #1 - user inputs a letter
        if len(guess) == 1:
            if guess not in alphabet:
                print('You have not entered a letter 😐') 
            elif guess in letters_guessed:
                print('You have already guessed that letter before 😅')
            elif guess not in word:
                print('Sorry, that letter is not part of the word 😟')
                letters_guessed.append(guess)
                tries -=1
            elif guess in word:
                print('Good Going!✨')
                letters_guessed.append(guess)
            else:
                print('No idea why we get this message, should be investigated further!😵')

        #2 - user inputs the full word
        elif len(guess) == len(word):
            if guess == word:
                print('Well done, you have guessed the word!!! ✨')
                time.sleep(1)
                print('Kya baat!')
                time.sleep(1)
                print('Kya baat!')
                time.sleep(1)
                print('Kya baat!')
                time.sleep(1)
                
                guessed = True
            else:
                print('Sorry, that was not the word we were looking for 😟')
                tries -= 1
                
        #3 - user wants to exit at any point of time.
        elif  guess =='exit' or 'leave':
            print('Thank you and have a nice day.')
            sys.exit(0)

        #4 - user inputs letters > total number of letters in the word or 1 letter. 
        else:
            print('The length of your guess is not the same as the length of the word we\'re looking for 😶')

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '*'
            print(status)

        if status == word:
            print('👏 👏 👏  ')
            time.sleep(1)
            print('Well done, you have guessed the word!😍')
            guessed = True
        elif tries == 0:
            print('You have run out of guesses !!!👎')
            time.sleep(1)
            print('The correct word was: '+ word )
            

    play_again()

play_game()

