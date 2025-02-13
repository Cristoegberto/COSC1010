#
# Crystal Egbert
# 2/13/25
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.
total = 0

# Get number of bugs collected each day using a for loop.
for day in range(1, 8):
    #prompt user.
    print('Enter the bugs collected on day', day)
    # input the number of bugs
    bugs = int(input())
    #add bugs to total.
    total = total + bugs

# Display the total bugs
print('You collected a total of', total, 'bugs')