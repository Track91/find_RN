import random
import math
import statistics
from statistics import *
def find_random_number(counter):
    range = 1000
    number = random.randint(0, range)
    counter = 1
    start = range/2
    number_asked = 500
    running = True
    while running:

        if number_asked > number:
            number_asked = int(number_asked - (start/(counter*2)))

        elif number_asked < number:
            number_asked = int(number_asked + (start/(counter*2)))

        else:
            break

        counter += 1

    counter -= 1
    return counter


def get_result():
    result = []

    for i in range(100000):
        globals()["v" + str(i)] = find_random_number(i)
        result.append(globals()["v" + str(i)])
    moyenne = statistics.fmean(result)
    mediane = statistics.median(result)
    variance = statistics.variance(result)
    ecart_type = math.sqrt(variance)
    print('Moyenne : {} \n '
          'Mediane : {} \n'
          'Ecart-type : {} '
          .format(moyenne, mediane, ecart_type))

get_result()
