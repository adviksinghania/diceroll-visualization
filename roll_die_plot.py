# !/bin/python3
# roll_die_plot.py
"""Graphing frequencies of die rolls with Seaborn."""

import random
import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print('Usage:   python3 RollDie.py <number of times to roll the die>')
    print('Example: python3 RollDie.py 600')
    sys.exit()

# sys.argv[1] represents number of times to roll the die
num = int(sys.argv[1])
# rolling die num number of times and storing in a list
dice_rolls = [random.randrange(1, 7) for _ in range(num)]
# NumPy unique function returns unique faces and frequency of each face of the die
values, frequencies = np.unique(dice_rolls, return_counts=True)

title = f'Rolling a six sided die {num:,} Times.'
sns.set_style('whitegrid')  # setting a backgroud style for the graph
axes = sns.barplot(x=values, y=frequencies, palette='bright')  # creating a bar plot
axes.set_title(title)  # setting the titles of the graph window
# labelling the x and y axes of the graph
axes.set(xlabel='Die Value', ylabel='Frequency')
# setting the maximum value represented by the y axis
# scale y-axis by 10% to make room for text above bars
axes.set_ylim(top=max(frequencies) * 1.10)

# display frequency & percentage above each patch (bar)
# patches attribute contains two-dimensional colored shapes that represent the plot’s bars
for bar, frequency in zip(axes.patches, frequencies):
    # get the x coordinate of the text displayed above the bar
    text_x = bar.get_x() + bar.get_width() / 2.0
    # get the y coordinate of the text displayed above the bar
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / num:.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')

# display graph
plt.show()

# Printing the results on the console
print(f'Face |{"Frequency":>12} |{"Probability":>12}')
for i, j in zip(values, frequencies):
    print(f'{i:>4} |{j:>12} |{j / num:>12.3%}')

sys.exit()
