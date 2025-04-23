#
# Crystal Egbert
# 4/17/25
# Capital Quiz Programming Project
# COSC 1010
#

import random 
NUM_STATES = 5

def main():
    state_caps = state_cap_dictionary()

    # initial variables to keep count of the number
    # of corect and incorrect answers
    correct = 0
    incorrect = 0

    # quiz the user
    for count in range(NUM_STATES):

        #get a random entry from the dictionary get all the keys
        state = random.choice(list(state_caps.keys()))
        # get the individual capital for the state
        capital = state_caps[state] 
        #Quiz the user
        print ('What is the capital of', state,'? ', end='')
        response = input()

        # Is the user correct?
        if response.lower() == capital.lower():
            correct += 1
            print ('Correct!')
        else:
            incorrect += 1
            print ('Incorrect.')

    # Display results
    print('Correct reponses:', correct)
    print('Incorrect responses:', incorrect)


def state_cap_dictionary():
    # Initialize dictionary
    sc = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
    return sc

# Call the main function.
main()