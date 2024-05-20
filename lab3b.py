#zad 0
# from Rozprawka import rozprawka
#
# print(f"Posąg Zeusa w Olimpii Miał 14 m wysokości."
#       f"{rozprawka()}"
#       f" Przedstawiał boga siedzącego na tronie. "
#       f"{rozprawka()}"
#       f" W jednej ręce trzymał statuę bogini Nike, w drugiej berło inkrustowane drogocennymi kamieniami. "
#       f"{rozprawka()}"
#       f"Na głowie miał wieniec z gałązek oliwnych, z lewego ramienia zwisał mu złoty płaszcz.")


#zad1
#
# from math import pow
# def funkcja(*args):
#      if len(args) == 1:
#          return pow(args[0], args[0])
#      elif len(args) == 2:
#          return pow(args[0], args[1])
#      else:
#          print("args ERROR")
#          return "args error"
# print(funkcja(8))

#zad2




# text = 'Wczytywanie do komputera tekstów, ilustracji, fotografii, itp. jest '   \
#        'możliwe dzięki urządzeniom zewnętrznym zwanym skanerami. Skaner to ' \
#        'urządzenie umożliwiające wprowadzenie do komputera grafiki i tekstu. ' \
#        'Dzięki zamianie skanowanej płaszczyzny na postać cyfrową może ona zostać ' \
#        'wyświetlona na ekranie monitora i zapisana na dysku w odpowiednim formacie ' \
#        'oraz może zostać poddana komputerowej obróbce. Skanery dzielimy na dwie podstawowe ' \
#        'grupy: ręczne (np. czytniki kodów paskowych) oraz stacjonarne. Najpopularniejszym ' \
#        'typem skanerów są skanery stacjonarne płaskie, które umożliwiają skanowanie ' \
#        'dokumentów o formacie A3 lub A4 i ich pochodnych. Są one podłączane do ' \
#        'komputerów przez port równoległy, uniwersalną magistralę szeregową lub sterownik SCSI.'
# def Wyrazy(text, *args):
#     look_in = (*args, 'komputer', 'skaner')
#     for word in look_in:
#         print(f"wyrazu {word} w teksie jest {text.count(word)}")
#
# Wyrazy(text, 'komputer', 'a')


#zad3

# def SredniaLiczb(*args):
#     if not args:
#         return "args ERROR"
#     else:
#         return sum(args) / len(args)
#
# print("Srednia liczb: 1, 2, 3, 4, 5, 6 =", SredniaLiczb(2, 3, 4, 5, 6))

#zad4






# def zdanie_rozdziel(tekst, rozdzielacz=",", pokaz_ilosc_fragmentow=True, pokaz_ilosc_wyrazow=True):
#     zdania = tekst.split(".")
#
#     if pokaz_ilosc_fragmentow == True:
#         for zdanie in zdania:
#             print(f"zdanie: {zdanie} ma {zdanie.count(rozdzielacz) + 1} '{rozdzielacz}'")
#     if pokaz_ilosc_wyrazow == True:
#         for zdanie in zdania:
#             print("ilość wyrazów w podanym tekście: ", len(zdanie.split(" ")))
# text = """Była sobie dziewczyneczka, hop sa sa, hop sa sa. Szła dzieweczka do laseczka, do zielonego, ha ha. Napotkała myśliweczka, hop sa sa. Tralala tralala."""
#
# zdanie_rozdziel(text, ".", True, True)

# zad 6




# from CiągGeometryczny import a, b
#
# print("an wyraz:", a(7, 3, 2))
# print("Suma:", b(10, 1, 3))

#zad7

# def dostawa_towaru(liczba_pracownikow=5, **kwargs):
#     print(f"Liczba pracowników: {liczba_pracownikow}")
#     print("Dostarczone produkty:")
#     for produkt, ilosc in kwargs.items():
#         print(f"{produkt}: {ilosc}")
#         if produkt in baza_danych:
#             baza_danych[produkt].append(ilosc)
#         else:
#             baza_danych[produkt] = [ilosc]
#
# baza_danych = {}
# dostawa_towaru(pomarańcze=15, gruszki=500, jabłka=200)
# dostawa_towaru(10, pomarańcze=15, gruszki=50, jabłka=20, śliwki=10)
# print(baza_danych.items())
# print(baza_danych.keys())
# print(baza_danych.values())

# zad 8

# import pola
#
# print("Pole prostokąta:", pola.area("prostokat"))
# print("Pole trójkąta:", pola.area("trojkat"))
# print("Pole kwadratu:", pola.area("kwadrat"))


#zad 9

# def dodaj_pole_kwadratu(func):
#     def wrapper(a, b=None):
#         if b is None:  # Sprawdzamy, czy drugi argument jest None
#             return a ** 2  # Jeśli tak, obliczamy pole kwadratu
#         else:
#             return func(a, b)  # W przeciwnym razie wykonujemy oryginalną funkcję
#     return wrapper
#
# @dodaj_pole_kwadratu
# def pole_prostokata(a, b):
#     return a * b
# @dodaj_pole_kwadratu
# def pole_trojkata(a, h):
#     return 0.5 * a * h
#
# # Dekorator dodający możliwość obliczenia pola kwadratu
#
#
# print("Pole prostokąta o bokach 3 i 4:", pole_prostokata(3, 4))
# print("Pole kwadratu o boku 5:", pole_prostokata(5))
# print("Pole trójkąta o podstawie 3 i wysokości 4:", pole_trojkata(3, 4))
# print("Pole kwadratu o boku 5:", pole_trojkata(5))
#zad10

# def dekorator(func):
#     def wrapper(username, password, **kwargs):
#         zmienna = func(username, password)
#         zmienna.update(kwargs)
#         return zmienna
#     return wrapper
#
# @dekorator
# def logowanie(user = "edek2003", password = "Wsx123"):
#     return {"user": user, "password": password}
#
# print(logowanie("imie","haslo",host = "www.google.com", port = "USB-C"))
#zad11
def dec(func):
    def wrapper(*args):
        n, a1, q = args
        suma = a1 * (1 - q ** n) / (1 - q) if q != 1 else n * a1
        print(f"Suma {n} elementow wynosi: {suma}")
        return func(*args)
    return wrapper

@dec
def ciag_geometryczny(n, a1=1, q=2):
    an = a1 * (q ** (n - 1)) if a1 != 1 else a1
    return an

n = 5
a1 = 1
q = 2

# Wywołanie funkcji z dekoratorem
an = ciag_geometryczny(n, a1, q)
print(f"{n}-ty element ciągu wynosi: {an}")
