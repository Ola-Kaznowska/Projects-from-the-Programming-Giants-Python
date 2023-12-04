# Zadanie rozgrzewkowe
# Napisz program, który zapyta użytkownika o N ocen cząstkowych, a następnie
# wyliczy średnią z przedmiotu.
# N - liczba ocen wprowadzona przez użytkownika na początku działania programu
# Dodatkowa część:
# Następnie wyświetli ocenę końcową z przedmiotu jako zaokrąglenie średniej do
# całości.


N = int(input("Podaj liczbę ocen: "))
suma = 0
for i in range(N):
    a = float(input("Podaj ocenę: "))
    suma += a
    
    srednia = suma/N  
