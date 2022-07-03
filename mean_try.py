import random
from statistics import *
def find_random_number(mot):

    number = random.randint(0, 1000)
    mot = 1
    start = 500
    number_asked = 500
    running = True
    while running:

        if number_asked > number:
            number_asked = int(number_asked - (start/(mot*2)))

        elif number_asked < number:
            number_asked = int(number_asked + (start/(mot*2)))

        else:
            break

        mot += 1
    mot -= 1
    return mot
def get_result():
    result = []

    for i in range(10000):
        globals()["v" + str(i)] = find_random_number(i)
        result.append(globals()["v" + str(i)])
    result = mean(result)
    return result

print(get_result())
