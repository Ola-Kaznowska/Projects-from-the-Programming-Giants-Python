# 5. Cena atrakcji turystycznej zależy od miesiąca. Napisz program, który zapyta
# użytkownika o liczbę biletów oraz miesiąc, w którym chce odwiedzić park
# rozrywki i na tej podstawie obliczy koszt transakcji.
# Koszt biletu w danym miesiącu (miesiąc jako numer -> koszt biletu):
# - 1 -> 50 zł
# - 2 -> 50 zł
# - 3 -> 100 zł
# - 4 -> 100 zł
# - 5 -> 200 zł
# - 6 -> 200 zł
# - 7 -> 250 zł
# - 8 -> 200 zł
# - 9 -> 200 zł

# - 10 -> 100 zł
# - 11 -> 100 zł
# - 12 -> 50 zł
# Wyświetl komunikat:
# "Cena biletów: XX zł"
# XX to wartość li
# czbowa



miesiac = int(input("Podaj  liczbę miesiąca w którym wyjeżdzasz na wakację: "))
liczba = int(input("Podaj liczbę biletu(ów): "))

miesiace = [50,50,100,100,200,200,250,200,200,100,100,50]
if miesiac > 0 and miesiac <= 12:
    cena = miesiace[miesiac -1] * liczba
    


print(f"Zarezerwowano {liczba} bilet(ów) na  {miesiac} koszt biletu(ów) to {cena}. Życzymy udanych wakacjii:)")