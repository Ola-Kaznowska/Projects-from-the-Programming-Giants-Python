import time
oceny = []
while True:
    ocena = input("Podaj ocenę lub wpisz 'Koniec': ")
    if ocena == "Koniec":
        break
    else:
        oceny.append(int(ocena))

print("Wprowadzone oceny to:", end=" ")
for i in range(len(oceny)):
    if i == len(oceny) - 1:
        print(oceny[i])
    else:
        print(oceny[i], end=", ")

srednia = sum(oceny) / len(oceny)
time.sleep(1)
print(f"Średnia ocen wynosi: {srednia}")

input("Czy jesteś zadowolony/na z swoich ocen? Proszę podać odp jeśli chcesz :D : ")

tak = "tak"
nie = "nie"

if tak == "tak":
    time.sleep(2)
    print("Super. Jest Git ;P")

if nie == "nie":
    time.sleep(2)
    print("Szkoda:/ Ale był to tylko wybór dodatkowy :)")
else: 
    time.sleep(2)
    print("Dziękujemy za skozystanie z naszego programu.")  
    