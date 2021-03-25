# !/bin/python3
# roll_die.py
"""Roll a six-sided die 6,000,000 times."""

import random

# number of die rolls
num_roll = 6_000_000
# face frequency counters
frequency = [0 for i in range(6)]

# 6,000,000 die rolls
for roll in range(num_roll):  # note underscore separators
    # random value in range 1 to 6 (face of the die)
    face = random.randrange(1, 7)
    # increment appropriate face counter
    frequency[face - 1] += 1

# output: displaying frequency for each face
print(f'Face{"Frequency":>13}')
for i, j in enumerate(frequency):
    print(f'{i + 1:>4}{j:>13}')
