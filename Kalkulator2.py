#poproś użytkownika o dwie liczby
l1 = int(input("Pierwsz liczba: "))
l2 = int(input("Druga liczba: "))
#zapytaj jakie działanie chce wykonać 
print("+ dodawanie\n- odejmowanie\n* mnożenie\n/ dzielenie")
i = input()
#(wpisanie + powoduje dodawanie, - to odejmowanie itd itd)
if i == "+":
    print(l1 + l2)
    pass
#else:
#    print("Nie rozumiem")
elif "-" in i:
    print(l1 - l2)
    pass
elif "*" in i:
    print(l1*l2)
    pass
elif "/" in i:
    
    print(l1/l2)
    pass
else:
    print("Nie")