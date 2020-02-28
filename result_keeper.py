import statistics

from scipy import stats

from IO_handler import write_results_to_file
from plotter import plot_fitness_progression, plot_individual


# keeps track of parameters and writes results for each run and after all runs
class ResultKeeper:
    def __init__(self, hp_sequence, length, energy, pop_size, tournament_size, mut_lambda, iterations, clash_limit,
                 m_sys_crossover, crossover_rate, in_plane_prob, out_of_plane_prob, crank_prob, kink_prob,
                 do_pioneer_search):
        self.hp_sequence = hp_sequence
        self.hp_sequence_length = length
        self.hp_sequence_energy = energy
        self.pop_size = pop_size
        self.tournament_size = tournament_size
        self.mut_lambda = mut_lambda
        self.iterations = iterations
        self.clash_limit = clash_limit
        self.m_sys_crossover = m_sys_crossover
        self.crossover_rate = crossover_rate
        self.in_plane_prob = in_plane_prob
        self.out_of_plane_prob = out_of_plane_prob
        self.crank_prob = crank_prob
        self.kink_prob = kink_prob
        self.do_pioneer_search = do_pioneer_search

        self.prelim_results_best = []
        self.prelim_results_worst = []
        self.prelim_results_avg = []

        self.result_writer = []
        self.prelim_result_writer = []

        self.result_to_compare = []

        self.results = []

    def start_result_writer(self):
        self.result_writer = ["Sequence: " + " ".join(self.hp_sequence),
                              "\nLength: {}\nMinimal energy: {}\n".format(self.hp_sequence_length,
                                                                          self.hp_sequence_energy),
                              "Population size: {}\nTournament size: {}\nLambda mutation: {}\n".format(
                                  self.pop_size,
                                  self.tournament_size,
                                  self.mut_lambda),
                              "Iterations: {}\nClash limit: {}\nM-crossover: {}\n".format(
                                  self.iterations,
                                  self.clash_limit,
                                  self.m_sys_crossover),
                              "Crossover rate: {}\nMutation probabilities:\n".format(self.crossover_rate),
                              "\tIn plane: {}\n\tOut of plane: {}\n\tCrank: {}\n\tKink: {}".format(
                                  self.in_plane_prob,
                                  self.out_of_plane_prob,
                                  self.crank_prob,
                                  self.kink_prob),
                              "\nDo pioneer search: {}".format(self.do_pioneer_search),
                              "\n\n{:3}\t{:4}\t{:15}\n".format("Run", "Best", "Time")]

    def append_result_writers(self, run, best_fitness_value, time):
        self.result_writer.append("{:3}\t{:4}\t{:5.10f}\n".format(run, best_fitness_value, time))
        self.result_to_compare.append("{:3}\t{:4}\t{:5.10f}\n".format(run, best_fitness_value, time))

    def finalize_result_writer(self, runs, results):
        self.result_writer.append(
            "\nEnergy value ({} runs)\n\tBest: {}\n\tMean: {}\n\tSD: {}".format(runs,
                                                                                min(results),
                                                                                statistics.mean(
                                                                                    results),
                                                                                statistics.pstdev(
                                                                                    results)))

    def start_compare_writer(self):
        self.result_to_compare = ["{:3}\t{:4}\t{:15}\n".format("Run", "Best", "Time")]

    def reset_prelim_results(self):
        self.prelim_results_best = []
        self.prelim_results_worst = []
        self.prelim_results_avg = []

    def append_prelim_results(self, best, worst, average):
        self.prelim_results_best.append(best)
        self.prelim_results_worst.append(worst)
        self.prelim_results_avg.append(average)

    def end_prelim_result_writer(self, best_fitness_value, time_diff):
        for j in range(0, len(self.prelim_results_avg)):
            # generation, best, worst, avg
            self.prelim_result_writer.append(
                "{:10}\t{:4}\t{:5}\t{:3.4f}\n".format((j + 1) * 10, self.prelim_results_best[j],
                                                      self.prelim_results_worst[j],
                                                      self.prelim_results_avg[j]))
        self.prelim_result_writer.append("\n\nBest energy value: {}\n".format(best_fitness_value))
        self.prelim_result_writer.append(
            "Mean best energy value: {}\n".format(statistics.mean(self.prelim_results_best)))
        self.prelim_result_writer.append(
            "Mean worst energy value: {}\n".format(statistics.mean(self.prelim_results_worst)))
        self.prelim_result_writer.append(
            "Mean average energy value: {}\n".format(statistics.mean(self.prelim_results_avg)))
        self.prelim_result_writer.append("Iterations: {}\n".format(self.iterations))
        self.prelim_result_writer.append("Execution time: {} sec\n".format(time_diff))

    def start_prelim_result_writer(self):
        self.prelim_result_writer = ["Sequence: " + " ".join(self.hp_sequence),
                                     "\n\nLength: {}, minimal energy: {}\n\n".format(self.hp_sequence_length,
                                                                                     self.hp_sequence_energy),
                                     "{:10}\t{:4}\t{:5}\t{:7}\n".format("Generation", "Best", "Worst",
                                                                        "Average")]

    def plot_and_write_prelim(self, run, best_individual, indicator):
        write_results_to_file(self.prelim_result_writer, "_run_{}".format(run), indicator + "prelim_results/")
        plot_individual(best_individual, self.hp_sequence, indicator)
        plot_fitness_progression(list(range(len(self.prelim_results_avg))), self.prelim_results_best,
                                 self.prelim_results_worst,
                                 self.prelim_results_avg, indicator)
