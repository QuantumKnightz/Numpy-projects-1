# output
# How many random numbers do you want? 10
# How many decimals? 6
# [3.587926, 2.254949, 3.881201, 9.792585, 4.456965, 9.225752, 1.18653, 5.913049, 1.068376, 9.269615]

import numpy as np
import random


n = int(input("How many random numbers do you want? "))
d = int(input("How many decimals? "))

num = np.round(np.random.uniform(0, 10, n), d)
print(num)