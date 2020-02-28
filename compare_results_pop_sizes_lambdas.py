import statistics

import matplotlib.pyplot as plt

from IO_handler import open_compare_file

file_0_100_10_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_10_normal_xover/resultsfinal_compare.txt")
file_0_100_20_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_20_normal_xover/resultsfinal_compare.txt")
file_0_100_30_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_30_normal_xover/resultsfinal_compare.txt")
file_0_100_40_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_40_normal_xover/resultsfinal_compare.txt")
file_0_100_50_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_50_normal_xover/resultsfinal_compare.txt")
file_0_100_60_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_60_normal_xover/resultsfinal_compare.txt")
file_0_100_70_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_70_normal_xover/resultsfinal_compare.txt")
file_0_100_80_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_80_normal_xover/resultsfinal_compare.txt")
file_0_100_90_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_90_normal_xover/resultsfinal_compare.txt")

file_0_200_10_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_10_normal_xover/resultsfinal_compare.txt")
file_0_200_20_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_20_normal_xover/resultsfinal_compare.txt")
file_0_200_30_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_30_normal_xover/resultsfinal_compare.txt")
file_0_200_40_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_40_normal_xover/resultsfinal_compare.txt")
file_0_200_50_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_50_normal_xover/resultsfinal_compare.txt")
file_0_200_60_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_60_normal_xover/resultsfinal_compare.txt")
file_0_200_70_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_70_normal_xover/resultsfinal_compare.txt")
file_0_200_80_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_80_normal_xover/resultsfinal_compare.txt")
file_0_200_90_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_90_normal_xover/resultsfinal_compare.txt")
file_0_200_100_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_100_normal_xover/resultsfinal_compare.txt")
file_0_200_110_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_110_normal_xover/resultsfinal_compare.txt")
file_0_200_120_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_120_normal_xover/resultsfinal_compare.txt")
file_0_200_130_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_130_normal_xover/resultsfinal_compare.txt")
file_0_200_140_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_140_normal_xover/resultsfinal_compare.txt")
file_0_200_150_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_150_normal_xover/resultsfinal_compare.txt")
file_0_200_160_normal_xover = open_compare_file(
    "results/sequence_0_pop_200_lambda_160_normal_xover/resultsfinal_compare.txt")

file_0_300_10_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_10_normal_xover/resultsfinal_compare.txt")
file_0_300_20_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_20_normal_xover/resultsfinal_compare.txt")
file_0_300_30_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_30_normal_xover/resultsfinal_compare.txt")
file_0_300_40_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_40_normal_xover/resultsfinal_compare.txt")
file_0_300_50_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_50_normal_xover/resultsfinal_compare.txt")
file_0_300_60_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_60_normal_xover/resultsfinal_compare.txt")
file_0_300_70_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_70_normal_xover/resultsfinal_compare.txt")
file_0_300_80_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_80_normal_xover/resultsfinal_compare.txt")
file_0_300_90_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_90_normal_xover/resultsfinal_compare.txt")
file_0_300_100_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_100_normal_xover/resultsfinal_compare.txt")
file_0_300_110_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_110_normal_xover/resultsfinal_compare.txt")
file_0_300_120_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_120_normal_xover/resultsfinal_compare.txt")
file_0_300_130_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_130_normal_xover/resultsfinal_compare.txt")
file_0_300_140_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_140_normal_xover/resultsfinal_compare.txt")
file_0_300_150_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_150_normal_xover/resultsfinal_compare.txt")
file_0_300_160_normal_xover = open_compare_file(
    "results/sequence_0_pop_300_lambda_160_normal_xover/resultsfinal_compare.txt")

file_0_400_10_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_10_normal_xover/resultsfinal_compare.txt")
file_0_400_20_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_20_normal_xover/resultsfinal_compare.txt")
file_0_400_30_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_30_normal_xover/resultsfinal_compare.txt")
file_0_400_40_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_40_normal_xover/resultsfinal_compare.txt")
file_0_400_50_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_50_normal_xover/resultsfinal_compare.txt")
file_0_400_60_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_60_normal_xover/resultsfinal_compare.txt")
file_0_400_70_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_70_normal_xover/resultsfinal_compare.txt")
file_0_400_80_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_80_normal_xover/resultsfinal_compare.txt")
file_0_400_90_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_90_normal_xover/resultsfinal_compare.txt")
file_0_400_100_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_100_normal_xover/resultsfinal_compare.txt")
file_0_400_110_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_110_normal_xover/resultsfinal_compare.txt")
file_0_400_120_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_120_normal_xover/resultsfinal_compare.txt")
file_0_400_130_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_130_normal_xover/resultsfinal_compare.txt")
file_0_400_140_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_140_normal_xover/resultsfinal_compare.txt")
file_0_400_150_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_150_normal_xover/resultsfinal_compare.txt")
file_0_400_160_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_160_normal_xover/resultsfinal_compare.txt")
file_0_400_180_normal_xover = open_compare_file(
    "results/sequence_0_pop_400_lambda_180_normal_xover/resultsfinal_compare.txt")

file_0_500_10_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_10_normal_xover/resultsfinal_compare.txt")
file_0_500_20_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_20_normal_xover/resultsfinal_compare.txt")
file_0_500_30_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_30_normal_xover/resultsfinal_compare.txt")
file_0_500_40_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_40_normal_xover/resultsfinal_compare.txt")
file_0_500_50_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_50_normal_xover/resultsfinal_compare.txt")
file_0_500_60_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_60_normal_xover/resultsfinal_compare.txt")
file_0_500_70_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_70_normal_xover/resultsfinal_compare.txt")
file_0_500_80_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_80_normal_xover/resultsfinal_compare.txt")
file_0_500_90_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_90_normal_xover/resultsfinal_compare.txt")
file_0_500_100_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_100_normal_xover/resultsfinal_compare.txt")
file_0_500_110_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_110_normal_xover/resultsfinal_compare.txt")
file_0_500_120_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_120_normal_xover/resultsfinal_compare.txt")
file_0_500_130_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_130_normal_xover/resultsfinal_compare.txt")
file_0_500_140_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_140_normal_xover/resultsfinal_compare.txt")
file_0_500_150_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_150_normal_xover/resultsfinal_compare.txt")
file_0_500_160_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_160_normal_xover/resultsfinal_compare.txt")
file_0_500_180_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_180_normal_xover/resultsfinal_compare.txt")
file_0_500_200_normal_xover = open_compare_file(
    "results/sequence_0_pop_500_lambda_200_normal_xover/resultsfinal_compare.txt")

pop_100 = [statistics.mean([item[0] for item in file_0_100_10_normal_xover]),
           statistics.mean([item[0] for item in file_0_100_20_normal_xover]),
           statistics.mean([item[0] for item in file_0_100_30_normal_xover]),
           statistics.mean([item[0] for item in file_0_100_40_normal_xover]),
           statistics.mean([item[0] for item in file_0_100_50_normal_xover]),
           statistics.mean([item[0] for item in file_0_100_60_normal_xover]),
           statistics.mean([item[0] for item in file_0_100_70_normal_xover]),
           statistics.mean([item[0] for item in file_0_100_80_normal_xover]),
           statistics.mean([item[0] for item in file_0_100_90_normal_xover]), 0, 0, 0, 0, 0, 0, 0, 0, 0]
print("100: Min mean: {}, Index: {}".format(min(pop_100), pop_100.index(min(pop_100))))

pop_200 = [statistics.mean([item[0] for item in file_0_200_10_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_20_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_30_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_40_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_50_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_60_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_70_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_80_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_90_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_100_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_110_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_120_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_130_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_140_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_150_normal_xover]),
           statistics.mean([item[0] for item in file_0_200_160_normal_xover]), 0, 0]
print("200: Min mean: {}, Index: {}".format(min(pop_200), pop_200.index(min(pop_200))))

pop_300 = [statistics.mean([item[0] for item in file_0_300_10_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_20_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_30_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_40_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_50_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_60_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_70_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_80_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_90_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_100_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_110_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_120_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_130_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_140_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_150_normal_xover]),
           statistics.mean([item[0] for item in file_0_300_160_normal_xover]), 0, 0]
print("300: Min mean: {}, Index: {}".format(min(pop_300), pop_300.index(min(pop_300))))

pop_400 = [statistics.mean([item[0] for item in file_0_400_10_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_20_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_30_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_40_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_50_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_60_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_70_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_80_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_90_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_100_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_110_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_120_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_130_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_140_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_150_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_160_normal_xover]),
           statistics.mean([item[0] for item in file_0_400_180_normal_xover]), 0]
print("400: Min mean: {}, Index: {}".format(min(pop_400), pop_400.index(min(pop_400))))

pop_500 = [statistics.mean([item[0] for item in file_0_500_10_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_20_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_30_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_40_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_50_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_60_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_70_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_80_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_90_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_100_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_110_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_120_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_130_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_140_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_150_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_160_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_180_normal_xover]),
           statistics.mean([item[0] for item in file_0_500_200_normal_xover])]
print("500: Min mean: {}, Index: {}".format(min(pop_500), pop_500.index(min(pop_500))))

y_pop = [pop_100, pop_200, pop_300, pop_400, pop_500]
x_lambda = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200]

fig = plt.figure(figsize=(10, 20))

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=5, sharey=True)
fig.set_size_inches(10, 12)

ax1.bar(x_lambda, y_pop[0], color='c', width=3)
plt.xlabel('lambda')
plt.ylabel('mean fitness')
ax1.set_title('pop size 100')
ax1.yaxis.set_ticks([0, -4, -8])
ax1.xaxis.set_ticks(x_lambda)

ax2.bar(x_lambda, y_pop[1], color='y', width=3)
ax2.set_title('pop size 200')
ax2.yaxis.set_ticks([0, -4, -8])
ax2.xaxis.set_ticks(x_lambda)

ax3.bar(x_lambda, y_pop[2], color='r', width=3)
ax3.set_title('pop size 300')
ax3.yaxis.set_ticks([0, -4, -8])
ax3.xaxis.set_ticks(x_lambda)

ax4.bar(x_lambda, y_pop[3], color='b', width=3)
ax4.set_title('pop size 400')
ax4.yaxis.set_ticks([0, -4, -8])
ax4.xaxis.set_ticks(x_lambda)

ax5.bar(x_lambda, y_pop[4], color='m', width=3)
ax5.set_title('pop size 500')
ax5.yaxis.set_ticks([0, -4, -8])
ax5.xaxis.set_ticks(x_lambda)

plt.subplots_adjust(hspace=1)
plt.savefig("different_pop_sizes_lambdas_mean.png")
plt.close()

pop_100 = [min([item[0] for item in file_0_100_10_normal_xover]),
           min([item[0] for item in file_0_100_20_normal_xover]),
           min([item[0] for item in file_0_100_30_normal_xover]),
           min([item[0] for item in file_0_100_40_normal_xover]),
           min([item[0] for item in file_0_100_50_normal_xover]),
           min([item[0] for item in file_0_100_60_normal_xover]),
           min([item[0] for item in file_0_100_70_normal_xover]),
           min([item[0] for item in file_0_100_80_normal_xover]),
           min([item[0] for item in file_0_100_90_normal_xover]), 0, 0, 0, 0, 0, 0, 0, 0, 0]
print("100: Min: {}, Index: {}".format(min(pop_100), pop_100.index(min(pop_100))))

pop_200 = [min([item[0] for item in file_0_200_10_normal_xover]),
           min([item[0] for item in file_0_200_20_normal_xover]),
           min([item[0] for item in file_0_200_30_normal_xover]),
           min([item[0] for item in file_0_200_40_normal_xover]),
           min([item[0] for item in file_0_200_50_normal_xover]),
           min([item[0] for item in file_0_200_60_normal_xover]),
           min([item[0] for item in file_0_200_70_normal_xover]),
           min([item[0] for item in file_0_200_80_normal_xover]),
           min([item[0] for item in file_0_200_90_normal_xover]),
           min([item[0] for item in file_0_200_100_normal_xover]),
           min([item[0] for item in file_0_200_110_normal_xover]),
           min([item[0] for item in file_0_200_120_normal_xover]),
           min([item[0] for item in file_0_200_130_normal_xover]),
           min([item[0] for item in file_0_200_140_normal_xover]),
           min([item[0] for item in file_0_200_150_normal_xover]),
           min([item[0] for item in file_0_200_160_normal_xover]), 0, 0]
print("200: Min: {}, Index: {}".format(min(pop_200), pop_200.index(min(pop_200))))


pop_300 = [min([item[0] for item in file_0_300_10_normal_xover]),
           min([item[0] for item in file_0_300_20_normal_xover]),
           min([item[0] for item in file_0_300_30_normal_xover]),
           min([item[0] for item in file_0_300_40_normal_xover]),
           min([item[0] for item in file_0_300_50_normal_xover]),
           min([item[0] for item in file_0_300_60_normal_xover]),
           min([item[0] for item in file_0_300_70_normal_xover]),
           min([item[0] for item in file_0_300_80_normal_xover]),
           min([item[0] for item in file_0_300_90_normal_xover]),
           min([item[0] for item in file_0_300_100_normal_xover]),
           min([item[0] for item in file_0_300_110_normal_xover]),
           min([item[0] for item in file_0_300_120_normal_xover]),
           min([item[0] for item in file_0_300_130_normal_xover]),
           min([item[0] for item in file_0_300_140_normal_xover]),
           min([item[0] for item in file_0_300_150_normal_xover]),
           min([item[0] for item in file_0_300_160_normal_xover]), 0, 0]
print("300: Min: {}, Index: {}".format(min(pop_300), pop_300.index(min(pop_300))))

pop_400 = [min([item[0] for item in file_0_400_10_normal_xover]),
           min([item[0] for item in file_0_400_20_normal_xover]),
           min([item[0] for item in file_0_400_30_normal_xover]),
           min([item[0] for item in file_0_400_40_normal_xover]),
           min([item[0] for item in file_0_400_50_normal_xover]),
           min([item[0] for item in file_0_400_60_normal_xover]),
           min([item[0] for item in file_0_400_70_normal_xover]),
           min([item[0] for item in file_0_400_80_normal_xover]),
           min([item[0] for item in file_0_400_90_normal_xover]),
           min([item[0] for item in file_0_400_100_normal_xover]),
           min([item[0] for item in file_0_400_110_normal_xover]),
           min([item[0] for item in file_0_400_120_normal_xover]),
           min([item[0] for item in file_0_400_130_normal_xover]),
           min([item[0] for item in file_0_400_140_normal_xover]),
           min([item[0] for item in file_0_400_150_normal_xover]),
           min([item[0] for item in file_0_400_160_normal_xover]),
           min([item[0] for item in file_0_400_180_normal_xover]), 0]
print("400: Min: {}, Index: {}".format(min(pop_400), pop_400.index(min(pop_400))))

pop_500 = [min([item[0] for item in file_0_500_10_normal_xover]),
           min([item[0] for item in file_0_500_20_normal_xover]),
           min([item[0] for item in file_0_500_30_normal_xover]),
           min([item[0] for item in file_0_500_40_normal_xover]),
           min([item[0] for item in file_0_500_50_normal_xover]),
           min([item[0] for item in file_0_500_60_normal_xover]),
           min([item[0] for item in file_0_500_70_normal_xover]),
           min([item[0] for item in file_0_500_80_normal_xover]),
           min([item[0] for item in file_0_500_90_normal_xover]),
           min([item[0] for item in file_0_500_100_normal_xover]),
           min([item[0] for item in file_0_500_110_normal_xover]),
           min([item[0] for item in file_0_500_120_normal_xover]),
           min([item[0] for item in file_0_500_130_normal_xover]),
           min([item[0] for item in file_0_500_140_normal_xover]),
           min([item[0] for item in file_0_500_150_normal_xover]),
           min([item[0] for item in file_0_500_160_normal_xover]),
           min([item[0] for item in file_0_500_180_normal_xover]),
           min([item[0] for item in file_0_500_200_normal_xover])]
print("500: Min: {}, Index: {}".format(min(pop_500), pop_500.index(min(pop_500))))

y_pop = [pop_100, pop_200, pop_300, pop_400, pop_500]
x_lambda = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200]

fig = plt.figure(figsize=(10, 20))

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=5, sharey=True)
fig.set_size_inches(10, 12)

ax1.bar(x_lambda, y_pop[0], color='c', width=3)
plt.xlabel('lambda')
plt.ylabel('min fitness')
ax1.set_title('pop size 100')
ax1.yaxis.set_ticks([0, -4, -8])
ax1.xaxis.set_ticks(x_lambda)

ax2.bar(x_lambda, y_pop[1], color='y', width=3)
ax2.set_title('pop size 200')
ax2.yaxis.set_ticks([0, -4, -8])
ax2.xaxis.set_ticks(x_lambda)

ax3.bar(x_lambda, y_pop[2], color='r', width=3)
ax3.set_title('pop size 300')
ax3.yaxis.set_ticks([0, -4, -8])
ax3.xaxis.set_ticks(x_lambda)

ax4.bar(x_lambda, y_pop[3], color='b', width=3)
ax4.set_title('pop size 400')
ax4.yaxis.set_ticks([0, -4, -8])
ax4.xaxis.set_ticks(x_lambda)

ax5.bar(x_lambda, y_pop[4], color='m', width=3)
ax5.set_title('pop size 500')
ax5.yaxis.set_ticks([0, -4, -8])
ax5.xaxis.set_ticks(x_lambda)

plt.subplots_adjust(hspace=1)
plt.savefig("different_pop_sizes_lambdas_min.png")

plt.close()

pop_100 = [([item[0] for item in file_0_100_10_normal_xover]).count(-8),
           ([item[0] for item in file_0_100_20_normal_xover]).count(-8),
           ([item[0] for item in file_0_100_30_normal_xover]).count(-8),
           ([item[0] for item in file_0_100_40_normal_xover]).count(-8),
           ([item[0] for item in file_0_100_50_normal_xover]).count(-8),
           ([item[0] for item in file_0_100_60_normal_xover]).count(-8),
           ([item[0] for item in file_0_100_70_normal_xover]).count(-8),
           ([item[0] for item in file_0_100_80_normal_xover]).count(-8),
           ([item[0] for item in file_0_100_90_normal_xover]).count(-8), 0, 0, 0, 0, 0, 0, 0, 0, 0]
print("100: Max Count: {}, Index: {}".format(max(pop_100), pop_100.index(max(pop_100))))

pop_200 = [([item[0] for item in file_0_200_10_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_20_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_30_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_40_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_50_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_60_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_70_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_80_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_90_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_100_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_110_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_120_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_130_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_140_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_150_normal_xover]).count(-8),
           ([item[0] for item in file_0_200_160_normal_xover]).count(-8), 0, 0]
print("200: Max Count: {}, Index: {}".format(max(pop_200), pop_200.index(max(pop_200))))

pop_300 = [([item[0] for item in file_0_300_10_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_20_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_30_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_40_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_50_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_60_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_70_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_80_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_90_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_100_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_110_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_120_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_130_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_140_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_150_normal_xover]).count(-8),
           ([item[0] for item in file_0_300_160_normal_xover]).count(-8), 0, 0]
print("300: Max Count: {}, Index: {}".format(max(pop_300), pop_300.index(max(pop_300))))

pop_400 = [([item[0] for item in file_0_400_10_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_20_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_30_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_40_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_50_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_60_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_70_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_80_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_90_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_100_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_110_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_120_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_130_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_140_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_150_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_160_normal_xover]).count(-8),
           ([item[0] for item in file_0_400_180_normal_xover]).count(-8), 0]
print("400: Max Count: {}, Index: {}".format(max(pop_400), pop_400.index(max(pop_400))))

pop_500 = [([item[0] for item in file_0_500_10_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_20_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_30_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_40_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_50_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_60_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_70_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_80_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_90_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_100_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_110_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_120_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_130_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_140_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_150_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_160_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_180_normal_xover]).count(-8),
           ([item[0] for item in file_0_500_200_normal_xover]).count(-8)]
print("500: Max Count: {}, Index: {}".format(max(pop_500), pop_500.index(max(pop_500))))

y_pop = [pop_100, pop_200, pop_300, pop_400, pop_500]
x_lambda = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200]

fig = plt.figure(figsize=(10, 20))

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=5, sharey=True)
fig.set_size_inches(10, 12)

ax1.bar(x_lambda, y_pop[0], color='c', width=3)
plt.xlabel('lambda')
plt.ylabel('count -8')
ax1.set_title('pop size 100')
ax1.yaxis.set_ticks([0, 5, 10, 15, 20, 25, 30])
ax1.xaxis.set_ticks(x_lambda)

ax2.bar(x_lambda, y_pop[1], color='y', width=3)
ax2.set_title('pop size 200')
ax2.yaxis.set_ticks([0, 5, 10, 15, 20, 25, 30])
ax2.xaxis.set_ticks(x_lambda)

ax3.bar(x_lambda, y_pop[2], color='r', width=3)
ax3.set_title('pop size 300')
ax3.yaxis.set_ticks([0, 5, 10, 15, 20, 25, 30])
ax3.xaxis.set_ticks(x_lambda)

ax4.bar(x_lambda, y_pop[3], color='b', width=3)
ax4.set_title('pop size 400')
ax4.yaxis.set_ticks([0, 5, 10, 15, 20, 25, 30])
ax4.xaxis.set_ticks(x_lambda)

ax5.bar(x_lambda, y_pop[4], color='m', width=3)
ax5.set_title('pop size 500')
ax5.yaxis.set_ticks([0, 5, 10, 15, 20, 25, 30])
ax5.xaxis.set_ticks(x_lambda)

plt.subplots_adjust(hspace=1)
plt.savefig("different_pop_sizes_lambdas_count.png")

plt.close()
