import numpy as np
import pandas as pd

# load data (same for p1 and p2)

rules = np.array(pd.read_table('data/day5_1.txt', sep='|', header=None))
with open('data/day5_2.txt', 'r') as f:
    pages_ = f.read()
pages = pages_.strip().splitlines()

# P1:

# room for solution
medians = []

# main loop:
for line in pages:
    numbers = list(map(int, line.split(',')))
    n = len(numbers)
    ordered = True
    for i in range(len(numbers)):
        for rule in rules:
            if numbers[i] == int(rule[0]):
                for j in range(i):
                    if numbers[j] == int(rule[1]):
                        ordered = False
                        break

    if ordered:
        mid_idx=(n - 1) // 2  
        medians.append(numbers[mid_idx])  


print(np.sum(medians))

# P2:

medians = []

def reorder_array(nums):
    tmp = nums[:]  
    changed = True
    while changed:
        changed = False
        for rule in rules:
            x, y = int(rule[0]), int(rule[1])
            if x in tmp and y in tmp:
                idx_x, idx_y = tmp.index(x), tmp.index(y)
                if idx_x > idx_y:
                    tmp[idx_x], tmp[idx_y] = tmp[idx_y], tmp[idx_x]
                    changed = True
    return nums
  
# main loop:
for line in pages:
    numbers = list(map(int, line.split(',')))
    n = len(numbers)
    ordered = True
    for i in range(len(numbers)):
        for rule in rules:
            if numbers[i] == int(rule[0]):
                for j in range(i):
                    if numbers[j] == int(rule[1]):
                        ordered = False
                        break

    if not ordered:
        temp = reorder_array(numbers)
        mid_idx=(n - 1) // 2  
        medians.append(temp[mid_idx])  
    else:
        temp = numbers

print(np.sum(medians))
