import random

from clash_checker import check_clash


def initialize_population(pop_size, sequence_length):
    population = list()

    for i in range(pop_size):
        # add new individual to population with key i
        population.append(create_individual(list(), sequence_length, [0, 1, 2]))

    return population


def create_individual(new_individual, sequence_length, possible_steps):
    # make an empty list for steps that led to clashes
    steps_that_clashed = [[] for _ in range(sequence_length)]

    # first step is always 1
    # and sequence of length n needs n-1 steps
    # --> an individual has length n-2
    while len(new_individual) < sequence_length - 2:
        current_length = len(new_individual)

        # check if there are any possible steps left
        if not possible_steps:
            # since there are no possible steps left, we need to backtrack more than 1 step
            i = current_length
            # go back to where there are still step options (= backtrack point)
            while len(steps_that_clashed[i]) == 3:
                steps_that_clashed[i] = []
                i -= 1

            # new possible steps
            possible_steps = [0, 1, 2]
            # if steps have already been tried for this position (and have failed), remove them from possible steps
            if not steps_that_clashed[i]:
                for s in steps_that_clashed[i]:
                    possible_steps.remove(s)

            # go back to backtrack point and remove all steps after that
            new_individual = new_individual[:current_length - i]

        # choose random new step
        step = random.SystemRandom().choice(possible_steps)
        new_individual.append(step)

        if check_clash(new_individual):
            # and remove the step that led to the clash
            possible_steps.remove(step)

            steps_that_clashed[len(new_individual)].append(step)
            # there was a clash, so remove the last step (backtrack)
            del new_individual[-1]
        else:
            possible_steps = [0, 1, 2]

    return new_individual
