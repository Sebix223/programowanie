#zad1
"""
set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
                 'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3','GALNT14', 'ERCC11',
                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
                'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])

print(set_gene1.intersection(set_gene2,set_gene3))
geny_dla_1i2=set_gene1.intersection(set_gene2)
geny_dla_1i3=set_gene1.intersection(set_gene3)
geny_dla_3i2=set_gene2.intersection(set_gene3)
print(f"dla 1 i 2: {geny_dla_1i2}")
print(f"dla 1 i 3: {geny_dla_1i3}")
print(f"dla 3 i 2: {geny_dla_3i2}")
geny_dla_1=set_gene1.difference(set_gene2, set_gene3)
print(f"{geny_dla_1}")
"""
#zad2
"""
lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                 'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']

for element in lista_gene1:
     print(element is 'FGFR4')
print(lista_gene1.index('FGFR4'))
"""
"""
word='''Twórca Emmy, start-up o nazwie Stealth, nazywa ją „niezależną sztuczną inteligencją” zaprojektowaną, by świadczyć profesjonalne usługi,
      takie jak badania i analiza. Odkąd w modzie są prognozy, że sztuczna inteligencja (ang. artificial intelligence, AI) zastąpi pracowników biurowych,
      w tym również dziennikarzy, chciałam to sprawdzić na własnej skórze.
      Emma rzeczywiście była szybka – dane wysłała w 12 minut. Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam.
      Fakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu (choć podzielała wątpliwą opinię, że wyjście z
      Unii Europejskiej byłoby niezwykle korzystne dla brytyjskiej gospodarki).'''



print(word.count('Emma'))
print(word.upper())

print(word.split())
zdania=word.split('.')
zdania = [zdanie.strip() for zdanie in zdania if zdanie.strip()]
print(f"liczba zdan:{len(zdania)}")
"""
"""
x=int(input("podaj liczbe:"))
if x%2==0:
    print(f"liczba {x} jest parzysta.")
else:
    print(f"liczba {x} jest nie parzysta.")
    """

########Zadanie 5
## W zależności od procentu uzyskanych punktów z kolokwium z Python'a
## student uzyskuje określoną ocenę końcową z laboratorium
## np 50%-60% to 3.0, 61%-70% to 3.5, ...., 91%-100% to 5.0
## Korzystając z instrukcji match, napisz program który będzie
# wyznaczał ocenę studenta na podstawie uzyskanych punktów (max 15pkt)
"""
def oblicz_ocene(punkty):
    match punkty:
        case 0|1|2|3|4|5|6|7:
            return 2.0
        case 8|9:
            return 3.0
        case 10 | 11:
            return 3.5
        case 12 | 13:
            return 4.0
        case 14:
            return 4.5
        case 15:
            return 5.0
uzyskane_punkty=int(input("podaj uzyskana liczbe punktow: "))

ocena_koncowa=oblicz_ocene(uzyskane_punkty)
print(f"ocena koncowa: {ocena_koncowa}")
"""
#zad6
n=int(input("podaj wartosc n:"))
suma=2
for i in range(1,n+1):
    suma=suma/(i+2)
print(f"suma ciagu dla n={n} to :{suma}")
#zad7
"""
import math
liczba=1

while liczba<=10:
    pierwiastek=math.sqrt(liczba)
    print(f"{pierwiastek}")
    liczba+=1

import cmath
def oblicz_pierw(a,b,c):
    detla=b**2-4*a*c
    pierwiastek1=(-b-cmath.sqrt(detla))/(2*a)
    pierwiastek2=(-b+cmath.sqrt(detla))/(2*a)
    return pierwiastek1,pierwiastek2
a=1
b=-3
c=2

pierwiastki=oblicz_pierw(a,b,c)
print(f"{pierwiastki} ")
"""


























