import random
from time import process_time


def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index+1]:
            return False
    return True


def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values


print(bogo_sort([3,33,8998,9842,123, 332]))
print(process_time(), "s")

