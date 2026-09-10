# Opgaver i Cyper Security: Tal og beregninger.
#I opgaverne nedenfor er det en god idé at gemme værdier i variabler og måske bruge f-strings til output. Husk også altid at input() som udgangspunkt er ren tekst så derfor er det nødvendigt at konvertere den indtastede værdi enten med int() eller float()

# Failsafe int input function
def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Failsafe float input function
def float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a float.")


#  Opgave A
#Spørg brugeren om hvor mange login-forsøg der blev registreret i system A og i system B og udskriv til slut det samlede antal forsøg.
systemA_login_attempts = int_input("Enter the number of login attempts in system A: ")
systemB_login_attempts = int_input("Enter the number of login attempts in system B: ")
total_login_attempts = systemA_login_attempts + systemB_login_attempts
print(f"Total login attempts: {total_login_attempts}")

# Opgave B
# Spørg brugeren om hvor mange mislykkede login-forsøg der var i går og i dag og udskriv forskellen mellem dem (i dag minus i går).
previous_login_attempts = int_input("Enter the number of login attempts in the previous day: ")
current_login_attempts = int_input("Enter the number of login attempts in the current day: ")
login_attempts_difference = abs(current_login_attempts - previous_login_attempts)
print(f"Login attempts difference: {login_attempts_difference}")

# Opgave C
#Spørg brugeren om hvor mange pakker der blev sendt og hvor mange der blev blokeret af firewallen og udskriv produktet af tallene.
sent_packets = int_input("Enter the number of sent packets: ")
blocked_packets = int_input("Enter the number of blocked packets: ")
product_packets = sent_packets * blocked_packets
print(f"Product of packets: {product_packets}")

# Opgave D
#Spørg brugeren om den samlede datamængde (MB) og tiden (sekunder) og udskriv den gennemsnitlige datahastighed (MB pr sekund).
data_volume = int_input("Enter the data volume (MB): ")
time_seconds = int_input("Enter the time (seconds): ")
average_speed = data_volume / time_seconds
print(f"Average speed: {average_speed} MB/s")


# Opgave E
# Spørg brugeren om antallet af angreb fra én IP-adresse og udskriv tallet opløftet i anden potens (dvs. vi simulerer belastning).
ip_attack_count = int_input("Enter the number of attacks from one IP address: ")
ip_attack_count_squared = ip_attack_count ** 2
print(f"IP attack count squared: {ip_attack_count_squared}")


# Opgave F
# Spørg brugeren om fem målinger af netværkstrafik (i MB) og udskriv gennemsnittet.
measurements = [int_input(f"Enter measurement {i + 1}: ") for i in range(5)]
average_measurement = sum(measurements) / len(measurements)
print(f"Average measurement: {average_measurement}")
