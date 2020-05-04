import os
from os.path import isfile, join
import shutil
from collections import Counter

def get_files(path):
    files = list()
    for f in os.listdir(path):
        filename = join(path, f)
        if isfile(filename):
            files.append(filename)
    return files

def file_types(files):
    filetypes = Counter()
    for ft in files:
        name, ext = os.path.splitext(ft)
        filetypes[ext] += 1
    return filetypes

def create_folders(filetypes, path, minfile):
    for fo in filetypes:
        if filetypes[fo] >= minfile:
            if not os.path.exists(join(path, fo)):
                os.mkdir(join(path, fo))
        else:
            if not os.path.exists(join(path, 'Other')):
                os.mkdir(join(path, 'Other'))

def sort_file(files, path, filetypes, minfile):
    for sf in files:
        name, ext = os.path.splitext(sf)
        if filetypes[ext] >= minfile:
            shutil.move(sf, join(path, ext))
        else:
            shutil.move(sf, join(path, 'Other'))

def file_sorter(path, minfile):
    files = get_files(path)
    filetypes = file_types(files)
    create_folders(filetypes, path, minfile)
    sort_file(files, path, filetypes, minfile)
    
## Funkcja file_sorter() sortuje wszystkie pliki z podanej scieżki według ich rozszerzenia, a następnie przenosi je do folderu o nazwie danego rozszerzenia (np. pliki pdf zostaną przeniesione do folderu o tytule "pdf"). Funkcje wykorzystujemy w następujący sposób:
##file_sorter(path, minfile)    <- gdzie path jest scieżką w której chcemy uporządkować pliki do folderów, a minfile oznacza minimalną ilosc plików z danym rozszerzeniem, która jest potrzebna by stworzyć dla nich folder. 