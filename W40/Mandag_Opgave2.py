#OPGAVE 2 – IP-ADRESSE SOM TUPLE
#En IPv4-adresse består af fire tal.
#Opret IP-adressen 192.168.1.25 som en tuple:
ip = (192, 168, 1, 25)
#Udskriv hele tuplen.
print(ip)

#Udskriv kun det første tal.
print(ip[0])

#Udskriv kun det sidste tal.
print(ip[-1])

#Brug et for-loop til at udskrive alle fire tal.
for tal in ip:
    print(tal)


#Prøv til sidst:
ip[3] = 30

#Hvad sker der? Forklar hvorfor.
# Det sidste tal i tuplen ændres ikke, da tupler er immutable (fremfor at de er mutable som lister).
