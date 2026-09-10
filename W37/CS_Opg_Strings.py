import ipaddress

print("Opgaver i Cyber Programmering – string funktioner")


#Opgave A (Opgave 23)
print("\nGem følgende loglinje i en variabel og udskriv den: 2026-01-01 10:15:23 LOGIN_FAILED user=admin ip=192.168.1.45")
log_line = "2026-01-01 10:15:23 LOGIN_FAILED user=admin ip=192.168.1.45"
print(log_line)

#Opgave B
print("\nUdskriv hvor mange tegn loglinjen fra opgave 23 indeholder ved hjælp af len().")
print(len(log_line))


#Opgave C
print("\nUdskriv loglinjen fra opgave 23 med kun store bogstaver.")
print(log_line.upper())


#Opgave D
print("\nUdskriv loglinjen fra opgave 23 med kun små bogstaver.")
print(log_line.lower())


#Opgave E
print("\nLad brugeren indtaste en loglinje og udskriv både loglinjen og dens længde.")
log_line = input("Indtast en loglinje: ")
print(log_line, len(log_line))


#Opgave F
print("\nLad brugeren indtaste et brugernavn og udskriv brugernavnet to gange lige efter: den ene gang kun med store bogstaver, den anden gang kun med små bogstaver.")
username = input("Indtast et brugernavn: ")
print(username.upper())
print(username.lower())


#Opgave G
# Function to keep asking for IP until it's a valid IP
def get_valid_ip():
    while True:
        ip = input("Indtast en IP-adresse: ")
        try:
            if ipaddress.IPv4Address(ip):
                return ip
        except ValueError:
            print("Ugyldig IP-adresse. Prøv igen.")

print("\nLad brugeren indtaste en IP-adresse som tekst og udskriv hvor mange tegn den indeholder.")
ip = get_valid_ip()
print(ip, len(ip))


#Opgave H
print("\nLad brugeren indtaste tre loglinjer og gem dem i tre variabler. Udskriv dem alle igen.")
log_a, log_b, log_c = input("Indtast loglinje A: "), input("Indtast loglinje B: "), input("Indtast loglinje C: ")
print(log_a, log_b, log_c)


#Opgave I
print("\nUdskriv de første 10 tegn af loglinjen fra opgave A (hvilken information giver det os?).")
print(log_line[:10])


#Opgave J
print("\nUdskriv de sidste 12 tegn af loglinjen fra opgave A (hvilken information giver det os?).")
print(log_line[-12:])

#Opgave K
print("\nLad brugeren indtaste en loglinje og udskriv de første 5 tegn (antag at disse tegn giver nyttig info).")
log_line = input("Indtast loglinje: ")
print(log_line[:5])


#Opgave L
print("\nLad brugeren indtaste en loglinje og udskriv både starten (første 8 tegn) og slutningen (sidste 8 tegn) i samme linje.")
log_line = input("Indtast loglinje: ")
print(log_line[:8], log_line[-8:])
