# zad1
import os

# def zmiana(path):
#     os.chdir(path)
#     print(os.listdir(path))
#
# zmiana("C:\\Users\\sebar\\")

# zad2
# import os
# def zmiana(path):
#     while True:
#         pyt=input("czy mam zmienic katalog?")
#         if pyt=="yes":
#             os.chdir(path)
#             print(os.listdir(path))
#             break
#         else:
#             continue
# zmiana("C:\\Users\\sebar\\")

# zad3
# path=os.path.join(os.getcwd(),'dokument')
# os.chdir(path)
# if not os.path.exists('dokument'):
#     os.mkdir("dokument")
# else:
#     print("ERROR Directory already exsist")
# Lista = ["lab1.doc", "lab2.doc", "lab3.doc"]
# for i,filename in enumerate(Lista,start=1):
#     with open(filename,"w") as file:
#         pass
#
#
# print(*os.listdir("."))
# a=list(filter(lambda a:True if a.endswith(".doc")else False,os.listdir(".")))
# print(a)

# zad4


# if not os.path.exists("studentDoc"):
#     os.mkdir("studentDoc")
#     os.mkdir("studentobrazy")
# else:
#     print("Error directory already exsist")
#
# path1=os.path.join(os.getcwd(),'studentDoc')
# path2=os.path.join(os.getcwd(),'studentobrazy')
#
# with open(os.path.join(path1, "pies1.txt"),"w") as file:
#     pass
# with open(os.path.join(path1, "pies2.txt"),"w") as file:
#     pass
# with open(os.path.join(path2, "kot.jpg"),"w") as file:
#     pass
# with open(os.path.join(path2, "kot2.jpg"),"w") as file:
#     pass
# zad5

# import os
# os.mkdir("piesunek")
# os.rename("piesunek","kotek")

# zad6
# import pickle
# lista1=[1,2,3]
# lista2=[1,2]
# lista3=[3]
# with open("plik1.txt","wb") as file:
#     pickle.dump([lista1,lista2,lista3],file)
# del lista1,lista2,lista3
# with open("plik1.txt","rb") as file:
#     lista1,lista2,lista3=pickle.load(file)
# print(lista1,lista2,lista3)

# zad7

# import struct
#
# number = 123456789
#
# with open('liczba.bin', 'wb') as file:
#     data = struct.pack('i', number)
#     file.write(data)
#
# with open('liczba.bin', 'rb') as file:
#     data = file.read()
#     number_unpacked = struct.unpack('i', data)[0]
#
# print(data)
# print("Liczba po odczycie:", number_unpacked)

# zad9


import os


def zawartosc_folderu(dir_path: str):
    print(f"zawartosc folderu '{os.path.basename(dir_path)}': {os.listdir(dir_path)}")
    file_list = os.listdir(dir_path)
    for file in file_list:
        if file.endswith("ABC.txt"):
            licznik = 0
            with open(os.path.join(dir_path, file), 'r') as f:
                tekst = f.read()
                wyrazy = list(tekst.split(" "))
                for wyraz in wyrazy:
                    if len(wyraz) >= 3:
                        licznik += 1
            print(f"ilosc wyrazow z conajmniej 3 literami w pliku{file}: {licznik}")


dir_path = os.path.join(os.getcwd(), "Pliki ze zdaniami")

try:
    os.mkdir("Pliki ze zdaniami")
except FileExistsError as e:
    print(e)
lista = ["Tekst1ID_ABC", "Tekst2ID_405.txt", "Tekst3ID_607.txt", " Tekst4ID_ABC.txt", "Tekst5ID_DEF.txt"]
os.chdir(dir_path)
for filename in lista:
    with open(filename, "w") as file:
        file.write("""Skrzyżowanie, na którym pierwszeństwo przejazdu ustalają znaki.
                    Uwaga! „Pierwszeństwo łamane”, ustalane przez znaki D-1 i A-7 z
                    tabliczkami T-6, na której gruba linia wskazuje przebieg drogi z pierwszeństwem.""")

zawartosc_folderu(dir_path)
