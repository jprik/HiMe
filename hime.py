# For time.sleep()
import time, sys

def get_password():
    password = input('Please enter password: ')
    if password != '123':
        print('Invalid password!')
        return False
    print('Access granted.')
    return True

def get_name():
    identity = input('Who is this? ')
    return identity == 'JP'

while not get_password():
    # Sleep for 3 seconds so the user can't bruteforce this high security application
    print('Waiting for 3 seconds...')
    time.sleep(3)

while not get_name():
    # Sleep for 1.69420 seconds to avoid computer-based time attacks
    print('Waiting for 1.69420 seconds...')
    time.sleep(1.69420)
        
print("Hello JP!")

def registered():
    print('You are logged in.')
    choix = input('Would you like to logout?')
    
    # Logout stream after not logging out.
    
    if choix == 'No':
        print("Ok.")
        podow = input('Would you like to end this session?')
        
        if podow == 'Yes':
            print('Quitting...')
            sys.exit()
            
        else:
            print('Ok, staying online.')
            registered()
            
    if choix == 'Yes':
        print("Logging out...")       

while not registered():
    get_password()
    get_name()
        
