#OPGAVE 2 – KONTROL AF PORTNUMRE
#Et portnummer i TCP/IP kan være mellem 1 og 65535.
#Lav et program, som gentagne gange spørger brugeren:
#Enter port number or quit:
#Programmet skal stoppe, når brugeren skriver:
#quit
#Kontrollér først, om input er et tal.
#Hvis det ikke er et tal, udskrives:
#Invalid input
#Hvis det er et tal, skal det konverteres til int.
#Kontrollér derefter, om tallet ligger mellem 1 og 65535.
#Hvis det ikke gør, udskrives:
#Invalid port number

#Opret denne tuple:
common_ports = (22, 80, 443)

#Hvis det indtastede portnummer findes i common_ports, skal programmet skrive:
#Common port
#Ellers skal programmet skrive:
#Other valid port
#Eksempel:
#Enter port number or quit: 443
#Common port
#Enter port number or quit: 8080
#Other valid port
#Enter port number or quit: hello
#Invalid input
#Enter port number or quit: 70000
#Invalid port number
#Enter port number or quit: quit
#Program stopped

#Du får brug for:
#while
#input()
#isdigit()
#int()
#if / elif / else
#in
#tuple
#break

while True:
    user_input = input("Enter port number or quit: ")
    if user_input == "quit":
        break
    if not user_input.isdigit():
        print("Invalid input")
        continue
    port = int(user_input)
    if port < 1 or port > 65535:
        print("Invalid port number")
        continue
    if port in common_ports:
        print("Common port")
    else:
        print("Other valid port")
