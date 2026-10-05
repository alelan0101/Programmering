#OPGAVE 1 – KONTROL AF LOGIN-FORSØG
#Du skal lave et lille program, der spørger brugeren om antallet af mislykkede login-forsøg.
#Programmet skal blive ved med at spørge, indtil brugeren skriver:
#quit
#Eksempel:
#Enter number of failed logins or quit: 2
#2 failed login attempts
#Enter number of failed logins or quit: 7
#Warning: Many failed login attempts
#Enter number of failed logins or quit: quit
#Program stopped
#Programmet skal kontrollere brugerens input.
#Kun heltal mellem 0 og 20 er gyldige.
#Hvis brugeren skriver tekst i stedet for et tal, skal programmet skrive:
#Invalid input
#Hvis brugeren skriver et tal mindre end 0 eller større end 20, skal programmet skrive:
#Number must be between 0 and 20
#Hvis tallet er 5 eller højere, skal programmet skrive en advarsel:
#Warning: Many failed login attempts
#Ellers udskrives antallet af login-forsøg.
#Du får brug for:
#while
#input()
#isdigit()
#int()
#if / else
#break

while True:
    user_input = input("Enter number of failed logins or quit: ")
    if user_input == "quit":
        break
    if not user_input.isdigit():
        print("Invalid input")
        continue
    num_failed_logins = int(user_input)
    if num_failed_logins < 0 or num_failed_logins > 20:
        print("Number must be between 0 and 20")
        continue
    if num_failed_logins >= 5:
        print("Warning: Many failed login attempts")
    else:
        print(num_failed_logins, "failed login attempts")
