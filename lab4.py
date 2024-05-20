# zad1
import os

# def zmiana_katalogu(sciezka):
#     try:
#         os.chdir(sciezka)
#         print(f"Zawartość katalogu {sciezka}:")
#         for plik in os.listdir():
#             print(plik)
#
#     except FileNotFoundError:
#         print("Podana ścieżka nie istnieje.")
#     except PermissionError:
#         print("Brak uprawnień dostępu do wskazanego katalogu.")


#zad2
# import os
# def zmiana(path):
#     while True:
#         pyt=input("czy mam zmienic katalog?(yes-no)")
#         if pyt=="yes":
#             os.chdir(path)
#             print(os.listdir(path))
#             break
#         else:
#             continue
# sciezka = input("Podaj ścieżkę do katalogu: ")
# zmiana("C:\\Users\\sebar\\")

# zad3
# python_dir = os.getcwd()
#
# nazwa_katalogu = "Dokument"
# dokumenty_path = os.path.join(python_dir, nazwa_katalogu)
# try:
#     os.mkdir(dokumenty_path)
# except FileExistsError as e:
#     print(e)
# except FileNotFoundError as e:
#     print(e)
#
# os.chdir(dokumenty_path)
# print(os.getcwd())
#
# with open("Lab1.doc", "w") as file:
#     pass
# with open("Lab2.doc", "w") as file2:
#     pass
# with open("Lab3.doc", "w") as file3:
#     pass
#
#
# print(os.listdir("."))#bierzący fold
# print(os.listdir(dokumenty_path))
#
# a = list(filter(lambda a: True if a.endswith(".doc") else False, os.listdir(".")))
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
import math

local_path = os.getcwd()
new_file_path = os.path.join(local_path, "folder")
try:
    os.mkdir(new_file_path)
except FileExistsError:
    print("Plik istnieje!")
try:
    os.rename(new_file_path, os.path.join(local_path, "after_change"))
except FileExistsError:
    print("Plik istnieje!")


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
# with open("plik1.txt", "rb") as f:
#     print(*pickle.load(f))
# zad7

# import struct
# with open("struct_path.txt", "wb") as file:
#     file.write(struct.pack('q', 123456789))
#
#
# with open("struct_path.txt", "rb") as file:
#     packed_data = file.read()
#
#
# unpacked_data = struct.unpack('q', packed_data)
#
# print("Pakowane dane:", packed_data)
# print("Rozpakowane dane:", unpacked_data[0])



# zad9
# import os
#
#
# def zawartosc_folderu(dir_path: str):
#     print(f"zawartosc folderu '{os.path.basename(dir_path)}': {os.listdir(dir_path)}")
#     file_list = os.listdir(dir_path)
#     for file in file_list:
#         if file.endswith("ABC.txt"):
#             licznik = 0
#             with open(os.path.join(dir_path, file), 'r') as f:
#                 tekst = f.read()
#                 wyrazy = list(tekst.split(" "))
#                 for wyraz in wyrazy:
#                     if len(wyraz) >= 3:
#                         licznik += 1
#             print(f"ilosc wyrazow z conajmniej 3 literami w pliku{file}: {licznik}")
#
#
# dir_path = os.path.join(os.getcwd(), "Pliki ze zdaniami")
#
# try:
#     os.mkdir("Pliki ze zdaniami")
# except FileExistsError as e:
#     print(e)
# lista = ["Tekst1ID_ABC", "Tekst2ID_405.txt", "Tekst3ID_607.txt", " Tekst4ID_ABC.txt", "Tekst5ID_DEF.txt"]
# os.chdir(dir_path)
# for filename in lista:
#     with open(filename, "w") as file:
#         file.write("""Skrzyżowanie, na którym pierwszeństwo przejazdu ustalają znaki.
#                     Uwaga! „Pierwszeństwo łamane”, ustalane przez znaki D-1 i A-7 z
#                     tabliczkami T-6, na której gruba linia wskazuje przebieg drogi z pierwszeństwem.""")
#
# zawartosc_folderu(dir_path)
