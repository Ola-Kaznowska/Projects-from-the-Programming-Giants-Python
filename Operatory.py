a = 3
b = 5 



a<b #znak mniejszości
#zwraca True jeżeli a jest mniejsze od b
#a False jeżeli a jest większe

a<=b #znak "nie większe"
#różnica jest taka że może być równe

a>b 

a>=b


print(56 < 26)
print(56 <= 56)

a == b #sprawdzamy czy są równe i dostajemy True albo False
a = b #PRZYPISUJEMY wartość b do zmiennej a
a != b 

#not
not 56 < 27
#czy 56 NIE jest mniejsze od 27
not 27 <= 56
#zwróci False
not (2 < 0) #cały nawias daje w rezultacie boola

#and
(3 > 0) and (4 < 8) #to zwraca True jeżeli OBA WARUNKI DAJĄ TRUE



#or

(3 < 0) or (2 < 3) #To zwrace True jeżei co najmniej 1 warunek daje True




print(12 > 15) # Fałsz # ==, <, !=, <=
print(5 < 15000) # Prawda # ==, >, >=, <=
print(120 != 120) # Fałsz # ==, >=, !=, <=
print(60 < 15) # Fałsz # ==, <, !=, >=
print(25.3421 <= 25.3421) # Prawda # ==, <, !=, <=



#4. Czy wolno mi lub innej osobie skorzystać z rollercoastera w parku rozrywkiMój wzrost to 175 cm. Na kolejkę wpuszcza się osoby wyższe niż 150 cm.Które osoby mogą skorzystać z kolejki? 115 cm, 149 cm, 150 cm, 151 cm, 210 cm.



print(175 > 150)

print(115 > 150)
print(149 > 150)
print(150 > 150)
print(151 > 150)
print(210 > 150)