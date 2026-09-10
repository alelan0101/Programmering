# Paysplit V2
# Applikation der splitter regningen mellem gæster
#
#  Vi bruger en ny version af et for-loop til huske et varierende antal gæsters navne. Først skal brugeren altså indtaste hvor mange gæster der er i alt. Og senere skal navnene på gæsterne gemmes (ét navn ad gangen)
#  Man kan arbejde med kode der ser sådan ud: (dette loop gennemløbes præcis 5 gange - udfordringen er at bruge antallet af gæster til at begrænse loop’et).
# for x in range(1,5):
#     print(x)

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

# Antal gæster
num_guests = int_input("Enter the number of guests: ")

# Regningens løb
total_bill = float_input("Enter the total bill: ")

# Tip i procent
tip_percent = float_input("Enter the tip percentage: ")

# Udreg tip mængde
tip_amount = total_bill * (tip_percent / 100)

# Det fulde beløb
total_amount = total_bill + tip_amount

# Betaling pr. gæst
payment_per_guest = total_amount / num_guests

# Navn på alle gæsterne og print resultat i loop
for i in range(1, num_guests + 1):
    guest_name = input(f"Enter the name of guest {i}: ")
    print(f"{guest_name} part of the bill {payment_per_guest:.2f}")
