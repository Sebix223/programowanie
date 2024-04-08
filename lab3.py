#zad1
# while True:
#     liczba1=int(input("podaj liczbe:"))
#     liczba2=int(input("podaj druga liczbe:"))
#     liczba1*=liczba2
#     print(f"iloczyn= {liczba1}")
#     if liczba1 <=0 or liczba2 <=0:
#         break

#zad2 i 4
# haslo=("123","223")
#
# wprowadzon_haslo=input("podaj haslo:")
# print("sebastian rosicki") if wprowadzon_haslo in haslo else print("podano nie poprawne haslo")

#zad3
# import random
# lista=[random.randint(1,1000)for liczba in range(100)]
#
# liczby_parzyste=[liczba for liczba in lista if liczba %2==0]
# liczby_parzyste.sort()
#
# for liczba in liczby_parzyste:
#     print(liczba)


#zad5
# def funkcja(a,b,c):
#     return a/b/c if all(x%2==0 for x in [a,b,c]) else None
#
# print(funkcja(2,4,6))

#zad6
# imie=['s','e','b','a']
# cale_imie=''.join(map(lambda x:x,imie))
# print(cale_imie)

#zad7
# imie_nazwisko="Sebastian Rosicki"
#
# slowa=lambda x: x.split()
# litery=lambda x: [list(word) for word in x.split()]
# print("slowa: ",slowa(imie_nazwisko))
# print("litery:",litery(imie_nazwisko))

#zad8
# szukana_litera=lambda slowo, litera:litera in slowo
# slowo="Rewolwerowiec"
# litera="p"
# if szukana_litera(slowo, litera):
#     print(f"litera '{litera}' w slowie '{slowo}'")
# else:
#     print(f"litera '{litera}' nie ma w slowie '{slowo}'")

#zad9


loginy = []
haslo = []
while True:
    login = input("wpisz login: ")
    password = input("wpisz haslo: ")
    if login.lower() == 'stop' or password.lower() == 'stop':
        break
    if login in loginy:
        continue
    if password in haslo:
        continue
    loginy.append(login)
    haslo.append(password)
dict_log_pass = dict(zip(loginy, haslo))

#zad10

# Poziom(3)
# Pion(2)
# Poziom(3)
# Pion(2)
# Poziom(3)
# print("\n")
# Pion(6)
# Poziom(3)


#zad11
# from sil import silnia
#
# n = float(input("wpisz liczba: "))
# k = float(input("wpisz liczba: "))
# if k > n:
#     print("Nie da sie tak")
# else:
#     print(f"({n} {k}) = {n}!/({k}!*{n-k}!)  == {silnia(n)/(silnia(k)*silnia(n-k))}")

#zad12
# numer = [x for x in range(1, 100)]
# numer_filter = list(filter(lambda x: True if x % 2 == 0 else False, numer))
# print(numer_filter)

#zad13
# import functools
#
# numer = functools.reduce(lambda x, y: x * y, [x for x in range(1, 100)])
#zad14

# numbers_filtered = list(filter(lambda number: True if number % 7 == 0 and number % 5 != 0 else False, [x for x in range(2000, 3201)]))
# print(numbers_filtered)






