from datetime import date
import tkinter
from tkinter import filedialog

def czyPierwsza(liczba):
    
    czy = False
    if liczba > 1:
        for i in range(2, liczba):
            if (liczba % i) == 0:
                return False
                break
        else:
            return True
        
    return czy

def getFolder():
    
    root = tkinter.Tk()
    root.withdraw()
    
    return filedialog.askdirectory()

def getLista():
    
    # funkcja dodatkowa - dane mogą być przekazane nie za pomocą listy, ale z pliku.
    root = tkinter.Tk()
    root.withdraw()
    fileName = filedialog.askopenfilename()
    with open(fileName, 'r', encoding = 'UTF-8') as file:
        s = file.read().splitlines()
        
    wynik = []
    for n in s:
        if n.isdigit():
            wynik.append(int(n))
            
    return wynik

def main(lista = []):
    
    # jeśli przy wywołaniu maina nie zostanie podana lista, domyślnie program przyjmie pustą listę i zastosuje funkcję getLista
    if not lista:
        lista = getLista()
    
    pierwsze = []
    d = date.today()
    for liczba in lista:
        if czyPierwsza(liczba):
            pierwsze.append(liczba)
    nazwaPliku = getFolder() + '/' + 'prime_'+d.strftime('%d')+"_"+d.strftime('%m')+"_"+d.strftime('%Y')+'.txt'
    with open (nazwaPliku, 'w') as file:
        for liczba in pierwsze:
            file.write('%s ' % liczba)

    

main([2, 3, 4, 5, 6, 7, 8, 9, 10])
