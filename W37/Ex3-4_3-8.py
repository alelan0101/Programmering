import random

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

print("\n#############################################")
print("Dinner invitations for a friendly get-together!")
print("#############################################\n")

guests = ["Hitler", "Stalin", "Churchill"]

# Greet function
def send_invitation(guest):
    print("\nHello Mr. " + guest + "!\nYou are hereby invited to a dinner about a fun and lively conversation about the past.\nYour presence is highly appreciated, and should bear ripeful fruits for everyone!.\n")

# Send invitations
for guest in guests:
    send_invitation(guest)

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.

#Pick random guest that cant make it and print
unavailable_guest = random.choice(guests)
print("\nUnfortunately, " + unavailable_guest + " can't make it.")

#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

#Pool of potential new guests
new_guests = ["Roosevelt", "Mussolini", "Mao", "Hirohito", "Patton", "Zhukov", "Erwin Rommel", "MacArthur", "Bradley", "Ridgway"]

#Replace the unavailable guest with a new guest from the pool
guests[guests.index(unavailable_guest)] = random.choice(new_guests)

#Print a second set of invitation messages, one for each person who is still in your list.
for guest in guests:
    send_invitation(guest)

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
print("\n#############################################")
print("We found a bigger table!")
print("#############################################\n")

# Remove the already added new guests from the list of new_guests
for guest in new_guests:
    if guest in guests:
        new_guests.remove(guest)

# Use insert() to add one new guest to the beginning of your list.
guests.insert(0, random.choice(new_guests))
new_guests.remove(guests[0])

# Use insert() to add one new guest to the middle of your list.
guests.insert(len(guests) // 2, random.choice(new_guests))
new_guests.remove(guests[len(guests) // 2])

# Use append() to add one new guest to the end of your list.
guests.append(random.choice(new_guests))
new_guests.remove(guests[-1])

# Print a new set of invitation messages, one for each person in your list.
for guest in guests:
    send_invitation(guest)

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.

# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
print("\n#############################################")
print("We can only invite two people for dinner.")
print("#############################################\n")

# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
while len(guests) > 2:
    popped_guest = guests.pop()
    print("Sorry, " + popped_guest + ", due to table space limitations, you are hereby removed from the guest list.")

# Print a message to each of the two people still on your list, letting them know they're still invited.
for guest in guests:
    print("You're still invited, " + guest + ".")

# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
del guests[:]
print(guests)
