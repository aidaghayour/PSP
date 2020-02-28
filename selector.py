import random


def select_random_numbers(number_to_be_selected, pool_size):
    pool = list(range(0, pool_size))
    random_numbers = list()

    for i in range(number_to_be_selected):
        rand_number = random.choice(pool)
        random_numbers.append(rand_number)
        # cannot contain same number twice
        pool.remove(rand_number)

    return sorted(random_numbers)
