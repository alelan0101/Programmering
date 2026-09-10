def IntOnlyInput(query: str) -> int:
    while True:
        try:
            result = input(query)
            return int(result)
        except ValueError:
            print("Det er desvaerre ikke et nummer, proev igen!")

nr1 = IntOnlyInput("Foerste nummer")
nr2 = IntOnlyInput("Andet nummer")

print("For tallene " + str(nr1) + " og " + str(nr2) + ", er summen: " + str(nr1+nr2) + ", forskellen er " + str(abs(nr2-nr1)) + ", produktet er " + str(nr1*nr2))
