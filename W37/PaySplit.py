# Application that splits the bill on a restuarant between a given amount of paying customers
# User values should be fetched via input()
# User should be asked if they want to pay a tip, as a percentage of the bill

# A failsafe function to receive ints via input
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ugyldigt input. Prøv igen.")

# A failsafe function to receive floats via input
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ugyldigt input. Prøv igen.")

# Get the number of guests
numGuests = get_int("Hvor mange gæster er der? ")

# Get the bill amount
billAmount = get_float("Hvad er beløbet? ")

# Get the tip amount
tipAmount = get_float("Hvor stor tip vil du give, i procent af beløbet? ")

tipAbsoluteAmount = billAmount * tipAmount / 100

# Calculate the amount each guest should pay
amountPerGuest = (billAmount + (billAmount * tipAmount / 100)) / numGuests

# Print the amount each guest should pay
print("Beløbet er " + str(billAmount) + " kr. og tip er " + str(tipAbsoluteAmount) + " kr. (" + str(tipAmount) + "%, af beløbet). Hver gæst skal betale " + str(amountPerGuest) + " kr.")
