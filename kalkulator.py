# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:31:26 2020

@author: julek
"""

"""Kalkulator liczb pierwszych
Dla przypomnienia, liczby pierwsze to liczby naturalne większe od 1,
które są podzielne wyłącznie przez samą siebie i przez 1.
Stwórz proszę funkcję, która:
będzie przyjmowała za argument listę/wektor/jednowymiarową macierz 
(w zależności od wybranego przez Ciebie języka programowania)
będzie zwracała do wybranej przez użytkownika ścieżki plik o nazwie
prime_DD_MM_YYYY.txt (gdzie DD_MM_YYYY to data). Sam plik powinien zawierać
tylko liczby pierwsze, oddzielane spacją.
Dla przykładu, jeśli w języku programowania Julia stworzę
taką funkcję i jako argument podam wektor [2 3 4 5 6 7 8 9 10],
to efektem takiej funkcji będzie wyeksportowany plik tekstowy
z wartościami 2 3 5 7."""

import os
from datetime import date

def givePrimes(lst):
    ans = list()      
    if type(lst) is list :
        for num in lst:
            if num > 1:
                for i in range(2,num):
                    if (num % i) == 0:
                        break
                else:
                    ans.append(num)
        fpath = input("Proszę o podanie docelowej ścieżki dla pliku:")
        today = date.today()
        fname = today.strftime("%d_%m_%Y")
        completePath = os.path.join(fpath, "prime_" + fname + ".txt")
        i = 0
        while True: # sprawdza czy jest już plik o danej nazwie i nie nadpisuje tylko tworzy nowy
            if os.path.isfile(completePath):
                completePath = os.path.join(fpath, "prime_" + fname + '_' + str(i) +".txt")
                i += 1
            else:
                break
        f = open(completePath, "w")
        listToStr = ' '.join([str(elem) for elem in ans])
        f.write(listToStr)
        f.close()
        return "Gotowe!"
    else:
        return "To nie lista!"
        quit()

#test
A = [1,2,3]
B = [-2,1,3,5]
C = (1,2)
D = list(range(100))

print(givePrimes(D))