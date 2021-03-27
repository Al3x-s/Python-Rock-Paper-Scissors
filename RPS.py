import random
import sys
import os, time

user_choice = input("Rock Paper Scissors... ")

userWins = 0
computerWins = 0
ties = 0

def parseUserChoice(user_choice):
    allchoices = ['ROCK', 'Rock', 'rock', 'r', 'PAPER', 'Paper', 'paper', 'p', 'Scissors', 'SCISSORS', 'scissors', 's']
    if user_choice in allchoices:
        return user_choice
        print('input works')

new_choice = None
def checkChoice(user_choice):
    rchoiceList = ['ROCK', 'Rock', 'rock', 'r']
    pchoiceList = ['PAPER', 'Paper', 'paper', 'p']
    schoiceList = ['Scissors', 'SCISSORS', 'scissors', 's']
    if user_choice in rchoiceList:
        new_choice = 'r'
        return new_choice
    elif user_choice in pchoiceList:
        new_choice = 'p'
        return new_choice
    elif user_choice in schoiceList:
        new_choice = 's'
        return new_choice

consiceChoiceList = ['r', 'p', 's']
computerChoice = random.choice(consiceChoiceList)
compChoiceFull = None

def printCompChoice(computerChoice):
    if computerChoice in ['r']:
        compChoiceFull = 'rock'
        print("The computer played " + compChoiceFull)
    elif computerChoice in ['p']:
        compChoiceFull = 'paper'
        print("The computer played " + compChoiceFull)
    else:
        compChoiceFull = 'scissors'
        print("The computer played " + compChoiceFull)

messages = ['Computer Wins!', 'You Win!', 'Its A Tie!']

def playGame(new_choice, computerChoice):
    if new_choice == 'r':
        if computerChoice == 'p':
            print(messages[0])
        elif computerChoice == 's':
            print(messages[1])
        else:
            print(messages[2])
    elif new_choice == 'p':
        if computerChoice == 's':
            print(messages[0])
        elif computerChoice == 'r':
            print(messages[1])
        else:
            print(messages[2])
    else:
        if computerChoice == 'r':
            print(messages[0])
        elif computerChoice == 'p':
            print(messages[1])
        else:
            print(messages[2])
    
parseUserChoice(user_choice)
checkChoice(user_choice)
printCompChoice(computerChoice)
playGame(new_choice, computerChoice)