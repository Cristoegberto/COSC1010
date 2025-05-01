# Crystal Egbert
# 4/24/25
# File Encryption and Decryption Programming Project
# COSC 1010
#
def decoding_dictionary():
    decoding = {
        'A': '!',  'a': '1',
        'B': '@',  'b': '2',
        'C': '#',  'c': '3',
        'D': '$',  'd': '4',
        'E': '%',  'e': '5',
        'F': '^',  'f': '6',
        'G': '&',  'g': '7',
        'H': '*',  'h': '8',
        'I': '(',  'i': '9',
        'J': ')',  'j': '0',
        'K': '+',  'k': '=',
        'L': '{',  'l': '}',
        'M': '[',  'm': ']',
        'N': '<',  'n': '>',
        'O': '/',  'o': '?',
        'P': '|',  'p': '`',
        'Q': 'a',  'q': 'b',
        'R': 'c',  'r': 'd',
        'S': 'e',  's': 'f',
        'T': 'g',  't': 'h',
        'U': 'i',  'u': 'j',
        'V': 'k',  'v': 'l',
        'W': 'm',  'w': 'n',
        'X': 'o',  'x': 'p',
        'Y': 'q',  'y': 'r',
        'Z': 's',  'z': 't'
    }
# Return the dictionary so other functions can use it
    return decoding 

def main():
    codes = decoding_dictionary()
    
# Open the text.txt file in read
    with open ('text.txt','r') as file:
# Open the encrypted file to write to
        with open('encrypted.txt', 'w') as encrypted_file:
# Read every line
            for line in file:
# Translate into my empty dictionary
                translated_line = ''

# Loop through each characher in the line
                for char in line:
# Check for the character in my dictionary and use the symbol
                    if char in codes:
# Replace it with the symbol from my dictionary and add to sting
                        translated_line += codes [char] 
                    else:
# If character not in dictionary leave it alone
                         translated_line += char
# Write the translated line in the encrypted file
                encrypted_file.write(translated_line)

# Put the translated_line into encrypted_text as a .txt file
def finaltranslation():
# get the dictionary again
    codes = decoding_dictionary()
# Reverse the dictionary to decode symbols back to letters
    reverse_codes = {symbol: letter for letter, symbol in codes.items()}
# Open encrypted_text.txt
    with open ('encrypted.txt','r') as file:
# Read it line for line
        for line in file:
# Name new empty file final_translation
            final_translation = ''
# Loop through each characher in the line
            for char in line:
# Check for the character in my dictionary
                if char in reverse_codes:
# Replace it with the symbol from my dictionary
                    final_translation += reverse_codes [char]
                else:
# If character not in dictionary leave it alone
                    final_translation += char

# Print decoded line
            print(final_translation)

# Call main()
main ()

# Call finaltranlation 
finaltranslation ()