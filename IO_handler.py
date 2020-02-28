import os
import re


# the benchmark sequences from included file
def read_benchmark_file():
    benchmark_list = list()
    with open("benchmark_sequences.txt") as data_file:
        # skip first line with column headers
        next(data_file)
        for line in data_file:
            line_list = re.split('\s+', line.strip('\n'))
            # first item absolute minimum energy, second item hp sequence
            benchmark_list.append([int(line_list[0]), list(line_list[1])])
        data_file.close()

    return benchmark_list


def open_compare_file(file_name):
    lines = list()
    with open(file_name) as data_file:
        # skip first line with column headers
        next(data_file)
        for line in data_file:
            line_list = re.split('\t+', line.strip('\n'))
            # add energy (first item is run number)
            lines.append([int(line_list[1]), float(line_list[2])])
        data_file.close()

    return lines


# write results
def write_results_to_file(result, name, indicator=""):
    output_file = indicator + "results" + name + ".txt"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    file = open(output_file, "w")
    for line in result:
        file.write(line)
    file.close()


# output if wrong command line arguments have been given
def print_wrong_arguments():
    print("\nWrong number of input parameters. Program will terminate.")
    print(("\nProgram call must be:\n\n\tpython main.py number_benchmark_sequence "
           "pop_size tournament_size mut_lambda iterations runs"))
    print(("\n\twith\n\t\tnumber_benchmark_sequence: int between 0-7\n\t\tpop_size: positive int\n\t\t"
           "tournament_size: positive int <= pop_size\n\t\tmut_lambda: positive int <= pop_size\n\t\t"
           "iterations: positive int\n\t\truns: positive int\n"))
    print(("Benchmark sequence number: \n\t0 = 20 amino acids"
           "\n\t1 = 24 amino acids"
           "\n\t2 = 25 amino acids"
           "\n\t3 = 36 amino acids"
           "\n\t4 = 48 amino acids"
           "\n\t5 = 50 amino acids"
           "\n\t6 = 60 amino acids"
           "\n\t7 = 64 amino acids\n\n"))
