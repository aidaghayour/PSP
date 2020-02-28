from mapper import map_individual


# this does nothing much except checking whether the list with the individuals coordinates
# has the same length as the set with the individuals coordinates.
# since the latter does not contain duplicates, the sets cardinality would
# would be less then the list's cardinality.
def check_clash(individual):
    coordinates = map_individual(individual)

    return len(set(coordinates)) < len(coordinates)
