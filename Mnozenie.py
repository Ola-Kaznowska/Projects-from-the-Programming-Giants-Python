oceny =[3, 4, 2, 4]

wynik = 1

for i in oceny:
    #iterując po liście i jest równe każdemu 
    #elementowi listy po kolei
    wynik *= i
    print(i)
    pass

while i < len(oceny):
    i +=1
    wynik = 2
    print(oceny)
pass

if 5 in oceny:
    print("Dobrze dla ciebie :)")