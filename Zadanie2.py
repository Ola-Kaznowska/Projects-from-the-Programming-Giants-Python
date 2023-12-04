"""
Zapytaj użytkownika o 10 liczb 
Jeżeli jakaś się powtórzy to poproś go jeszcze raz
a jeżeli nie to dołącz ją do listy
"""


liczby = []

while len(liczby) < 10:
    a = int(input("Podaj liczbę: "))
    
    if a in liczby:
        print("NIE POWTARZAJ SIĘ")
        pass
    else:
     liczby.append(a) #Dołączenie elementu a do listy
     pass
pass 