#
#Crystal Egbert
# 2/22/2025
# Feet to Inches Programming Project
# COSC 1010
#
# Variables
inches = 12

# Get the number of feet.
def main():

    # Get number of feet
    feet = int(input("Enter the number of feet: "))

    # Convert feet to inches
    print(feet, "feet is" , feet_to_inches (feet), "inches.")

# Convert feet_to_inches function
def feet_to_inches(feet):
    return feet * inches

    #call the main
main()

