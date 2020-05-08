import os
from datetime import datetime
import math

# x = [1,2,3,4,5,6,7,8,10]
x = [123, 45, 87, 96, 12, 58, 5, 47, 73]


def toBePrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for d in range(3, sqr, 2):
        if n % d == 0:
            return False
    return True


# print(toBePrime(2))
# print(toBePrime(1))
# print(toBePrime(5))
# print(toBePrime(88))

def chooseOnlyPrime(list):
    j = []
    for i in list:
        if toBePrime(i):
            j.append(i)
    return ' '.join(map(str, j))


def sentToFile(x):
    text = chooseOnlyPrime(x)
    direct = 'C:\\tasks\\lobi'
    day, month, year = time()
    name = 'prime_%s_%s_%s.txt' % (day, month, year)
    full_name = os.path.join(direct, name)
    with open(full_name, 'w') as file:
        file.write('%s' % text)


def time():
    t = datetime.date(datetime.now())
    day = t.day
    month = t.month
    year = t.year
    return day, month, year


def main():
    print("blabla")


if __name__ == '__main__':
    # print(chooseOnlyPrime(x))
    sentToFile(x)
    # time()
