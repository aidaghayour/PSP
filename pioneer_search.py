# pioneer search:
# a child must differ from all other individuals in at least must_differences places
# otherwise it will be discarded


def child_in_population(children, population):
    must_differences = int(0.1 * len(children))

    for individual in population:

        for child in children:
            difference_counter = 0
            for a, b in zip(individual, child):
                if a != b:
                    difference_counter += 1

            if difference_counter < must_differences:
                return True
    return False
