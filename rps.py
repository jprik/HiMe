import sys, random
from random import randint

def scoreKeeper():
    scoreKeeper.ties = 0
    scoreKeeper.wins = 0
    scoreKeeper.losses = 0

def aiTurn():
    
    aiChoiceInt = random.randint(1, 3)
    if aiChoiceInt == 1:
        aiTurn.aiChoiceStr = 'Rock'
    elif aiChoiceInt == 2:
        aiTurn.aiChoiceStr = 'Paper'
    elif aiChoiceInt == 3:
        aiTurn.aiChoiceStr = 'Scissors'
        
def playerTurn():
    print('Your move!')
    playerChoiceStr = input()
    if playerChoiceStr == 'Rock' and aiTurn.aiChoiceStr == 'Rock':
        scoreKeeper.ties = scoreKeeper.ties + 1
        print('Tie game!')     
    elif playerChoiceStr == 'Rock' and aiTurn.aiChoiceStr == 'Scissors':
        scoreKeeper.wins = scoreKeeper.wins + 1
        print('You win!')
    elif playerChoiceStr == 'Rock' and aiTurn.aiChoiceStr == 'Paper':
        scoreKeeper.losses = scoreKeeper.losses + 1
        print('You lose!')
    elif playerChoiceStr == 'Paper' and aiTurn.aiChoiceStr == 'Rock':
        scoreKeeper.wins = scoreKeeper.wins + 1
        print('You win!')
    elif playerChoiceStr == 'Paper' and aiTurn.aiChoiceStr == 'Paper':
        scoreKeeper.ties = scoreKeeper.ties + 1 
        print('Tie game!')
    elif playerChoiceStr == 'Paper' and aiTurn.aiChoiceStr == 'Scissors':
        scoreKeeper.losses = scoreKeeper.losses + 1
        print('You lose!')
    elif playerChoiceStr == 'Scissors' and aiTurn.aiChoiceStr == 'Rock':
        scoreKeeper.losses = scoreKeeper.losses + 1
        print('You lose!')
    elif playerChoiceStr == 'Scissors' and aiTurn.aiChoiceStr == 'Paper':
        scoreKeeper.wins = scoreKeeper.wins + 1
        print('You win!')
    elif playerChoiceStr == 'Paper' and aiTurn.aiChoiceStr == 'Scissors':
        scoreKeeper.losses = scoreKeeper.losses + 1
        print('You lose!')
        
aiTurn()        
playerTurn()

        