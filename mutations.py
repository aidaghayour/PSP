import random


# contains possible mutation types

def in_plane_rotation(individual):
    # randomly choose mutation point
    mutation_point = random.randint(0, len(individual) - 1)

    # rotation: 1 -> -90 degrees, 2 -> -180 degrees
    if individual[mutation_point] == 0:
        new_direction = random.choice([1, 2])
    # rotation: 0 -> +90 degrees, 2 -> -90 degrees
    elif individual[mutation_point] == 1:
        new_direction = random.choice([0, 2])
    # rotation: 0 -> +90 degrees, 1 -> +180 degrees
    else:
        new_direction = random.choice([0, 1])

    individual[mutation_point] = new_direction
    return individual


def out_of_plane_rotation(individual):
    # randomly choose mutation point
    mutation_point = random.randint(0, len(individual) - 1)

    # starting from mutation point, flip 0s (left) to 2s (right) or vice versa
    for i in range(mutation_point, len(individual)):
        if individual[i] == 0:
            individual[i] = 2

        if individual[i] == 2:
            individual[i] = 0

    return individual


def crank_shaft_rotation(individual):
    crank_shafts = list()

    # find crank shaft pattern (0220 or 2002)
    for i in range(0, len(individual) - 3):
        if individual[i] == 0 and individual[i + 1] == 2 and individual[i + 2] == 2 and individual[i + 3] == 0:
            crank_shafts.append(i)

        if individual[i] == 2 and individual[i + 1] == 0 and individual[i + 2] == 0 and individual[i + 3] == 2:
            crank_shafts.append(i)

    # no crankshafts
    if not crank_shafts:
        return individual
    # randomly chooses one of the crankshaft structures
    crank_shaft_point = random.choice(crank_shafts)

    # convert 2002 to 0220
    if individual[crank_shaft_point] == 0:
        individual[crank_shaft_point] = 2
        individual[crank_shaft_point + 1] = 0
        individual[crank_shaft_point + 2] = 0
        individual[crank_shaft_point + 3] = 2

    # convert 0220 to 2002
    elif individual[crank_shaft_point] == 2:
        individual[crank_shaft_point] = 0
        individual[crank_shaft_point + 1] = 2
        individual[crank_shaft_point + 2] = 2
        individual[crank_shaft_point + 3] = 0

    return individual


def kink_movement(individual):
    kink_indices = list()

    # find kink structures in sequence
    for i in range(0, len(individual) - 2):
        # 020, 021, 101, 102, 120, 121, 201, 202
        if (individual[i] == 0 and individual[i + 1] == 2 and individual[i + 2] == 0) or (
                individual[i] == 0 and individual[i + 1] == 2 and individual[i + 2] == 1) or (
                individual[i] == 1 and individual[i + 1] == 0 and individual[i + 2] == 1) or (
                individual[i] == 1 and individual[i + 1] == 0 and individual[i + 2] == 2) or (
                individual[i] == 1 and individual[i + 1] == 2 and individual[i + 2] == 0) or (
                individual[i] == 1 and individual[i + 1] == 2 and individual[i + 2] == 1) or (
                individual[i] == 2 and individual[i + 1] == 0 and individual[i + 2] == 1) or (
                individual[i] == 2 and individual[i + 1] == 0 and individual[i + 2] == 2):
            kink_indices.append(i)

    # no kinks
    if not kink_indices:
        return individual
    # randomly choose one of the kinks
    mutation_point = random.choice(kink_indices)

    # 020 to 101
    if individual[mutation_point] == 0 and individual[mutation_point + 1] == 2 and individual[mutation_point + 2] == 0:
        individual[mutation_point] = 1
        individual[mutation_point + 1] = 0
        individual[mutation_point + 2] = 1

    # 021 to 102
    elif individual[mutation_point] == 0 and individual[mutation_point + 1] == 2 and individual[
        mutation_point + 2] == 1:
        individual[mutation_point] = 1
        individual[mutation_point + 1] = 0
        individual[mutation_point + 2] = 2

    # 101 to 020
    elif individual[mutation_point] == 1 and individual[mutation_point + 1] == 0 and individual[
        mutation_point + 2] == 1:
        individual[mutation_point] = 0
        individual[mutation_point + 1] = 2
        individual[mutation_point + 2] = 0

    # 102 to 021
    elif individual[mutation_point] == 1 and individual[mutation_point + 1] == 0 and individual[
        mutation_point + 2] == 2:
        individual[mutation_point] = 0
        individual[mutation_point + 1] = 2
        individual[mutation_point + 2] = 1

    # 120 to 201
    elif individual[mutation_point] == 1 and individual[mutation_point + 1] == 2 and individual[
        mutation_point + 2] == 0:
        individual[mutation_point] = 2
        individual[mutation_point + 1] = 0
        individual[mutation_point + 2] = 1

    # 121 to 202
    elif individual[mutation_point] == 1 and individual[mutation_point + 1] == 2 and individual[
        mutation_point + 2] == 1:
        individual[mutation_point] = 2
        individual[mutation_point + 1] = 0
        individual[mutation_point + 2] = 2

    # 201 to 120
    elif individual[mutation_point] == 2 and individual[mutation_point + 1] == 0 and individual[
        mutation_point + 2] == 1:
        individual[mutation_point] = 1
        individual[mutation_point + 1] = 2
        individual[mutation_point + 2] = 0

    # 202 to 121
    elif individual[mutation_point] == 2 and individual[mutation_point + 1] == 0 and individual[
        mutation_point + 2] == 2:
        individual[mutation_point] = 1
        individual[mutation_point + 1] = 2
        individual[mutation_point + 2] = 1

    return individual
