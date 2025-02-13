#
# Crytal Egbert
# 02/08/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
# 
#Constants
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

#local variables
numAttending = 0    # The number of people attending
numPerPerson = 0    # The number of dog dogs and buns per person
total = 0   # Total numer of hot dogs and buns needed
minDogs = 0     # Minimus number of packages of hot dogs
minBuns = 0     # Minimus number of packages of hot dog buns
dogsLeft = 0    # The number of hot dogs left from a package
bunsLeft = 0    # The number of hot dog buns left from a package

# Get the number of people attending the cookout.
numAttending = int(input('Enter the numer of people attending the cookout. '))

# Get the number of hot dogs from the user.
numPerPerson = int(input('Enter the number of hot dogs per person. '))

# Calculate the total number of hot dogs needed.
total = numAttending * numPerPerson

# Calculate the minimum number of hot dogs needed.
minDogs = total // HOT_DOGS_PER_PACKAGE

# Determine if the number of people attending is large enough to require more than one package of hot dogs
if minDogs > 0:
    # Calculate the number of hot dogs left over from a package if any
    dogsLeft = total % HOT_DOGS_PER_PACKAGE

    # If there will be left overs add an additional hot dogs
    if dogsLeft != 0:
        minDogs += 1
   # Set the minimum number of packages of hot dogs to one
else:
    minDogs = 1

# Determing the number of left over hot dogs, if any
dogsLeft = HOT_DOGS_PER_PACKAGE * minDogs - total

### ME Bun variables ###


# Calculate the total number of hot dogs needed.
total = numAttending * numPerPerson

# Calculate the minimum number of hot dogs needed.
minBuns = total // BUNS_PER_PACKAGE

# Determine if the number of people attending is large enough to require more than one package of buns
if minBuns > 0:
    # Calculate the number of buns left over from a package if any
    bunsLeft = total % BUNS_PER_PACKAGE

    # If there will be left overs add an additional bun
    if bunsLeft != 0:
        minBuns += 1
   # Set the minimum number of packages of hot dogs to one
else:
    minBuns = 1

# Determing the number of left over hot dogs, if any
bunsLeft = BUNS_PER_PACKAGE * minBuns - total

# Final totals

# Display the minimum number of hot dog packages needed
print (' Minimum packages of hot dogs needed:', minDogs)

# Display the minimum packages of hot dog buns needed
print('Minimum packages of hot dog buns needed:', minBuns )

#  Display the number of hot dogs left over
print(' Hot dogs left over: ', dogsLeft )

# Display the num er of hot dog buns left over3
print(' Hot dog buns left over:', bunsLeft)

