# Bubble sort benchmark

import sys
import random
from time import process_time

MAX_VALUE = 999999
DEFAULT_SIZE = 5000
DEFAULT_TRIALS = 5


def generate_random_numbers(size):
    return list(random.randint(1, MAX_VALUE) for i in range(size))


def bubble_sort(data):
    size = len(data)
    for i in range(size):
        swapped = False
        for j in range(size - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    size = DEFAULT_SIZE
    num_trials = DEFAULT_TRIALS

    if len(sys.argv) > 1:
        size = int(sys.argv[1])

    if len(sys.argv) > 2:
        num_trials = int(sys.argv[2])

    total_time = 0.0

    for i in range(num_trials):
        data = generate_random_numbers(size)
        start_time = process_time()
        bubble_sort(data)
        total_time += process_time() - start_time
        print(f"Trial {i + 1} done")

    average_time = total_time / num_trials
    print(f"{size} numbers sorted in {average_time:.5f} seconds")
