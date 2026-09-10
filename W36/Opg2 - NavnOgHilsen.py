# Get username via input, split it by spaces, capitalize each word.
userName = input("Hvad er dit navn?").split()
userName = [word.capitalize() for word in userName]

# Print greeting using the capitalized username.
print("Hej med dig " + " ".join(userName) + ", rart at møde dig!")
