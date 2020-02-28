
The program call must be:

	python main.py number_benchmark_sequence pop_size tournament_size mut_lambda iterations runs

	with
		number_benchmark_sequence: int between 0-7
		pop_size: positive int
		tournament_size: positive int <= pop_size
		mut_lambda: positive int <= pop_size
		iterations: positive int
		runs: positive int

Benchmark sequence number:
	0 = 20 amino acids
	1 = 24 amino acids
	2 = 25 amino acids
	3 = 36 amino acids
	4 = 48 amino acids
	5 = 50 amino acids
	6 = 60 amino acids
	7 = 64 amino acids

the_ga.py contains the GA iterations and main.py calls the GA for each run.
Further parameters can be set in main.py.
To do rotation crossover, import crossover_operator_rotate instead of crossover_operator
in the_ga.py.

The identifier string in main.py should be set to something unique and appropriate for the
current run, as it is the name of the folder that will be created for the output.

Packages to be installed (are installed in the venv python):
- matplotlib (version==2.1.2)
- scipy
(- pandas)

pandas is only needed for compare_results_pop_sizes_lambdas.py,
compare_results_sequences_lambda.py, and compare_results_xovers_and_lambdas.py.
These files are not part of the GA but can be used for visualizing the results.

The source code can also be found at https://github.com/cubeme/ECproject
