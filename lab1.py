#zad1
# imiona = ['Anna', 'Jan', 'Katarzyna', 'Michał', 'Anna', 'Tomasz', 'Maria', 'Jan', 'Magdalena', 'Piotr']
#
#
# nazwa_szukana = input("Podaj imię osoby, której indeks chcesz znaleźć: ")
# if nazwa_szukana in imiona:
#     indeks = imiona.index(nazwa_szukana)
#     print(f"Indeks osoby o imieniu {nazwa_szukana}: {indeks}")
# else:
#     print("Podane imię nie znajduje się na liście.")
#
#
# liczba_osob = imiona.count(nazwa_szukana)
# print(f"Liczba osób o imieniu {nazwa_szukana}: {liczba_osob}")
#
# nowe_imie_koniec = input("Podaj nowe imię do dodania na koniec listy: ")
# imiona.append(nowe_imie_koniec)
#
# nowe_imie_trzecie = input("Podaj nowe imię do dodania jako trzecią pozycję na liście: ")
# imiona.insert(2, nowe_imie_trzecie)
#
# imiona.sort()
# usuniety_element = imiona.pop()
#
# nowa_lista = ['Adam', 'Ewa', 'Paweł']
# imiona.extend(nowa_lista)
#
# print("Lista po wykonaniu operacji:")
# print(imiona)

#zad2
# dane_osobowe = {
#     'osoba1': {'imie': ['Anna'], 'nazwisko': ['Kowalska'], 'wiek': [30]},
#     'osoba2': {'imie': ['Jan'], 'nazwisko': ['Nowak'], 'wiek': [25]},
#     'osoba3': {'imie': ['Katarzyna'], 'nazwisko': ['Nowakowska'], 'wiek': [35]}
# }
# numer_osoby = input("Podaj numer osoby, której dane chcesz wyswietlic: ")
# if numer_osoby in dane_osobowe:
#     osoba = dane_osobowe[numer_osoby]
#     imie = osoba['imie'][0]
#     nazwisko = osoba['nazwisko'][0]
#     wiek = osoba['wiek'][0]
#     print(f"dane osoby {numer_osoby}:")
#     print(f"imię: {imie}")
#     print(f"nazwisko: {nazwisko}")
#     print(f"wiek: {wiek}")
# else:
#     print("Podany numer osoby nie istnieje.")
# #zad3
# kierunek_studiow = input("Podaj kierunek studiów: ")
#
# dane_osobowe['osoba1']['kierunek_studiów'] = [kierunek_studiow]
# dane_osobowe['osoba2']['kierunek_studiów'] = [kierunek_studiow]
# dane_osobowe['osoba3']['kierunek_studiów'] = [kierunek_studiow]
#
#
# print("Zaktualizowany słownik:")
# print(dane_osobowe)
# #zad4
# nazwy_kluczy = list(dane_osobowe['osoba1'].keys())
# print("Nazwy kluczy słownika:")
# print(nazwy_kluczy)
#
# # Oblicz ilość elementów w słowniku
# ilosc_elementow = sum(len(value) for value in dane_osobowe.values())
# print("Ilość elementów w słowniku:", ilosc_elementow)




#print(1+2+10+20000001+4+347586970885==321784560456434534646)
#x=(int(input('podaj wartosc x:')))
#y=(int(input('podaj wartosc y:')))
#wynik=2*x+5*y
#print(f"{wynik}")

## 3. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
##  gdzie : a-imie, a-nazwisko, c-liczba, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)

##imie=input('podaj imie;')
#nazwisko=input('podaj nazwisko:')
#wiek=int(input('podaj wiek:'))
#kierunek=input('podaj kierunek:')
#print(f"Jestem {imie} {nazwisko} mam {wiek} studiuje {kierunek}")

## 5. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą wyświetl właściwy komunikat
"""
x=int(input('podaj x:'))
y=int(input('podaj y:'))
suma=x+y
if suma%2==0:
 print("suma jest parzysta")
else:
 print("suma jest nieparzysta")
"""

## 6. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
## iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.
"""
x=int(input('podaj x:'))
y=int(input('podaj y:'))
operacja=input('podaj operacje:')
if operacja=='+':
 print(x+y)
if operacja=='-':
  print(x-y)
if operacja=='*':
  print(x*y)
if operacja=='/':
  print(x/y)
if operacja=='**':
 print(x**y)
 """
## 7. Dla dowolnego x sprawdź wynik działań (x > 1 and x < 13) oraz (x != 5 or x < 0)
#x=5
#print((x > 1 and x < 13) and  (x != 5 or x < 0))

#Użytkownik podaje imie, sprawdź czy to imie to Janusz lub Grażyna
"""
imie=input('podaj imie:')
if imie=='Janusz' or imie=='Grazyna':
    print('zgardza sie')
else:
    print('nie zgadza sie')
"""


"""
def generuj_sylaby(spolgloska):
    samogloski = ['a', 'e', 'i', 'o', 'u', 'y']

    for samogloska in samogloski:
        sylaba = spolgloska + samogloska
        print(sylaba)

spolgloska = input("Wpisz jedną spółgłoskę: ")

print(f"Sylaby z '{spolgloska}':")
generuj_sylaby(spolgloska)
"""