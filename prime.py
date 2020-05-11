#tworzymy plik z nazwa dzisiejszej daty

from datetime import date

today = date.today()
curr_date = today.strftime("%d_%m_%Y")
print(curr_date)

file_primes = open("prime_" + curr_date +".txt","w+")

#tworzyny funkcje wypisujaca liczby pierwsze

def function_prime_check(num_list):
    
    for i in range(0,len(num_list)):
        num = num_list[i]
        
   
        is_prime = True

        for i in range(2,num//2):
           
            if num % i == 0: 
                is_prime = False
                break
      
        if is_prime:
            file_primes.write(str(num) + " ")


function_prime_check([12,11,13,33,45,233])

file_primes.close()

print("end")









