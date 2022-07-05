# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 00:32:37 2022

@author: LINS PC
"""

# Sample Rock,Paper,Scissors Game 1

from random import randint
t = ["R", "P", "S"]
computer = t[randint(0,2)]
print("My Rock, Paper and Scissor Game!!")
score=0
C=0

while C<5:

    player = input("What's your move?  :")
    if player == computer:
        print("Tie!")
        print(score)
    elif player == "R" or "r":
        if computer == "P":
            print("You lose!", computer, "covers", player)
            score=score - 1
            print(score)
        else:
            print("You win!", player, "smashes", computer)
            score = score + 1
            print(score)
    elif player == "P":
        if computer == "S" or "s":
            print("You lose!", computer, "cut", player)
            score = score - 1
            print(score)
        else:
            print("You win!", player, "covers", computer)
            score = score + 1
            print(score)
    elif player == "S":
        if computer == "R" or "r":
            print("You lose...", computer, "smashes", player)
            score = score - 1
            print(score)
        else:
            print("You win!", player, "cut", computer)
            score = score + 1
            print(score)
    else:
        print("That's not a valid play. Check your spelling!")
    C = C + 1

print('Your final score is: ' +str(score))
