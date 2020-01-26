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

def isWinner(playerChoice, aiChoice):
    if playerChoice == 'Rock' and aiChoice == 'Paper':
        return True
    elif playerChoice == 'Paper' and aiChoice == 'Rock':
        return True
    elif playerChoice == 'Scissors' and aiChoice == 'Paper':
        return True
    return False
        
def playerTurn():
    print('Your move!')
    playerChoiceStr = input()
    print('Ai Chose {}'.format(aiTurn.aiChoiceStr))
    
    if playerChoiceStr == aiTurn.aiChoiceStr:
        print('Tie game!')
    elif playerChoiceStr != aiTurn.aiChoiceStr:
        value = isWinner(playerChoiceStr, aiTurn.aiChoiceStr)
        if value == True:
            print('Congratulations, you won!')
        else:
            print('Better luck next time!')
        
aiTurn()        
playerTurn()

        
