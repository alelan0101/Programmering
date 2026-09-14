# Opgave Brugere og aldre med statistik
# I denne opgave skal løse disse underopgaver:

# Først laves en liste med 8 fornavne på personer (gemt som strings)
names = ['John', 'Jane', 'Bob', 'Alice', 'Mike', 'Sarah', 'David', 'Emily']


# Nu skal I lave en ny tom liste (der senere skal indeholde tal).
ages = []

# I denne liste skal brugernes alder, (indtastes fra tastaturet) placeres (Husk at konvertere tekst til int).

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ugyldigt input. Prøv igen.")


for name in names:
    age = get_int(f"Enter age for {name}: ")
    ages.append(age)


# Programmet skal nu udregne gennemsnittet af brugernes alder.
average_age = sum(ages) / len(ages)

# Til slut skal udskrives en oversigt over brugere og aldre (brug print-f) samt gennemsnittet.
for name, age in zip(names, ages):
    print(f"{name}: {age}")
print(f"Gennemsnit: {average_age}")


#Opgave Fejlslagne ”login-attempts” på én server hver dag i en uge
#Lav først en liste med navnene på de 7 ugedage, derefter:

days = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]

#I en loop: indlæs antallet af ”attempts” for hver dag i ugen (fra tastaturet). Bemærk hver indlæst værdi skal over i en ny liste som tal, hvilket jo kræver konvertering.
attempts = []
for day in days:
    attempt = get_int(f"Enter number of login attempts for {day}: ")
    attempts.append(attempt)


#Programmet nu lave en del beregninger: summen af alle attemps i hele ugen. Gennemsnittet af attempts pr. dag.
total_attempts = sum(attempts)
average_attempts = total_attempts / len(attempts)


#Svær:
#I skal også finde (og udskrive) den ugedag hvor der var færrest og den ugedag hvor der var flest attempts (hint: man loope igennem hele listen og gemme det hidtil største mindste antal loginforsøg. Man kan også prøve at bruge indbygget funktion kaldet min() hhv max. Udfordringen er stadig at finde (og udskrive) ugedagen hvor det sker

least_attempts = attempts[0]
most_attempts = attempts[0]
for i in range(1, len(attempts)):
    least_attempts = min(least_attempts, attempts[i])
    most_attempts = max(most_attempts, attempts[i])

least_day = days[attempts.index(least_attempts)]
most_day = days[attempts.index(most_attempts)]


#Til slut skal der udprintes oversigter hvor man kan se dag-for-dag hvad der er sket + de udregnede statistiske værdier. Her kan I bruge print-f-kommandoen.
print(f"Total attempts: {total_attempts}")
print(f"Average attempts: {average_attempts}")
print(f"Least attempts: {least_attempts} on {least_day}")
print(f"Most attempts: {most_attempts} on {most_day}")
