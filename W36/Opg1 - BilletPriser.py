def IntOnlyInput(query: str) -> int:
    while True:
        try:
            result = input(query)
            return int(result)
        except ValueError:
            print("Det er desvaerre ikke et nummer, proev igen!")

billetPris: int = IntOnlyInput("Hvad er prisen for en billet?")
fuldePris = billetPris * 3
print("Det bliver " + str(fuldePris) + ", tak!")
