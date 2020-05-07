# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:16:02 2020

@author: julek
"""

""" Ogarniacz biurka/pulpitu/dowolnego folderu na komputerze
Stwórz proszę funkcję, która sprawdzi, jakiego rodzaju pliki znajdują się w
wybranej ścieżce (np. na pulpicie), stworzy adekwatne foldery i przeniesie 
pliki, gdzie trzeba.
Dla przykładu, jeśli na pulpicie będę miał 10 pdfów, 5 plików xlsx i 4 pliki
docx, efektem tej funkcji będzie stworzenie folderów pdf, xlsx oraz docx,
w których znajdziemy wszystkie pliki danego rodzaju.
Czasem nie ma sensu robić oddzielnego folderu dla pojedynczych plików - jeśli
chcesz, spróbuj dodać do funkcji argument, który będzie wyznaczał minimalną
liczbę wystąpień plików danego rodzaju, aby stworzyć oddzielny folder
(np. moje minimum to 3 => na pulpicie będą tylko 2 pliki png, dlatego pliki
te lądują w folderze other) """

import os
import glob
import shutil

def organiser(path,n):
    os.chdir(path)
    files = glob.glob('*.*')
    uniq_extensions = set()
    for file in files:
        uniq_extensions.add(file.split(".")[1])
    for ext in uniq_extensions:
        x = glob.glob('*.' + ext)
        if os.path.isdir(path + '/' + ext) == True: # sprawdza czy danego folderu nie ma już w podanej ścieżce a jak jest to dodaje do niego pliki 
            for file in x:
                shutil.move(file, ext)         
        else:
            if len(x) >= n: # jeśli nie ma folderu to albo tworzy nowy dla danego rozszerzenia albo wrzuca do 'others'
                os.mkdir(ext)
                for file in x:
                    shutil.move(file, ext)
            else:
                if os.path.isdir(path + '/' + 'others') == True:
                    for file in x:
                        shutil.move(file, 'others')
                else:
                    os.mkdir('others')
                    for file in x:
                        shutil.move(file, 'others')
                
    return 'Gotowe!'              
    
# testy
a = "C:/Users/Admin/Desktop/Studia/_Python/lobi"
print(organiser(a,3))