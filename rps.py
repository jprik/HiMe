import random, sys, os


def scoreKeeper():
    scoreKeeper.ties = 0
    scoreKeeper.wins = 0
    scoreKeeper.losses = 0

scoreKeeper()

def gameState():

    print('Current score is %d tie(s), %d win(s), and %d losse(s).'%(scoreKeeper.ties, scoreKeeper.wins, scoreKeeper.losses))

    quitDecide = input('**Press (q) to quit game, Press enter to resume...**')

    if quitDecide == 'q':

        sys.exit()
        

    else:

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
                scoreKeeper.losses + 1
                return False

            elif playerChoice == 'Paper' and aiChoice == 'Rock':
                scoreKeeper.wins + 1
                return True

            elif playerChoice == 'Scissors' and aiChoice == 'Paper':
                scoreKeeper.wins + 1
                return True

            elif playerChoice == 'Scissors' and aiChoice == 'Rock':
                scoreKeeper.losses + 1
                return False

        def playerTurn():
            print('--Your move!--')

            playerChoiceStr = input()

            print('AI Chose %s'%(aiTurn.aiChoiceStr))

            if playerChoiceStr == aiTurn.aiChoiceStr:
                print('!!Tie game!!')
                scoreKeeper.ties += 1
                gameState()

            elif playerChoiceStr != aiTurn.aiChoiceStr:
                value = isWinner(playerChoiceStr, aiTurn.aiChoiceStr)

                if value is True:
                    print('!!Congratulations, you have won!!')
                    scoreKeeper.wins +=1
                    gameState()

                else:
                    print('!!Better luck next time!!')
                    scoreKeeper.losses += 1
                    gameState()

        aiTurn()
        playerTurn()


gameState()
