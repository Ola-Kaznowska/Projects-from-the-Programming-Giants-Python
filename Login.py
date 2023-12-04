login = "login"
haslo = "haslo"


if login == 'login' and haslo == "haslo":
    print("Podałeś dobre dane, zapraszam")
    pass
elif login !='login' and haslo == "haslo":
    print("Błędny login")
    pass
elif login == 'login' and haslo != 'haslo':
    print("Błędne hasło")
    pass
else:
    print("Nie rozumiem")
    pass
    