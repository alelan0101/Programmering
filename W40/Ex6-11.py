# 6-11. Cities: Make a dictionary called cities.
# Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city.
# The keys for each city’s dictionary should be something like country, population, and fact.
# Print the name of each city and all of the information you have stored about it.

cities = {
    'Randers': {
        'country': 'Denmark',
        'population': 60000,
        'fact': 'For bygning der kaldes, hundelorten.'
    },
    'Aarhus': {
        'country': 'Denmark',
        'population': 500000,
        'fact': 'Består udelukkende af ensrettet veje'
    },
    'Aalborg': {
        'country': 'Denmark',
        'population': 400000,
        'fact': 'Stor landsby'
    }
}

for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print()
