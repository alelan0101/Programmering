#Opgave 1 Byer
#Lav en liste med mindst 8 forskellige byer.
byListe = ['Esbjerg', 'Aarhus', 'Odense', 'København', 'Aalborg', 'Vejle', 'Rudersdal', 'Horsens']

#Brug slices til at udskrive:
#De første tre byer
print(byListe[:3])
#De sidste tre byer
print(byListe[-3:])
#Tre byer fra midten
print(byListe[3:6])
#Lav derefter et loop som kun gennemløber de første fire byer.
for by in byListe[:4]:
    print(f'I would like to visit {by}')

for by in byListe:
    print(f'I would like to visit {by}')
