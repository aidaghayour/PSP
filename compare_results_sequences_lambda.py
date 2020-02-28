import statistics

import matplotlib.pyplot as plt
import pandas as pd

from IO_handler import open_compare_file

file_0_500_30 = open_compare_file(
    "results/sequence_0_pop_500_lambda_30/resultsfinal_compare.txt")
file_0_500_40 = open_compare_file(
    "results/sequence_0_pop_500_lambda_40/resultsfinal_compare.txt")
file_0_500_50 = open_compare_file(
    "results/sequence_0_pop_500_lambda_50/resultsfinal_compare.txt")

file_1_500_30 = open_compare_file(
    "results/sequence_1_pop_500_lambda_30/resultsfinal_compare.txt")
file_1_500_40 = open_compare_file(
    "results/sequence_1_pop_500_lambda_40/resultsfinal_compare.txt")
file_1_500_50 = open_compare_file(
    "results/sequence_1_pop_500_lambda_50/resultsfinal_compare.txt")

file_2_500_30 = open_compare_file(
    "results/sequence_2_pop_500_lambda_30/resultsfinal_compare.txt")
file_2_500_40 = open_compare_file(
    "results/sequence_2_pop_500_lambda_40/resultsfinal_compare.txt")
file_2_500_50 = open_compare_file(
    "results/sequence_2_pop_500_lambda_50/resultsfinal_compare.txt")

file_3_500_30 = open_compare_file(
    "results/sequence_3_pop_500_lambda_30/resultsfinal_compare.txt")
file_3_500_40 = open_compare_file(
    "results/sequence_3_pop_500_lambda_40/resultsfinal_compare.txt")
file_3_500_50 = open_compare_file(
    "results/sequence_3_pop_500_lambda_50/resultsfinal_compare.txt")

file_4_500_30 = open_compare_file(
    "results/sequence_4_pop_500_lambda_30/resultsfinal_compare.txt")
file_4_500_40 = open_compare_file(
    "results/sequence_4_pop_500_lambda_40/resultsfinal_compare.txt")
file_4_500_50 = open_compare_file(
    "results/sequence_4_pop_500_lambda_50/resultsfinal_compare.txt")

file_5_500_30 = open_compare_file(
    "results/sequence_5_pop_500_lambda_30/resultsfinal_compare.txt")
file_5_500_40 = open_compare_file(
    "results/sequence_5_pop_500_lambda_40/resultsfinal_compare.txt")
file_5_500_50 = open_compare_file(
    "results/sequence_5_pop_500_lambda_50/resultsfinal_compare.txt")

file_6_500_30 = open_compare_file(
    "results/sequence_6_pop_500_lambda_30/resultsfinal_compare.txt")
file_6_500_40 = open_compare_file(
    "results/sequence_6_pop_500_lambda_40/resultsfinal_compare.txt")
file_6_500_50 = open_compare_file(
    "results/sequence_6_pop_500_lambda_50/resultsfinal_compare.txt")

file_7_500_30 = open_compare_file(
    "results/sequence_7_pop_500_lambda_30/resultsfinal_compare.txt")
file_7_500_40 = open_compare_file(
    "results/sequence_7_pop_500_lambda_40/resultsfinal_compare.txt")
file_7_500_50 = open_compare_file(
    "results/sequence_7_pop_500_lambda_50/resultsfinal_compare.txt")

sequences_lambda_30 = [min([item[0] for item in file_0_500_30]), min([item[0] for item in file_1_500_30]),
                       min([item[0] for item in file_2_500_30]), min([item[0] for item in file_3_500_30]),
                       min([item[0] for item in file_4_500_30]), min([item[0] for item in file_5_500_30]),
                       min([item[0] for item in file_6_500_30]), min([item[0] for item in file_7_500_30])]

print("Lambda = 30")
for i in range(8):
    print("{}: {}".format(i, sequences_lambda_30[i]))

sequences_lambda_40 = [min([item[0] for item in file_0_500_40]), min([item[0] for item in file_1_500_40]),
                       min([item[0] for item in file_2_500_40]), min([item[0] for item in file_3_500_40]),
                       min([item[0] for item in file_4_500_40]), min([item[0] for item in file_5_500_40]),
                       min([item[0] for item in file_6_500_40]), min([item[0] for item in file_7_500_40])]
print("Lambda = 40")
for i in range(8):
    print("{}: {}".format(i, sequences_lambda_40[i]))

sequences_lambda_50 = [min([item[0] for item in file_0_500_50]), min([item[0] for item in file_1_500_50]),
                       min([item[0] for item in file_2_500_50]), min([item[0] for item in file_3_500_50]),
                       min([item[0] for item in file_4_500_50]), min([item[0] for item in file_5_500_50]),
                       min([item[0] for item in file_6_500_50]), min([item[0] for item in file_7_500_50])]

print("Lambda = 50")
for i in range(8):
    print("{}: {}".format(i, sequences_lambda_50[i]))

groups = [sequences_lambda_30, sequences_lambda_40, sequences_lambda_50]
column_label = ['lambda=30', 'lambda=40', 'lambda=50']
group_label = [x for x in range(1, 9)]

# Convert data to pandas DataFrame.
df = pd.DataFrame(groups, index=column_label, columns=group_label).T

# Plot.
df.plot.bar(color=['m', 'b', 'c'])
plt.xlabel('Sequence')
plt.ylabel('Fitness')
plt.savefig("different_sequences_lambdas_min.png")
plt.close()

sequences_lambda_30 = [statistics.mean([item[0] for item in file_0_500_30]),
                       statistics.mean([item[0] for item in file_1_500_30]),
                       statistics.mean([item[0] for item in file_2_500_30]),
                       statistics.mean([item[0] for item in file_3_500_30]),
                       statistics.mean([item[0] for item in file_4_500_30]),
                       statistics.mean([item[0] for item in file_5_500_30]),
                       statistics.mean([item[0] for item in file_6_500_30]),
                       statistics.mean([item[0] for item in file_7_500_30])]

sequences_lambda_40 = [statistics.mean([item[0] for item in file_0_500_40]),
                       statistics.mean([item[0] for item in file_1_500_40]),
                       statistics.mean([item[0] for item in file_2_500_40]),
                       statistics.mean([item[0] for item in file_3_500_40]),
                       statistics.mean([item[0] for item in file_4_500_40]),
                       statistics.mean([item[0] for item in file_5_500_40]),
                       statistics.mean([item[0] for item in file_6_500_40]),
                       statistics.mean([item[0] for item in file_7_500_40])]

sequences_lambda_40_time = [statistics.mean([item[1] for item in file_0_500_40]),
                            statistics.mean([item[1] for item in file_1_500_40]),
                            statistics.mean([item[1] for item in file_2_500_40]),
                            statistics.mean([item[1] for item in file_3_500_40]),
                            statistics.mean([item[1] for item in file_4_500_40]),
                            statistics.mean([item[1] for item in file_5_500_40]),
                            statistics.mean([item[1] for item in file_6_500_40]),
                            statistics.mean([item[1] for item in file_7_500_40])]
print("Average time 40:")
for i in range(8):
    print("Sequence: {}, Time: {}".format(i, sequences_lambda_40_time[i]))

sequences_lambda_50 = [statistics.mean([item[0] for item in file_0_500_50]),
                       statistics.mean([item[0] for item in file_1_500_50]),
                       statistics.mean([item[0] for item in file_2_500_50]),
                       statistics.mean([item[0] for item in file_3_500_50]),
                       statistics.mean([item[0] for item in file_4_500_50]),
                       statistics.mean([item[0] for item in file_5_500_50]),
                       statistics.mean([item[0] for item in file_6_500_50]),
                       statistics.mean([item[0] for item in file_7_500_50])]

sequences_lambda_50_time = [statistics.mean([item[1] for item in file_0_500_50]),
                            statistics.mean([item[1] for item in file_1_500_50]),
                            statistics.mean([item[1] for item in file_2_500_50]),
                            statistics.mean([item[1] for item in file_3_500_50]),
                            statistics.mean([item[1] for item in file_4_500_50]),
                            statistics.mean([item[1] for item in file_5_500_50]),
                            statistics.mean([item[1] for item in file_6_500_50]),
                            statistics.mean([item[1] for item in file_7_500_50])]

print("Average time 50:")
for i in range(8):
    print("Sequence: {}, Time: {}".format(i, sequences_lambda_50_time[i]))

groups = [sequences_lambda_30, sequences_lambda_40, sequences_lambda_50]
column_label = ['lambda=30', 'lambda=40', 'lambda=50']
group_label = [x for x in range(1, 9)]

# Convert data to pandas DataFrame.
df = pd.DataFrame(groups, index=column_label, columns=group_label).T

# Plot.
df.plot.bar(color=['m', 'b', 'c'])
plt.xlabel('Sequence')
plt.ylabel('Fitness')
plt.savefig("different_sequences_lambdas_mean.png")
plt.close()

sequences_lambda_30 = [([item[0] for item in file_0_500_30]).count(min([item[0] for item in file_0_500_30])),
                       ([item[0] for item in file_1_500_30]).count(min([item[0] for item in file_1_500_30])),
                       ([item[0] for item in file_2_500_30]).count(min([item[0] for item in file_2_500_30])),
                       ([item[0] for item in file_3_500_30]).count(min([item[0] for item in file_3_500_30])),
                       ([item[0] for item in file_4_500_30]).count(min([item[0] for item in file_4_500_30])),
                       ([item[0] for item in file_5_500_30]).count(min([item[0] for item in file_5_500_30])),
                       ([item[0] for item in file_6_500_30]).count(min([item[0] for item in file_6_500_30])),
                       ([item[0] for item in file_7_500_30]).count(min([item[0] for item in file_7_500_30]))]

sequences_lambda_40 = [([item[0] for item in file_0_500_40]).count(min([item[0] for item in file_0_500_40])),
                       ([item[0] for item in file_1_500_40]).count(min([item[0] for item in file_1_500_40])),
                       ([item[0] for item in file_2_500_40]).count(min([item[0] for item in file_2_500_40])),
                       ([item[0] for item in file_3_500_40]).count(min([item[0] for item in file_3_500_40])),
                       ([item[0] for item in file_4_500_40]).count(min([item[0] for item in file_4_500_40])),
                       ([item[0] for item in file_5_500_40]).count(min([item[0] for item in file_5_500_40])),
                       ([item[0] for item in file_6_500_40]).count(min([item[0] for item in file_6_500_40])),
                       ([item[0] for item in file_7_500_40]).count(min([item[0] for item in file_7_500_40]))]

sequences_lambda_50 = [([item[0] for item in file_0_500_50]).count(min([item[0] for item in file_0_500_50])),
                       ([item[0] for item in file_1_500_50]).count(min([item[0] for item in file_1_500_50])),
                       ([item[0] for item in file_2_500_50]).count(min([item[0] for item in file_2_500_50])),
                       ([item[0] for item in file_3_500_50]).count(min([item[0] for item in file_3_500_50])),
                       ([item[0] for item in file_4_500_50]).count(min([item[0] for item in file_4_500_50])),
                       ([item[0] for item in file_5_500_50]).count(min([item[0] for item in file_5_500_50])),
                       ([item[0] for item in file_6_500_50]).count(min([item[0] for item in file_6_500_50])),
                       ([item[0] for item in file_7_500_50]).count(min([item[0] for item in file_7_500_50]))]

groups = [sequences_lambda_30, sequences_lambda_40, sequences_lambda_50]
column_label = ['lambda=30', 'lambda=40', 'lambda=50']
group_label = [x for x in range(1, 9)]

# Convert data to pandas DataFrame.
df = pd.DataFrame(groups, index=column_label, columns=group_label).T

# Plot.
df.plot.bar(color=['m', 'b', 'c'])
plt.xlabel('Sequence')
plt.ylabel('Fitness')
plt.savefig("different_sequences_lambdas_count.png")
plt.close()
