#
# Crystal Egbert
# 2/22/2025
# Kilometer Converter Programming Project
# COSC 1010
#
 
# Variables
conversion_formula = 0.6214

# Enter miles per hour to be converted
def main ():
    # Get the distance in kilomters.
    kilometers = float(input("Enter a distance in kilometers: "))
    
    # Display distance after conversion
    show_miles(kilometers)

# Define show_miles
def show_miles(km):

    # Run calculation
    miles = km * conversion_formula

    # Display miles
    print (km, "kilometers equals", miles, "miles")

# Call to action
main ()