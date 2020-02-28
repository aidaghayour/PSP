import operator

from fitness_evaluator import evaluate_fitness


def hold_tournament(competitors, hp_sequence):
    competitors_with_fitness = list()

    for competitor in competitors:
        # append competitor's fitness and competitor
        competitors_with_fitness.append([evaluate_fitness(competitor, hp_sequence), competitor])

    # return fitness+competitor list ranked according to fitness
    # sort is done in ascending order, so the first two have the minimal, i.e. the best, fitness
    return sorted(competitors_with_fitness, key=operator.itemgetter(0))
