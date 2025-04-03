#
# Crystal Egbert
# 3/28/25
# Lottery Number Generator Programming Project
# COSC 1010
#
# import 
import random 


# define functions
numbers = [0] * 7    #repeat this element 7 times

# make loop to iterate 7 times
for index in range (7):
    #pick random number 0-9
    numbers[index] = random.randint (0, 9)   

# display the random numbers
print(numbers) 