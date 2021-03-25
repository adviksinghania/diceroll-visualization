# !/bin/python3
# roll_die_dynamic.py
"""Dynamically graphing frequencies of die rolls."""

import sys
import random
import time
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn as sns


def update(frame_number, rolls, faces, frequencies):
    """Configure bar plot contents for each animation frame."""
    # Though FuncAnimation requires the update function
    # to have frame_number parameter, we do not use it
    # roll die and update frequencies
    for _ in range(rolls):
        frequencies[random.randrange(1, 7) - 1] += 1

    # reconfigure plot for updated die frequencies
    plt.cla()  # clear old contents contents of current Figure
    axes = sns.barplot(x=faces, y=frequencies, palette='bright')  # new bars
    axes.set_title(f'Die Frequencies for {sum(frequencies):,} Rolls')
    axes.set(xlabel='Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10)  # scale y-axis by 10%

    # display frequency & percentage above each patch (bar)
    # patches attribute contains two-dimensional colored shapes that represent the plot’s bars
    for bar, frequency in zip(axes.patches, frequencies):
        # get the x coordinate of the text displayed above the bar
        text_x = bar.get_x() + bar.get_width() / 2.0
        # get the y coordinate of the text displayed above the bar
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage:   python3 RollDie.py <number of frames> <rolls per frame>')
        print('Example: python3 RollDie.py 6000 2')
        sys.exit(0)

    # read command-line arguments for number of frames and rolls per frame
    number_of_frames = int(sys.argv[1])
    rolls_per_frame = int(sys.argv[2])

    start = time.time()
    sns.set_style('whitegrid')  # white background with gray grid lines
    figure = plt.figure('Rolling a Six-Sided Die')  # Figure for animation
    values = list(range(1, 7))  # die faces for display on x-axis
    frequencies = [0] * 6  # six-element list of die frequencies

    # configure and start animation that calls function update
    die_animation = animation.FuncAnimation(
        figure, update, repeat=False, frames=number_of_frames, interval=30,
        fargs=(rolls_per_frame, values, frequencies))

    plt.show()  # display window
    stop = time.time()

    print('Success. Took', round(stop - start, 3), 'seconds.')
    sys.exit(0)
