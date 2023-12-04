print("Kalkulator średniej")

print("---------------------------------------------")



Pol = int(input("Podaj swoją ocenę z Polskiego: "))
Inf = int(input("Podaj swoją ocenę z Informatyki: "))
Mat = int(input("Podaj swoja ocenę z Matematyki: "))
Ang = int(input("Podaj swoją ocene z j. Angielskiego: "))
Biol = int(input("Podaj swoją ocenę z Biologi : "))


srednia = (Pol+Inf+Mat+Ang+Biol) / 5

print(f"Twoja średnia ocen wynośi {srednia}")

if srednia >= 5:
    print("Dostajesz nagrodę od dyrektora! :)")
    
else:
    print("Kto się pilnie uczył ten z radości skacze a leniuszek i oróźnaczek niech sobie popłacze.")







