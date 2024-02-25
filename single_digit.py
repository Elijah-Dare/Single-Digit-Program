""" This is a program that checks if a user enters a single digit
It returns false if the user does not input a single digit"""

def get_single_digit(number):
    """This function checks whether the digit entered is single or not"""
    if len(number) == 1 and number.isdigit(): # This checks if the length of the input of the user and if the 
                                              # input is a number
        return True
    else:
        return False
    
active = True # A flag is created
while active: # Program main loop
    prompt = 'Enter a number> '
    response = input(prompt) # This takes in the input from the user.
    
    # This loop checks what the function returns and prints its equivalent output
    if get_single_digit(response):
        print('Valid single digit')
        break
    else:
        print('Not a valid single digit')
        
        
print(f"Ths single digit you entered is, {response}") # This prints out the single digit entered by the user after the if loop is valid.
