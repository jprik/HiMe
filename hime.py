# For time.sleep()
import time, sys



def gameloop():
    
    count = 0
    
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
        
    def pasver(): # Password counting system
        if count >= 4:
            print('You have exceeded the number of tries, shutting down...')
            time.sleep(2)
            sys.exit()
        else:
            return False
            
    while not get_password():
        count +=1
        # Sleep for 3 seconds so the user can't bruteforce this high security application
        print('Waiting for 3 seconds...')
        time.sleep(3)
        pasver()


        
    while not get_name():
        # Sleep for 1.69420 seconds to avoid computer-based time attacks
        print('Waiting for 1.69420 seconds...')
        time.sleep(1.69420)
        
    print("Hello JP!")

    def registered():
        print('You are logged in.')
        choix = input('Would you like to logout?')
    
        # Logout stream after not logging out.
    
        if choix.lower() == 'no':
            print("Ok.")
            podow = input('Would you like to end this session?')
        
            if podow.lower() == 'yes':
                print('Quitting...')
                sys.exit()
            
            else:
                print('Ok, staying online.')
                registered()
            
        if choix.lower() == 'yes':
            print("Logging out...")       

    while not registered():
        gameloop() # Reruns gameloop, should fix issues of program getting lost after relogging.
        
gameloop()
 # Runs all of the above code after it is entirely defined.
