#OPGAVE 4 – SIKKERHEDSHÆNDELSE
#Vi kan repræsentere en simpel sikkerhedshændelse med en tuple:
event = ("192.168.1.25", "failed_login", 5)
#Tuplen indeholder:
#IP-adresse
#Type af hændelse
#Antal forsøg
#Udskriv de tre værdier hver for sig.
for value in event:
    print(value)

#Lav derefter en betingelse:
#Hvis event[1] er "failed_login" og event[2] er mindst 3, skal programmet udskrive:
#Warning: Multiple failed login attempts
#Ekstra: Udskriv også den IP-adresse advarslen kommer fra.
if event[1] == "failed_login" and event[2] >= 3:
    print("Warning: Multiple failed login attempts")
    print("Ekstra: Udskriv også den IP-adresse advarslen kommer fra.")
    print(event[0])
