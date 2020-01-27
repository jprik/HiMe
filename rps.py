import random

def gameState():

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
            return False

        elif playerChoice == 'Paper' and aiChoice == 'Rock':
            return True

        elif playerChoice == 'Scissors' and aiChoice == 'Paper':
            return True

        elif playerChoice == 'Scissors' and aiChoice == 'Rock':
            return False

    def playerTurn():
        print('Your move!')

        playerChoiceStr = input()

        print('AI Chose {}'.format(aiTurn.aiChoiceStr))

        if playerChoiceStr == aiTurn.aiChoiceStr:
            print('Tie game!')

        elif playerChoiceStr != aiTurn.aiChoiceStr:
            value = isWinner(playerChoiceStr, aiTurn.aiChoiceStr)

            if value is True:
                print('Congratulations, you have won!')
                gameState()

            else:
                print('Better luck next time!')
                gameState()

    aiTurn()
    playerTurn()
gameState()
