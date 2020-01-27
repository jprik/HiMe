import random, sys, os


def scoreKeeper():
    scoreKeeper.ties = 0
    scoreKeeper.wins = 0
    scoreKeeper.losses = 0

scoreKeeper()

def gameState():

    print('Current score is %d tie(s), %d win(s), and %d losse(s).'%(scoreKeeper.ties, scoreKeeper.wins, scoreKeeper.losses))

    quitDecide = input('**Press (q) to quit game, Press enter to resume...**: ')

    if quitDecide == 'q':
        return 1

    else:

        def aiTurn():

            aiChoiceInt = random.randint(1, 3)
            if aiChoiceInt == 1:
                aiTurn.aiChoiceStr = 'rock'
            elif aiChoiceInt == 2:
                aiTurn.aiChoiceStr = 'paper'
            elif aiChoiceInt == 3:
                aiTurn.aiChoiceStr = 'scissors'


        def isWinner(playerChoice, aiChoice):
            if playerChoice == 'rock' and aiChoice == 'scissors':
                scoreKeeper.wins + 1
                return True
            elif playerChoice == 'paper' and aiChoice == 'rock':
                scoreKeeper.wins + 1
                return True
            elif playerChoice == 'scissors' and aiChoice == 'paper':
                scoreKeeper.wins + 1
                return True
            else:
                # At this point, the player cannot tie
                # or win, so therefore the player can only
                # lose.
                return False

        def playerTurn():
            print('--Your move!--')

            # Convert input to lower-case
            playerChoiceStr = input().lower().strip()

            print(f'You chose {playerChoiceStr}')
            print(f'AI chose {aiTurn.aiChoiceStr}')

            if playerChoiceStr == aiTurn.aiChoiceStr:
                print('!!Tie game!!')
                scoreKeeper.ties += 1
                return
            else:
                won = isWinner(playerChoiceStr, aiTurn.aiChoiceStr)
                if won:
                    print('!!Congratulations, you have won!!')
                    scoreKeeper.wins += 1
                    return
                else:
                    print('!!Better luck next time!!')
                    scoreKeeper.losses += 1
                    return

        aiTurn()
        playerTurn()
        return 0


state = 0
while state== 0:
    state = gameState()
    
