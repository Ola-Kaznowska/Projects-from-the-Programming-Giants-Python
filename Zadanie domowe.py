import random

plik = open("historie.txt", "a")
plik.close()


plik = open("historie.txt", "r")
menu = ["Nowa historyjka", "Wyświetl historię", "Koniec"]
historie = plik.readlines()
plik.close()
for i in range(len(historie)):
    historie[i] = historie[i].replace("\n," "")



czy_koniec = False

czynnosc = ["wizyta", "wycieczka", "gotowanie", "walka", "lot"]
gdzie = ["w samolocie", "na plaży", "na rynku", "w górach"]
kiedy = ["wczoraj", "w średniowieczu" , "jutro", "kiedy po źiemi chodziły dinozaury"]
z_kim = ["z kolegą", "z szewczykiem dratewką", "ze starszą panią", "ze smokiem"]
po_co = ["po chwałę", "po bogadctwo", "po dobry humor", "po złote skarpety"]



lista_list = [czynnosc, gdzie, kiedy, po_co, z_kim]
lista_naglowkow = ["co", "gdzie", "kiedy", "po co"]
while not czy_koniec:
    for i in range(len(menu)):
        print(f"{i+1}. {menu[1]}")
    wybor = int(input("Podaj wybór: "))
    if wybor == 1:
        czy_wylosowano_poprawnie = False
        while not czy_wylosowano_poprawnie:
            print("Nowa historia")
            for i in range(len(lista_naglowkow)):
                obecna_lista = lista_list[i]
                dlugosc_listy = len(obecna_lista)
                wylosowane = obecna_lista[random.randrange(0, dlugosc_listy)]
                print(f"{i+1}.{lista_naglowkow[i]}: {wylosowane}")
            print("Czy akceptujesz wylosowane informacje?")
            print("1. Akceptuje losowanie")
            print("2. Losuj ponownie")
            opcja_historii = int(input("Podaj wybór: "))
            if opcja_historii == 1:
                czy_wylosowano_poprawnie = True
            elif opcja_historii == 2:
                czy_wylosowano_poprawnie = False
       
       
        historyjka = input("Ułóż historię: ")
        historie.append(historyjka)
    elif wybor == 2:
        print("Wyświetl Historię")
        for i in range(len(historie)):
            print(f"{i+1}. {historie[i]}")
    elif wybor == 3:
        print("Koniec programu")
        plik = open("historie.txt", "w")
        for linia in historie:
            plik.write(linia+'\n')
        plik.close()
        czy_koniec = True
    else:
        print("Zły wybór")