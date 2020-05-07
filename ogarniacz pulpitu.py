import tkinter
from tkinter import filedialog
import os
from pathlib import Path
import shutil

def getPliki(wskazanyFolder):
    
    listaPlikow = []
    
    with os.scandir(wskazanyFolder) as elty:
        for elt in elty:
            if elt.is_file():
                listaPlikow.append(elt.name)
                
    listaPlikow.sort(key=lambda plik: os.path.splitext(plik.lower())[1])
    return listaPlikow

def getFoldery(listaPlikow):
    
    foldery = []
    poprzednie = '@' # dla bezpieczeństwa (nie ''), gdyby trafiło na plik bez rozszerzenia
    i = -1
    
    for elt in listaPlikow:
        biezace = os.path.splitext(elt.lower())[1][1:]
        if biezace != poprzednie:
            foldery.append([biezace,1])
            i += 1 #numer wiersza
        else:
            foldery[i][1] += 1 #zwiększa licznik (ile plików o danym rozszerzeniu)
        poprzednie = biezace
        
    return foldery

def jakiFolder(ext, listaFolderow, minIle):
    
    ile = 0
    for elt in listaFolderow:
        if elt[0] == ext:
            ile = elt[1]
            break
    if ile < minIle:
        folder = 'Other'
    else:
        folder = ext
    return folder

def przeniesPliki(listaFolderow, wskazanyFolder, listaPlikow, minIle):

    for plik in listaPlikow:
        ext = os.path.splitext(plik.lower())[1][1:]
        folder = jakiFolder(ext,listaFolderow, minIle)
        p = Path(os.path.join(wskazanyFolder, folder))
        p.mkdir(exist_ok=True) # zabezpiecza przed wysypaniem się programu, jeśli istnieje już folder o takiej nazwie
        
        src = os.path.join(wskazanyFolder, plik)
        dest = os.path.join(wskazanyFolder, folder, plik)        
        shutil.move(src, dest)
        
    return

            
def main(minIle = 0):
    
    root = tkinter.Tk()
    root.withdraw()
    wskazanyFolder = filedialog.askdirectory()

    listaPlikow = getPliki(wskazanyFolder)
    listaFolderow = getFoldery(listaPlikow)
    przeniesPliki(listaFolderow, wskazanyFolder, listaPlikow, minIle)

#    print(listaPlikow)
#    print(listaFolderow)
    

    
main(3)
