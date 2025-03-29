#
# Crystal Egbert
# 3/15/25
# Average of Numbers Programming Project
# COSC 1010

    
# Def main
def average_number(holder):

# Name vaiables
    total = 0  # Total of the numbers added
    count = 0  # Count numbers added

try:

# Get the file
    with open ('numbers.txt','r') as file:

        for line in file:           # Read every line
            number = int(line)      # Change the str into int
            total += number         # Find total of all numbers
            count += 1              # Find

# Find the average of the numbers
    if count > 0:
        average = total / count     #divide to find average
        print(f"Average:  {average}")
    else:
        print("No average available.")
        
except ValueError:
    print('There was a ValueError.')
except IOError:
    print('There was a IOError.')

# Call the funtion
average_number('numbers.txt')
