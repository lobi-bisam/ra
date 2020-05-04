from datetime import datetime
import math
from os.path import join

def is_prime_number(number):
    if number > 1 :
        for nr in range(2, round(math.sqrt(number))+1):
            if (number % nr) == 0:
                return False
        return True
    else:
        return False
        
def save_list_to_file(list, path):
    file_name = join(path, 'prime_' + datetime.now().strftime('%d_%m_%Y')+ '.txt')
    with open(file_name, 'w') as file:
        for element in list:
            print(element, file= file)
    return file_name
        
def prime_numbers(numbers, path): 
    pn = list()
    for nr in numbers:
        if is_prime_number(nr) == True:      
            pn.append(nr)
    print(save_list_to_file(pn, path))

##Funkcja prime_numbers() okresla czy liczba z podanej listy jest liczbą pierwsza i zapisuje ją w pliku tekstowym w podanej scieżce. Funkcje wykorzystujemy w następujący sposób:
##prime_numbers(numbers, path)    <- gdzie numbers jest listą z cyframi, a path jest scieżką w której chcemy by plik z cyframi pierwszymi został zapisany. 