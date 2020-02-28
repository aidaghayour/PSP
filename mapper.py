from coordinates import Coordinate


def map_individual(individual):
    # first step always straight (1)
    coord_back_2 = Coordinate(0, 0)
    coord_back_1 = Coordinate(1, 0)
    coordinates = [coord_back_2, coord_back_1]

    for i in range(2, len(individual) + 2):
        step = individual[i - 2]

        # find out current orientation
        # east
        if coord_back_2.x < coord_back_1.x and coord_back_2.y == coord_back_1.y:
            # and go straight
            if step == 1:
                new_coord = Coordinate(coord_back_1.x + 1, coord_back_1.y)

            # and go left
            if step == 0:
                new_coord = Coordinate(coord_back_1.x, coord_back_1.y + 1)

            # and go right
            if step == 2:
                new_coord = Coordinate(coord_back_1.x, coord_back_1.y - 1)

        # north
        if coord_back_2.x == coord_back_1.x and coord_back_2.y < coord_back_1.y:
            # and go straight
            if step == 1:
                new_coord = Coordinate(coord_back_1.x, coord_back_1.y + 1)

            # and go left
            if step == 0:
                new_coord = Coordinate(coord_back_1.x - 1, coord_back_1.y)

            # and go right
            if step == 2:
                new_coord = Coordinate(coord_back_1.x + 1, coord_back_1.y)

        # west
        if coord_back_2.x > coord_back_1.x and coord_back_2.y == coord_back_1.y:
            # and go straight
            if step == 1:
                new_coord = Coordinate(coord_back_1.x - 1, coord_back_1.y)

            # and go left
            if step == 0:
                new_coord = Coordinate(coord_back_1.x, coord_back_1.y - 1)

            # and go right
            if step == 2:
                new_coord = Coordinate(coord_back_1.x, coord_back_1.y + 1)

        # south
        if coord_back_2.x == coord_back_1.x and coord_back_2.y > coord_back_1.y:
            # and go straight
            if step == 1:
                new_coord = Coordinate(coord_back_1.x, coord_back_1.y - 1)

            # and go left
            if step == 0:
                new_coord = Coordinate(coord_back_1.x + 1, coord_back_1.y)

            # and go right
            if step == 2:
                new_coord = Coordinate(coord_back_1.x - 1, coord_back_1.y)

        coordinates.append(new_coord)
        coord_back_2 = coord_back_1
        coord_back_1 = new_coord

    return coordinates
