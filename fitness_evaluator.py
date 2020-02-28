from mapper import map_individual


def evaluate_fitness(individual, hp_sequence):
    coordinates_individual = map_individual(individual)
    fitness = 0

    for i in range(len(coordinates_individual) - 2):
        # if the current point is a polar amino acids, it cannot contribute to fitness
        if hp_sequence[i] == "P":
            continue
        # check for spatial neighbors among the points subsequent to i
        # since i+1 is a sequential neighbor and does therefore not contribute to fitness
        # we start with j = i+2
        # the last point and the one before the last point cannot contribute to the fitness, because they are
        # themselves sequential neighbors and any possible other neighbors would already be accounted for
        for j in range(i + 2, len(coordinates_individual) - 2):
            # check eastern, northern, western, southern lattice square
            if (coordinates_individual[i].x == coordinates_individual[j].x - 1 and coordinates_individual[i].y ==
                coordinates_individual[j].y) or (
                    coordinates_individual[i].x == coordinates_individual[j].x and coordinates_individual[i].y ==
                    coordinates_individual[j].y - 1) or (
                    coordinates_individual[i].x == coordinates_individual[j].x + 1 and coordinates_individual[i].y ==
                    coordinates_individual[j].y) or (
                    coordinates_individual[i].x == coordinates_individual[j].x and coordinates_individual[i].y ==
                    coordinates_individual[j].y + 1):
                # check whether the neighbor is also hydrophobic
                if hp_sequence[j] == "H":
                    fitness -= 1
    return fitness


def get_best_individual(population, hp_sequence):
    # set arbitrary first best individual
    best_individual = [evaluate_fitness(population[0], hp_sequence), population[0]]
    # check fitness for all in population
    for ind in population:
        fitness_individual = evaluate_fitness(ind, hp_sequence)
        # if fitness is better than that of current best, replace best individual with new current ind
        if fitness_individual < best_individual[0]:
            best_individual = [evaluate_fitness(ind, hp_sequence), ind]

    return best_individual
