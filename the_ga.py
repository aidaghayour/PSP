import multiprocessing as mp
import statistics
import time

from crossover_operator import crossover
from fitness_evaluator import get_best_individual, evaluate_fitness
from initializer import initialize_population
from mutation_operator import mutate
from pioneer_search import child_in_population
from selector import select_random_numbers
from tournament_holder import hold_tournament


def run_ga(result_keeper, identifier, run, hp_sequence, minimum_energy):
    # execution time
    start_time = time.time()

    # use four processes when possible
    pool = mp.Pool(processes=4)

    print("run: {}".format(run + 1))

    # stats
    result_keeper.reset_prelim_results()
    result_keeper.start_prelim_result_writer()

    # initialize population
    population = pool.apply(initialize_population, args=(result_keeper.pop_size, len(hp_sequence),))

    # list that contains best fitness at [0] and the corresponding individual at [1]
    best = pool.apply(get_best_individual, args=(population, hp_sequence,))
    best_fitness_value = best[0]
    best_individual = best[1]

    # do GA iterations
    iterations = 0
    while iterations < result_keeper.iterations and best_fitness_value > minimum_energy:
        # get random tournament competitors
        random_tournament_indices = select_random_numbers(result_keeper.tournament_size, result_keeper.pop_size)

        competitors = list()
        for index in random_tournament_indices:
            competitors.append(population[index])

        # rank them according to fitness
        ranked_competitors = pool.apply(hold_tournament, args=(competitors, hp_sequence,))

        # take 2 best as parents
        parents = [ranked_competitors[0][1], ranked_competitors[1][1]]
        # get 2 worst individuals
        worst_two = [ranked_competitors[-1][1], ranked_competitors[-2][1]]

        # do crossover with parents
        # returns list with [child_fitness, child] as elements
        children = pool.apply(crossover, args=(
            parents, result_keeper.clash_limit, result_keeper.m_sys_crossover, result_keeper.crossover_rate,
            hp_sequence,))

        # apply pioneer search
        if iterations % 10 == 0 and result_keeper.do_pioneer_search:
            while pool.apply(child_in_population, args=(children, population,)):
                children = pool.apply(crossover,
                                      args=(parents, result_keeper.clash_limit, result_keeper.m_sys_crossover,
                                            result_keeper.crossover_rate, hp_sequence,))

        # replace individuals
        # right now there cannot be multiple copies of same individual in the tournament
        # if this changes, we have to pay attention when removing the competitors from the population
        for fitness_and_child, one_worst_ind in zip(children, worst_two):
            # get the index of the individual to be replaced
            del_index = population.index(one_worst_ind)
            # delete the individual
            del population[del_index]
            # insert the child at that index
            population.insert(del_index, fitness_and_child[1])
            # if that child has better fitness than the current best fitness, set new best individual
            if fitness_and_child[0] < best_fitness_value:
                best_fitness_value = fitness_and_child[0]
                best_individual = population[del_index]

        # get random individuals for mutation
        random_mutation_indices = select_random_numbers(result_keeper.mut_lambda, result_keeper.pop_size)

        individuals_to_mutate = list()

        # do not allow best individual to be mutated
        best_index = population.index(best_individual)
        if best_index in random_mutation_indices:
            # select new random number
            random_alt = select_random_numbers(1, result_keeper.pop_size)[0]
            while (random_alt == index) or (random_alt in random_mutation_indices):
                random_alt = select_random_numbers(1, result_keeper.pop_size)[0]

            index_of_best_index = random_mutation_indices.index(best_index)
            del random_mutation_indices[index_of_best_index]
            random_mutation_indices.insert(index_of_best_index, random_alt)

        for index in random_mutation_indices:
            individuals_to_mutate.append([index, population[index]])

        # do mutation
        mutated_individuals = pool.apply(mutate, args=(
            individuals_to_mutate, result_keeper.in_plane_prob, result_keeper.out_of_plane_prob,
            result_keeper.crank_prob, result_keeper.kink_prob, result_keeper.clash_limit,))

        # order in index list and mutated individual list should not have changed
        for mutant in mutated_individuals:
            # evaluate fitness of mutant
            fitness = pool.apply(evaluate_fitness, args=(mutant[1], hp_sequence,))
            # replace individuals
            del population[mutant[0]]
            population.insert(mutant[0], mutant[1])
            # check fitness
            if fitness < best_fitness_value:
                best_fitness_value = fitness
                best_individual = population[mutant[0]]

        if iterations % 10 == 0:
            ranked_population_fitness = [pool.apply(evaluate_fitness, args=(individual, hp_sequence,)) for individual
                                         in
                                         population]
            ranked_population_fitness.sort()
            result_keeper.append_prelim_results(ranked_population_fitness[0], ranked_population_fitness[-1],
                                                statistics.mean(ranked_population_fitness))

        iterations += 1

    # do output stuff
    end_time = time.time()
    result_keeper.results.append(best_fitness_value)
    result_keeper.append_result_writers(run, best_fitness_value, end_time - start_time)

    result_keeper.end_prelim_result_writer(best_fitness_value, end_time - start_time)
    result_keeper.plot_and_write_prelim(run, best_individual, identifier)
