#
# Crystal Egbert
# 4/12/25
# Vowels and Consonants Programming Project
# COSC 1010
#

# get main function
def main():
    # get input from user
    user_str = input ('Enter a string of characters: ')

    # report the vowels and consonants
    print ('That string has,', num_vowels(user_str), 'vowels and,', \
          num_consonants(user_str), 'constonants')

# get function
def num_vowels(s):
    # make a list of the vowels
    vowels = ['a','e','i','o','u']

    # initialize an accumulator
    v_count = 0

    # count the vowels in s.
    for ch in s:
        if ch.lower() in vowels:
            v_count+= 1

    # return the vowel count
    return v_count 

# get def
def num_consonants (s):
    # make a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # initialize and accumulator
    c_count = 0
    # count the constanants in s:
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1

    # return the consonant count
    return c_count

# call the main
main()