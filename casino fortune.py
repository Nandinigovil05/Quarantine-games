import random
print('''Welcome to the Casino Fortune.
You have $50. You are free to try your luck and gamble .
Answer with yes or no. 

To win you must get one of the following combinations:
💲 💲 💲  pays $250
💲  - 💲  pays $100
-  🍑 💲  pays $50
🍒 🍒 -   pays $20  
''')
#Constants:
INIT_STAKE = 50
ITEMS = ["🍒", "🍑", "🔔", "💲"]

firstWheel = None
secondWheel = None
thirdWheel = None
stake = INIT_STAKE

def play():
    global stake, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    while(stake != 0 and playQuestion == True):
        firstWheel = spinWheel()
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        printScore()
        playQuestion = askPlayer()

def askPlayer():
    '''
    Asks the player if he wants to play again.
    expecting from the user to answer with yes, y, no or n
    No case sensitivity in the answer. yes, YeS, y, y, nO . . . all works
    '''
    global stake
    while(True):
        answer = input("You have $" + str(stake) + ". Would you like to play? ")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("You ended the game with $" + str(stake) + " in your hand.")
            return False
        else:
            print("wrong input!")

def spinWheel():
    '''
    returns a random item from the wheel
    '''
    randomNumber = random.randint(0, 2)
    return ITEMS[randomNumber]

def printScore():
    '''
    prints the current score
    '''
    global stake, firstWheel, secondWheel, thirdWheel
    if((firstWheel == "🍒") and (secondWheel == "🍒")):
        win = 20
    elif((firstWheel == "🍑") and (secondWheel == "🍑") and (thirdWheel != "💲")):
        win = 50
    elif((firstWheel == "💲") and (secondWheel != "💲") and (thirdWheel == "💲")):
        win = 100
    elif((firstWheel == "💲") and (secondWheel == "💲") and (thirdWheel == "💲")):
        win = 250
    else:
        win = -10

    stake += win
    if(win > 0):
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You win $' + str(win))
    else:
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You lose')

play()
