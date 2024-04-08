from globals import *
def oblicz_pole_prostokata(a, b):
    return a * b
def oblicz_pole_trojkata(a, h):
    return 0.5 * a * h


def oblicz_pole_figur(geometry):
    if geometry == 'prostokat':
        return oblicz_pole_prostokata(bok_prostokata, bok_prostokata)
    elif geometry == 'trojkat':
        return oblicz_pole_trojkata(podstawa_trojkata, wysokosc_trojkata)
    elif geometry == 'kwadrat':
        return oblicz_pole_prostokata(bok_kwadratu, bok_kwadratu)



