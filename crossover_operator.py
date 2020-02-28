import operator
import random

from clash_checker import check_clash
from fitness_evaluator import evaluate_fitness
from mutation_operator import mutate


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

        clashed = 0
        new_children_created = 0

        # try to make two children, stop when two children created or clash limit reached
        while clashed < clash_limit and new_children_created < 2:
            # create two new children with one crossover
            new_children = create_children(parents)
            # check if first child clashes
            if not check_clash(new_children[0]):
                children.append(new_children[0])
                new_children_created += 1
            else:
                clashed += 1
            # check if second child clashes
            if not check_clash(new_children[1]):
                children.append(new_children[1])
                new_children_created += 1
            else:
                clashed += 1

        # checks if two children were actually made
        if not new_children_created == 2:
            # no child was made, so just reuse both parents
            if new_children_created == 0:
                children.extend(list(parents))
            # one child was made, so reuse first parent
            if new_children_created == 1:
                children.append(list(parents[0]))

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


def create_children(parents):
    # choose random crossover point
    crossover_point = random.randint(2, len(parents[0]) - 1)

    child1 = parents[0][:crossover_point]
    child1.extend(parents[1][crossover_point:])

    child2 = parents[1][:crossover_point]
    child2.extend(parents[0][crossover_point:])

    return [child1, child2]
