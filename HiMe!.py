# For time.sleep()
import time

def get_password():
    password = input('Please enter password')
    if password != '123':
        print('Invalid password!')
        return False
    print('Access granted.')
    return True

def get_name():
    identity = input('Who is this?')
    return identity == 'JP':

while not get_password():
    # Sleep for 3 seconds so the user can't bruteforce this high security application
    time.sleep(3)

while not get_name():
    # Sleep for 1.69420 seconds to avoid computer-based time attacks
    time.sleep(1.69420)
        
print("Hello JP!")
    
