#
# Crystal Egbert
# 4/5/25
# Magic 8 Ball Programming Project
# COSC 1010
#
# import file
import random

# hold responses
responses =[]

 # begin try except
try:                 
    with open('8_ball_responses.txt','r') as file:
      responses = file.readlines()  #read lines and create a file to a list

# prompt user for a question
    while True:
        question = input('Ask my Mystical, Magical 8 Ball youre undying questions: \nType "Done" if you\'ve satified your queries.')

# quit or break loop
        if question == 'Done':
            print('Adios!')
            break

# display randomly selected response from the list
        print(random.choice(responses).strip())  # strip to clean it up

#check for errors
except FileNotFoundError:
    print('The file was not found.')
except IOError:
    print('There was a IOError.') 