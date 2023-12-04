imie = input("Jak masz na imię?: ")
nazwisko = input("Jak masz na nazwisko?: ")
rok = int(input("W którym roku się urodziłeś/aś?: "))
miesiac = int(input("W  jakim miesiącu się urodziłęś/aś: "))
wiek = abs(rok - 2023)

print(f"Masz na imię {imie}, a na nazwisko {nazwisko}, urodziłeś/aś się w roku {rok}, w miesiacu {miesiac}, masz lat {wiek}")