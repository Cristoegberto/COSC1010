#
# Crystal Egbert
# 4/12/25
# Pig Latin Programming Project
# COSC 1010
#

# def funtion to convert user input
def new_sentence():

    sentence = input('Please enter your sentence to be translated to Piglatin: ')
  # split the senence into a list
    words = sentence.split()
    # make list and put the new words and sentences in
    pig_list = []
  
# split the input into words
    for word in words:                  # for each word in the sentence
        piglatin_word = user_input(word)  #convert the word to piglatin
        pig_list.append(piglatin_word)    # put piglatin word in pig list
   
        
    final_sentence = ' '                #start final sentence w spaces
    for word in pig_list:              # join
        final_sentence += word + ' '    # concatenate the words w spaces

    print (final_sentence)
    

#def second function to convert the word
def user_input(word):
   
    # store the fist letter in variable first_letter use slicing
    old_word = word[1:]    # hold everything from 1 on
    first_letter = word[0] # hold first letter 
    # concatenate the whole word together in piglatin
    piglatin_word = old_word + first_letter + 'ay' 

    #print new sentence
    return piglatin_word
    
new_sentence()