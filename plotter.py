import datetime
import os

import matplotlib.pyplot as plt
from matplotlib import lines

from mapper import map_individual


# plots the individual in the lattice
def plot_individual(individual, hp_sequence, indicator=""):
    ind_coordinates = map_individual(individual)

    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

    for coord in ind_coordinates:
        if coord.x > x_max:
            x_max = coord.x

        if coord.x < x_min:
            x_min = coord.x

        if coord.y > y_max:
            y_max = coord.y

        if coord.y < y_min:
            y_min = coord.y

    distance = max([abs(x_max - x_min), abs(y_max - y_min)])
    x_max = x_min + distance
    y_max = y_min + distance

    fig, ax = plt.subplots()
    plt.axis('scaled')
    ax.set_axis_off()
    ax.set_xlim(x_min - 1, x_max + 1)
    ax.set_ylim(y_min - 1, y_max + 1)

    # draw grid
    grid_x = [x + 0.5 for x in range(x_min - 1, x_max + 1)]
    grid_y = [x + 0.5 for x in range(y_min - 1, y_max + 1)]

    for i in range(len(grid_x)):
        line = lines.Line2D([grid_x[i], grid_x[i]], [y_min - 1, y_max + 1], linewidth=1, color='black',
                            linestyle='dotted')
        ax.add_line(line)
        line = lines.Line2D([x_min - 1, x_max + 1], [grid_y[i], grid_y[i]], linewidth=1, color='black',
                            linestyle='dotted')
        ax.add_line(line)

    # draw circles
    for coord, point in zip(ind_coordinates, hp_sequence):
        if point == "H":
            circle = plt.Circle((coord.x, coord.y), 0.25, color='black', fill=False, clip_on=False)
        else:
            circle = plt.Circle((coord.x, coord.y), 0.25, color='black', clip_on=False)
        ax.add_artist(circle)

    # draw connections
    for i in range(len(ind_coordinates) - 1):
        y1 = ind_coordinates[i].y
        y2 = ind_coordinates[i + 1].y
        x1 = ind_coordinates[i].x
        x2 = ind_coordinates[i + 1].x
        # subtract/add circle radius to not draw inside circle
        if x1 == x2:
            y2 = y2 - 0.25 if y2 - y1 > 0 else y2 + 0.25
            y1 = y1 + 0.25 if y2 - y1 > 0 else y1 - 0.25

        if y1 == y2:
            x2 = x2 - 0.25 if x2 - x1 > 0 else x2 + 0.25
            x1 = x1 + 0.25 if x2 - x1 > 0 else x1 - 0.25

        line = lines.Line2D([x1, x2], [y1, y2], linewidth=1, color='black')
        ax.add_line(line)

    figure_name = indicator + "plots/plot_best_ind_{}.png".format(
        datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S-%f'))
    os.makedirs(os.path.dirname(figure_name), exist_ok=True)
    fig.savefig(figure_name)
    plt.close()


# plots best, worst, and average fitness progression
def plot_fitness_progression(x, y_best, y_worst, y_avg, indicator):
    plt.figure()
    plt.xlabel('Generations (x10)')
    plt.ylabel('Fitness')
    plt.plot(x, y_best, 'r-', label='Best Fitness')
    plt.plot(x, y_worst, 'g-', label='Worst Fitness')
    plt.plot(x, y_avg, 'b-', label='Average Fitness')
    plt.legend()
    figure_name = indicator + "plots/plot_fitness_progression_{}.png".format(
        datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S-%f'))
    os.makedirs(os.path.dirname(figure_name), exist_ok=True)
    plt.savefig(figure_name)
    plt.close()
