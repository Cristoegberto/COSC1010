#
# Crystal Egbert
# 3/15/25
# File Display Programming Project
# COSC 1010
#
# Open file
myfile = open('numbers.txt','r')

# Read and display the files contents
for line in myfile:   # Read every line
    number = int(line) # convert str to int
    print(number)   # print number as int

# Close the file
myfile.close 