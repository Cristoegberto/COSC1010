
# Crystal Egbert
# 2/7/2025
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables
# Get the dimentions of the rectangle. 


# Get length A
length1 = int(input('Enter the length of the rectrangle 1: '))

# Get width A
width1 = int(input('Enter the width of rectangle 1: '))

# Get length B
length2 = int(input('Enter the length of rectangle 2: '))

# Get width B
width2 = int(input('Enter the width of the rectangle 2: '))

# Calculate area A
area1 = length1 * width1

# Calculate area B
area2 = length2 * width2

# Print area comparison using if-elif-else statements
if area1 > area2:
    print('Rectangle 1 has the greaeter area.')
else:
    if area2 > area1:
        print('Rectangle 2 has the grater area.')
    else:
        print('Both have same area.')
