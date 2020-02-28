import statistics

import matplotlib.pyplot as plt
import pandas as pd

from IO_handler import open_compare_file

file_0_100_10_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_10_normal_xover/resultsfinal_compare.txt")
file_0_100_10_normal_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_10_normal_xover_and_pioneer/resultsfinal_compare.txt")
file_0_100_10_rotate_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_10_rotate_xover/resultsfinal_compare.txt")
file_0_100_10_rotate_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_10_rotate_xover_and_pioneer/resultsfinal_compare.txt")

file_0_100_20_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_20_normal_xover/resultsfinal_compare.txt")
file_0_100_20_normal_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_20_normal_xover_and_pioneer/resultsfinal_compare.txt")
file_0_100_20_rotate_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_20_rotate_xover/resultsfinal_compare.txt")
file_0_100_20_rotate_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_20_rotate_xover_and_pioneer/resultsfinal_compare.txt")

file_0_100_30_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_30_normal_xover/resultsfinal_compare.txt")
file_0_100_30_normal_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_30_normal_xover_and_pioneer/resultsfinal_compare.txt")
file_0_100_30_rotate_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_30_rotate_xover/resultsfinal_compare.txt")
file_0_100_30_rotate_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_30_rotate_xover_and_pioneer/resultsfinal_compare.txt")

file_0_100_40_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_40_normal_xover/resultsfinal_compare.txt")
file_0_100_40_normal_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_40_normal_xover_and_pioneer/resultsfinal_compare.txt")
file_0_100_40_rotate_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_40_rotate_xover/resultsfinal_compare.txt")
file_0_100_40_rotate_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_40_rotate_xover_and_pioneer/resultsfinal_compare.txt")

file_0_100_50_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_50_normal_xover/resultsfinal_compare.txt")
file_0_100_50_normal_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_50_normal_xover_and_pioneer/resultsfinal_compare.txt")
file_0_100_50_rotate_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_50_rotate_xover/resultsfinal_compare.txt")
file_0_100_50_rotate_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_50_rotate_xover_and_pioneer/resultsfinal_compare.txt")

file_0_100_60_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_60_normal_xover/resultsfinal_compare.txt")
file_0_100_60_normal_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_60_normal_xover_and_pioneer/resultsfinal_compare.txt")
file_0_100_60_rotate_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_60_rotate_xover/resultsfinal_compare.txt")
file_0_100_60_rotate_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_60_rotate_xover_and_pioneer/resultsfinal_compare.txt")

file_0_100_70_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_70_normal_xover/resultsfinal_compare.txt")
file_0_100_70_normal_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_70_normal_xover_and_pioneer/resultsfinal_compare.txt")
file_0_100_70_rotate_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_70_rotate_xover/resultsfinal_compare.txt")
file_0_100_70_rotate_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_70_rotate_xover_and_pioneer/resultsfinal_compare.txt")

file_0_100_80_normal_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_80_normal_xover/resultsfinal_compare.txt")
file_0_100_80_normal_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_80_normal_xover_and_pioneer/resultsfinal_compare.txt")
file_0_100_80_rotate_xover = open_compare_file(
    "results/sequence_0_pop_100_lambda_80_rotate_xover/resultsfinal_compare.txt")
file_0_100_80_rotate_xover_and_pioneer = open_compare_file(
    "results/sequence_0_pop_100_lambda_80_rotate_xover_and_pioneer/resultsfinal_compare.txt")

normal_xover_10 = min([item[0] for item in file_0_100_10_normal_xover])
normal_xover_and_pioneer_10 = min([item[0] for item in file_0_100_10_normal_xover_and_pioneer])
rotate_xover_10 = min([item[0] for item in file_0_100_10_rotate_xover])
rotate_xover_and_pioneer_10 = min([item[0] for item in file_0_100_10_rotate_xover_and_pioneer])

normal_xover_20 = min([item[0] for item in file_0_100_20_normal_xover])
normal_xover_and_pioneer_20 = min([item[0] for item in file_0_100_20_normal_xover_and_pioneer])
rotate_xover_20 = min([item[0] for item in file_0_100_20_rotate_xover])
rotate_xover_and_pioneer_20 = min([item[0] for item in file_0_100_20_rotate_xover_and_pioneer])

normal_xover_30 = min([item[0] for item in file_0_100_30_normal_xover])
normal_xover_and_pioneer_30 = min([item[0] for item in file_0_100_30_normal_xover_and_pioneer])
rotate_xover_30 = min([item[0] for item in file_0_100_30_rotate_xover])
rotate_xover_and_pioneer_30 = min([item[0] for item in file_0_100_30_rotate_xover_and_pioneer])

normal_xover_40 = min([item[0] for item in file_0_100_40_normal_xover])
normal_xover_and_pioneer_40 = min([item[0] for item in file_0_100_40_normal_xover_and_pioneer])
rotate_xover_40 = min([item[0] for item in file_0_100_40_rotate_xover])
rotate_xover_and_pioneer_40 = min([item[0] for item in file_0_100_40_rotate_xover_and_pioneer])

normal_xover_50 = min([item[0] for item in file_0_100_50_normal_xover])
normal_xover_and_pioneer_50 = min([item[0] for item in file_0_100_50_normal_xover_and_pioneer])
rotate_xover_50 = min([item[0] for item in file_0_100_50_rotate_xover])
rotate_xover_and_pioneer_50 = min([item[0] for item in file_0_100_50_rotate_xover_and_pioneer])

normal_xover_60 = min([item[0] for item in file_0_100_60_normal_xover])
normal_xover_and_pioneer_60 = min([item[0] for item in file_0_100_60_normal_xover_and_pioneer])
rotate_xover_60 = min([item[0] for item in file_0_100_60_rotate_xover])
rotate_xover_and_pioneer_60 = min([item[0] for item in file_0_100_60_rotate_xover_and_pioneer])

normal_xover_70 = min([item[0] for item in file_0_100_70_normal_xover])
normal_xover_and_pioneer_70 = min([item[0] for item in file_0_100_70_normal_xover_and_pioneer])
rotate_xover_70 = min([item[0] for item in file_0_100_70_rotate_xover])
rotate_xover_and_pioneer_70 = min([item[0] for item in file_0_100_70_rotate_xover_and_pioneer])

normal_xover_80 = min([item[0] for item in file_0_100_80_normal_xover])
normal_xover_and_pioneer_80 = min([item[0] for item in file_0_100_80_normal_xover_and_pioneer])
rotate_xover_80 = min([item[0] for item in file_0_100_80_rotate_xover])
rotate_xover_and_pioneer_80 = min([item[0] for item in file_0_100_80_rotate_xover_and_pioneer])

normal_xover = [normal_xover_10, normal_xover_20, normal_xover_30, normal_xover_40, normal_xover_50, normal_xover_60,
                normal_xover_70, normal_xover_80]
normal_xover_and_pioneer = [normal_xover_and_pioneer_10, normal_xover_and_pioneer_20, normal_xover_and_pioneer_30,
                            normal_xover_and_pioneer_40, normal_xover_and_pioneer_50, normal_xover_and_pioneer_60,
                            normal_xover_and_pioneer_70, normal_xover_and_pioneer_80]
rotate_xover = [rotate_xover_10, rotate_xover_20, rotate_xover_30, rotate_xover_40, rotate_xover_50, rotate_xover_60,
                rotate_xover_70, rotate_xover_80]
rotate_xover_and_pioneer = [rotate_xover_and_pioneer_10, rotate_xover_and_pioneer_20, rotate_xover_and_pioneer_30,
                            rotate_xover_and_pioneer_40, rotate_xover_and_pioneer_50, rotate_xover_and_pioneer_60,
                            rotate_xover_and_pioneer_70, rotate_xover_and_pioneer_80]
groups = [normal_xover, normal_xover_and_pioneer, rotate_xover, rotate_xover_and_pioneer]
column_label = ['normal xover', 'normal xover and pioneer', 'rotate xover', 'rotate xover and pioneer']
group_label = [x for x in range(10, 81, 10)]

# Convert data to pandas DataFrame.
df = pd.DataFrame(groups, index=column_label, columns=group_label).T

# Plot.
df.plot.bar(color=['r', 'b', 'c', 'm'])
plt.xlabel('Lambda Mutations')
plt.ylabel('Fitness')
plt.savefig("different_xovers_and_lambdas_min.png")
plt.close()


normal_xover_10 = statistics.mean([item[0] for item in file_0_100_10_normal_xover])
normal_xover_and_pioneer_10 = statistics.mean([item[0] for item in file_0_100_10_normal_xover_and_pioneer])
rotate_xover_10 = statistics.mean([item[0] for item in file_0_100_10_rotate_xover])
rotate_xover_and_pioneer_10 = statistics.mean([item[0] for item in file_0_100_10_rotate_xover_and_pioneer])

normal_xover_20 = statistics.mean([item[0] for item in file_0_100_20_normal_xover])
normal_xover_and_pioneer_20 = statistics.mean([item[0] for item in file_0_100_20_normal_xover_and_pioneer])
rotate_xover_20 = statistics.mean([item[0] for item in file_0_100_20_rotate_xover])
rotate_xover_and_pioneer_20 = statistics.mean([item[0] for item in file_0_100_20_rotate_xover_and_pioneer])

normal_xover_30 = statistics.mean([item[0] for item in file_0_100_30_normal_xover])
normal_xover_and_pioneer_30 = statistics.mean([item[0] for item in file_0_100_30_normal_xover_and_pioneer])
rotate_xover_30 = statistics.mean([item[0] for item in file_0_100_30_rotate_xover])
rotate_xover_and_pioneer_30 = statistics.mean([item[0] for item in file_0_100_30_rotate_xover_and_pioneer])

normal_xover_40 = statistics.mean([item[0] for item in file_0_100_40_normal_xover])
normal_xover_and_pioneer_40 = statistics.mean([item[0] for item in file_0_100_40_normal_xover_and_pioneer])
rotate_xover_40 = statistics.mean([item[0] for item in file_0_100_40_rotate_xover])
rotate_xover_and_pioneer_40 = statistics.mean([item[0] for item in file_0_100_40_rotate_xover_and_pioneer])

normal_xover_50 = statistics.mean([item[0] for item in file_0_100_50_normal_xover])
normal_xover_and_pioneer_50 = statistics.mean([item[0] for item in file_0_100_50_normal_xover_and_pioneer])
rotate_xover_50 = statistics.mean([item[0] for item in file_0_100_50_rotate_xover])
rotate_xover_and_pioneer_50 = statistics.mean([item[0] for item in file_0_100_50_rotate_xover_and_pioneer])

normal_xover_60 = statistics.mean([item[0] for item in file_0_100_60_normal_xover])
normal_xover_and_pioneer_60 = statistics.mean([item[0] for item in file_0_100_60_normal_xover_and_pioneer])
rotate_xover_60 = statistics.mean([item[0] for item in file_0_100_60_rotate_xover])
rotate_xover_and_pioneer_60 = statistics.mean([item[0] for item in file_0_100_60_rotate_xover_and_pioneer])

normal_xover_70 = statistics.mean([item[0] for item in file_0_100_70_normal_xover])
normal_xover_and_pioneer_70 = statistics.mean([item[0] for item in file_0_100_70_normal_xover_and_pioneer])
rotate_xover_70 = statistics.mean([item[0] for item in file_0_100_70_rotate_xover])
rotate_xover_and_pioneer_70 = statistics.mean([item[0] for item in file_0_100_70_rotate_xover_and_pioneer])

normal_xover_80 = statistics.mean([item[0] for item in file_0_100_80_normal_xover])
normal_xover_and_pioneer_80 = statistics.mean([item[0] for item in file_0_100_80_normal_xover_and_pioneer])
rotate_xover_80 = statistics.mean([item[0] for item in file_0_100_80_rotate_xover])
rotate_xover_and_pioneer_80 = statistics.mean([item[0] for item in file_0_100_80_rotate_xover_and_pioneer])

normal_xover = [normal_xover_10, normal_xover_20, normal_xover_30, normal_xover_40, normal_xover_50, normal_xover_60,
                normal_xover_70, normal_xover_80]
normal_xover_and_pioneer = [normal_xover_and_pioneer_10, normal_xover_and_pioneer_20, normal_xover_and_pioneer_30,
                            normal_xover_and_pioneer_40, normal_xover_and_pioneer_50, normal_xover_and_pioneer_60,
                            normal_xover_and_pioneer_70, normal_xover_and_pioneer_80]
rotate_xover = [rotate_xover_10, rotate_xover_20, rotate_xover_30, rotate_xover_40, rotate_xover_50, rotate_xover_60,
                rotate_xover_70, rotate_xover_80]
rotate_xover_and_pioneer = [rotate_xover_and_pioneer_10, rotate_xover_and_pioneer_20, rotate_xover_and_pioneer_30,
                            rotate_xover_and_pioneer_40, rotate_xover_and_pioneer_50, rotate_xover_and_pioneer_60,
                            rotate_xover_and_pioneer_70, rotate_xover_and_pioneer_80]
groups = [normal_xover, normal_xover_and_pioneer, rotate_xover, rotate_xover_and_pioneer]
column_label = ['normal xover', 'normal xover and pioneer', 'rotate xover', 'rotate xover and pioneer']
group_label = [x for x in range(10, 81, 10)]

# Convert data to pandas DataFrame.
df = pd.DataFrame(groups, index=column_label, columns=group_label).T

# Plot.
df.plot.bar(color=['r', 'b', 'c', 'm'])
plt.xlabel('Lambda Mutations')
plt.ylabel('Fitness')
plt.savefig("different_xovers_and_lambdas_mean.png")
plt.close()


normal_xover_10 = ([item[0] for item in file_0_100_10_normal_xover]).count(-8)
normal_xover_and_pioneer_10 =([item[0] for item in file_0_100_10_normal_xover_and_pioneer]).count(-8)
rotate_xover_10 = ([item[0] for item in file_0_100_10_rotate_xover]).count(-8)
rotate_xover_and_pioneer_10 = ([item[0] for item in file_0_100_10_rotate_xover_and_pioneer]).count(-8)

normal_xover_20 = ([item[0] for item in file_0_100_20_normal_xover]).count(-8)
normal_xover_and_pioneer_20 = ([item[0] for item in file_0_100_20_normal_xover_and_pioneer]).count(-8)
rotate_xover_20 = ([item[0] for item in file_0_100_20_rotate_xover]).count(-8)
rotate_xover_and_pioneer_20 = ([item[0] for item in file_0_100_20_rotate_xover_and_pioneer]).count(-8)

normal_xover_30 = ([item[0] for item in file_0_100_30_normal_xover]).count(-8)
normal_xover_and_pioneer_30 = ([item[0] for item in file_0_100_30_normal_xover_and_pioneer]).count(-8)
rotate_xover_30 = ([item[0] for item in file_0_100_30_rotate_xover]).count(-8)
rotate_xover_and_pioneer_30 = ([item[0] for item in file_0_100_30_rotate_xover_and_pioneer]).count(-8)

normal_xover_40 = ([item[0] for item in file_0_100_40_normal_xover]).count(-8)
normal_xover_and_pioneer_40 = ([item[0] for item in file_0_100_40_normal_xover_and_pioneer]).count(-8)
rotate_xover_40 = ([item[0] for item in file_0_100_40_rotate_xover]).count(-8)
rotate_xover_and_pioneer_40 = ([item[0] for item in file_0_100_40_rotate_xover_and_pioneer]).count(-8)

normal_xover_50 = ([item[0] for item in file_0_100_50_normal_xover]).count(-8)
normal_xover_and_pioneer_50 = ([item[0] for item in file_0_100_50_normal_xover_and_pioneer]).count(-8)
rotate_xover_50 = ([item[0] for item in file_0_100_50_rotate_xover]).count(-8)
rotate_xover_and_pioneer_50 = ([item[0] for item in file_0_100_50_rotate_xover_and_pioneer]).count(-8)

normal_xover_60 = ([item[0] for item in file_0_100_60_normal_xover]).count(-8)
normal_xover_and_pioneer_60 = ([item[0] for item in file_0_100_60_normal_xover_and_pioneer]).count(-8)
rotate_xover_60 = ([item[0] for item in file_0_100_60_rotate_xover]).count(-8)
rotate_xover_and_pioneer_60 = ([item[0] for item in file_0_100_60_rotate_xover_and_pioneer]).count(-8)

normal_xover_70 = ([item[0] for item in file_0_100_70_normal_xover]).count(-8)
normal_xover_and_pioneer_70 = ([item[0] for item in file_0_100_70_normal_xover_and_pioneer]).count(-8)
rotate_xover_70 = ([item[0] for item in file_0_100_70_rotate_xover]).count(-8)
rotate_xover_and_pioneer_70 = ([item[0] for item in file_0_100_70_rotate_xover_and_pioneer]).count(-8)

normal_xover_80 = ([item[0] for item in file_0_100_80_normal_xover]).count(-8)
normal_xover_and_pioneer_80 = ([item[0] for item in file_0_100_80_normal_xover_and_pioneer]).count(-8)
rotate_xover_80 = ([item[0] for item in file_0_100_80_rotate_xover]).count(-8)
rotate_xover_and_pioneer_80 = ([item[0] for item in file_0_100_80_rotate_xover_and_pioneer]).count(-8)

normal_xover = [normal_xover_10, normal_xover_20, normal_xover_30, normal_xover_40, normal_xover_50, normal_xover_60,
                normal_xover_70, normal_xover_80]
normal_xover_and_pioneer = [normal_xover_and_pioneer_10, normal_xover_and_pioneer_20, normal_xover_and_pioneer_30,
                            normal_xover_and_pioneer_40, normal_xover_and_pioneer_50, normal_xover_and_pioneer_60,
                            normal_xover_and_pioneer_70, normal_xover_and_pioneer_80]
rotate_xover = [rotate_xover_10, rotate_xover_20, rotate_xover_30, rotate_xover_40, rotate_xover_50, rotate_xover_60,
                rotate_xover_70, rotate_xover_80]
rotate_xover_and_pioneer = [rotate_xover_and_pioneer_10, rotate_xover_and_pioneer_20, rotate_xover_and_pioneer_30,
                            rotate_xover_and_pioneer_40, rotate_xover_and_pioneer_50, rotate_xover_and_pioneer_60,
                            rotate_xover_and_pioneer_70, rotate_xover_and_pioneer_80]
groups = [normal_xover, normal_xover_and_pioneer, rotate_xover, rotate_xover_and_pioneer]
column_label = ['normal xover', 'normal xover and pioneer', 'rotate xover', 'rotate xover and pioneer']
group_label = [x for x in range(10, 81, 10)]

# Convert data to pandas DataFrame.
df = pd.DataFrame(groups, index=column_label, columns=group_label).T

# Plot.
df.plot.bar(color=['r', 'b', 'c', 'm'])
plt.xlabel('Lambda Mutations')
plt.ylabel('Count')
plt.savefig("different_xovers_and_lambdas_count.png")
plt.close()
