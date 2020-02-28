import operator
import random

from clash_checker import check_clash
from fitness_evaluator import evaluate_fitness
from mutation_operator import mutate


# does crossover with rotating the part of the second parent if a clash occurred,
# instead of dismissing the child right away
def crossover(parents, clash_limit, m_sys_crossover, crossover_rate, hp_sequence, do_mutation=False):
    children = list()

    # per iteration two children are added -> 2 * m_sys_crossover children are created in total
    for i in range(m_sys_crossover):
        # choose random number
        random_number = random.SystemRandom().uniform(0, 1.0)
        # check crossover probability
        if random_number > crossover_rate:
            # no crossover, just append parents
            children.extend(parents)
            continue

        children = create_children(parents, clash_limit)

    # do mutation on children
    if do_mutation:
        children = mutate(children, 0.4, 0.1, 0.1, 0.4, clash_limit)

    # get fitness of all children
    ranked_children = list()
    for child in children:
        # append child's fitness and child
        ranked_children.append([evaluate_fitness(child, hp_sequence), child])

    # rank children according to fitness
    ranked_children.sort(key=operator.itemgetter(0))

    # return two best children
    return ranked_children[:2]


def create_children(parents, clash_limit):
    clashed = 0
    new_children = []

    while clashed < clash_limit:
        # choose random crossover point
        crossover_point = random.randint(2, len(parents[0]) - 1)

        # create two children (rotate crossover point if necessary)
        child1 = crossover_with_rotation(parents, 0, 1, crossover_point)
        child2 = crossover_with_rotation(parents, 1, 0, crossover_point)

        # check if children were made
        if child1:
            new_children.append(child1)
            if len(new_children) == 2:
                break
        if child2:
            new_children.append(child2)
            if len(new_children) == 2:
                break

    # check how many children were made
    if not new_children:
        new_children.extend(list(parents))
    if len(new_children) == 1:
        new_children.append(list(parents[0]))

    return new_children


def crossover_with_rotation(parents, p0, p1, crossover_point):
    alt_directions = [0, 1, 2]
    # get the value of the crossover point
    crossover_direction = parents[p1][crossover_point]
    alt_directions.remove(crossover_direction)
    # create first part of child
    child = parents[p0][:crossover_point]

    # try to do crossover
    while alt_directions:
        child.append(crossover_direction)
        child.extend(parents[p1][crossover_point + 1:])

        # crossover didn't work, try again with but rotate second part
        if check_clash(child):
            del child[crossover_point:]
            crossover_direction = random.choice(alt_directions)
            alt_directions.remove(crossover_direction)
        else:
            return child

    # not child could be made
    return []
