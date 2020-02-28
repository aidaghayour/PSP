import argparse
import sys

from IO_handler import read_benchmark_file, write_results_to_file, print_wrong_arguments
from result_keeper import ResultKeeper
from the_ga import run_ga

# there are six input arguments:
# benchmark sequence number: 0 = 20 amino acids, 1 = 24 amino acids, 2 = 25 amino acids, 3 = 36 amino acids,
# 4 = 48 amino acids, 5 = 50 amino acids, 6 = 60 amino acids, 7 = 64 amino acids,
# population size n,
# parent tournament selection size k,
# mutation group size lambda,
# the maximum number of iterations i,
# and the number of runs, i.e. how often the complete GA is executed
parser = argparse.ArgumentParser(description='GP Parameters.')
parser.add_argument('benchmark_sequence', metavar='b', type=int, nargs='?', help='Which benchmark sequence to use.')
parser.add_argument('pop_size', metavar='n', type=int, nargs='?', help='Population size.')
parser.add_argument('tournament_size', metavar='k', type=int, nargs='?', help='The tournament size k.')
parser.add_argument('mut_lambda', metavar='l', type=int, nargs='?', help='Mutation group size lambda.')
parser.add_argument('iterations', metavar='i', type=int, nargs='?',
                    help='The number of generations the algorithm will run.')
parser.add_argument('runs', metavar='r', type=int, nargs='?',
                    help='The number of runs the experiment will be repeated')
args = parser.parse_args()

if not len(sys.argv) == 7:
    print_wrong_arguments()
    sys.exit(1)

# set parameters
clash_limit = 10
m_sys_crossover = 3
crossover_rate = 1.0
in_plane_prob = 0.2
out_of_plane_prob = 0.2
crank_prob = 0.2
kink_prob = 0.4
do_pioneer_search = False

# get hp sequence: [total minimum energy, sequence]
benchmark = read_benchmark_file()[args.benchmark_sequence]

# result_keeper keeps track of all parameters and results for output
result_keeper = ResultKeeper(benchmark[1], length=len(benchmark[1]), energy=benchmark[0], pop_size=args.pop_size,
                             tournament_size=args.tournament_size,
                             mut_lambda=args.mut_lambda, iterations=args.iterations, clash_limit=clash_limit,
                             m_sys_crossover=m_sys_crossover, crossover_rate=crossover_rate,
                             in_plane_prob=in_plane_prob, out_of_plane_prob=out_of_plane_prob,
                             crank_prob=crank_prob,
                             kink_prob=kink_prob,

                             do_pioneer_search=do_pioneer_search)

print("sequence: " + " ".join(benchmark[1]))

# identifying string for creating a folder for output files
identifier = "results/sequence_{}_pop_{}_lambda_{}/".format(args.benchmark_sequence,
                                                            args.pop_size,
                                                            args.mut_lambda)
# initialize the result keeper
result_keeper.start_result_writer()
result_keeper.start_compare_writer()

# let the GA run
for i in range(args.runs):
    run_ga(result_keeper, identifier, i, benchmark[1], benchmark[0])

# get output
result_keeper.finalize_result_writer(args.runs, result_keeper.results)
write_results_to_file(result_keeper.result_writer, "final", identifier)
write_results_to_file(result_keeper.result_to_compare, "final_compare", identifier)
