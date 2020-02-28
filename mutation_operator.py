import copy
import random

from clash_checker import check_clash
from mutations import in_plane_rotation, out_of_plane_rotation, crank_shaft_rotation, kink_movement


def mutate(individuals_to_mutate, in_plane_prob, out_of_plane_prob, crank_prob, kink_prob, clash_limit):
    mutated_individuals = list()

    # cumulative probabilities
    cumulative_probabilities = [in_plane_prob, in_plane_prob + out_of_plane_prob,
                                in_plane_prob + out_of_plane_prob + crank_prob,
                                in_plane_prob + out_of_plane_prob + crank_prob + kink_prob]

    for individual in individuals_to_mutate:
        mutant = copy.copy(individual[1])
        clashed = 0

        random_number = random.SystemRandom().uniform(0, 1.0)

        # applies mutation until mutant does not show any clashes
        while clash_limit != clashed:
            # do in plane rotation
            if random_number <= cumulative_probabilities[0]:
                mutant = in_plane_rotation(mutant)

            # do out of plane rotation
            elif cumulative_probabilities[0] < random_number <= cumulative_probabilities[1]:
                mutant = out_of_plane_rotation(mutant)

            # do crank shaft mutation
            elif cumulative_probabilities[1] < random_number <= cumulative_probabilities[2]:
                mutant = crank_shaft_rotation(mutant)

            # do kink movement
            elif cumulative_probabilities[2] < random_number <= cumulative_probabilities[3]:
                mutant = kink_movement(mutant)

            # if clash occurred, try again to mutate individual
            if check_clash(mutant):
                mutant = copy.copy(individual[1])
                clashed += 1
            else:
                break

        mutated_individuals.append([individual[0], mutant])

    return mutated_individuals
