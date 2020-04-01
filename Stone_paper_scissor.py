# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:27:20 2020

@author: Lenovo
"""

import random
import time

def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True


def print_score():
    print(player_name +': '+ str(player_score)+' , computer: ' + str(comp_score) )
    
def print_hand(hand, name='Guest'):
    hands = ['Stone', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])
    

def judge(player, computer):
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'Lose'
    elif player == 1 and computer == 2:
        return 'Lose'
    elif player == 2 and computer == 0:
        return 'Lose'
    else:
        return 'Win'
    

print('\nStarting the Stone Paper Scissors game!')
player_name = input('Please enter your name: ')

player_score = 0
comp_score = 0

for i in range(3):


    print('\n Pick a hand: (0: Stone, 1: Paper, 2: Scissors)')
    player_hand = int(input('Please enter a number (0-2): '))

    if validate(player_hand):
        # Assign a random number between 0 and 2 to computer_hand using randint
        computer_hand =random.randint(0,2) 
    
        print_hand(player_hand, player_name)
        time.sleep(1)
        print_hand(computer_hand, 'Computer')
        time.sleep(1)

        result = judge(player_hand, computer_hand)
        print('Result: ' + result)
        time.sleep(1)
        
        if result == 'Win':
            player_score += 1
            print_score()
        elif result == 'Lose':
            comp_score += 1
            print_score()
        else:
            player_score += 1
            comp_score += 1
            print_score()

        
    else:
            print('Please enter a valid number')
if player_score > comp_score:
    print('\n<--'+player_name +' Wins! -->')
elif comp_score == player_score:
    print('\n<-- Match Draws -->')
else:
    print('\n<--Computer Wins!-->')