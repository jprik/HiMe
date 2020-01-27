import time
import sys
import os

def gameloop():

    count = 0

    def get_password():  # Password fetching function.
        password = input('Please enter password: ')
        if password != '123':
            print('Invalid password!')
            return False
        print('Access granted.')
        return True

    def get_name():
        identity = input('Who is this? ')
        return identity == 'JP'

    def pasver():  # Password counting system
        if count >= 3:
            print('You have exceeded the number of tries, shutting down...')
            time.sleep(2)
            sys.exit()
        else:
            return False

    while not get_password():
        count += 1
        print('Waiting for 3 seconds...')
        time.sleep(3)
        pasver()

    while not get_name():
        print('Incorrect user-name...')
        # Sleep for 1.69420 seconds to avoid computer-based time attacks
        print('Waiting for 1.69420 seconds...')
        time.sleep(1.69420)

    print("Hello JP!")

    def registered():
        print('You are logged in, press (q) to logout, type (rps) to launch Rock Paper Scissors, and type (qq) to end this session.')
        choix = input('Choose an option from above: ')

        if choix.lower() == 'q':
            print("Logging out...")

        elif choix.lower() == 'qq':
            print('Quitting...')
            sys.exit()

        if choix.lower() == 'rps':
            print('Launching program...')
            os.system('python rps.py')

    while not registered():
        gameloop()


gameloop()
# Runs all of the above code after it is entirely defined.
