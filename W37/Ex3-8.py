print("3-8. Seeing the World: Think of at least five places in the world you'd like to visit.\n")

# Store the locations in a list. Make sure the list is not in alphabetical order.
locations = ['Paris', 'Tokyo', 'New York', 'Sydney', 'London']

print("Print your list in its original order. Don't worry about printing the list neatly; just print it as a raw Python list.")
print(locations)
print()

print("Use sorted() to print your list in alphabetical order without modifying the actual list.")
print(sorted(locations))
print()

print("Show that your list is still in its original order by printing it.")
print(locations)
print()

print("Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.")
print(sorted(locations, reverse=True))
print()

print("Show that your list is still in its original order by printing it again.")
print(locations)
print()

print("Use reverse() to change the order of your list. Print the list to show that its order has changed.")
locations.reverse()
print(locations)
print()

print("Use reverse() to change the order of your list again. Print the list to show it's back to its original order.")
locations.reverse()
print(locations)
print()

print("Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed.")
locations.sort()
print(locations)
print()

print("Use sort() to change your list so it's stored in reverse-alphabetical order. Print the list to show that its order has changed.")
locations.sort(reverse=True)
print(locations)
print()
