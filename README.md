

# Dice-Roll-Visualization

Using [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) to graph the probabilities of the faces of a die in a specified number of rolls.

## About

**Law of Large Numbers:** In probability theory, the law of large numbers (LLN) is a theorem that describes the result of performing the same experiment a large number of times. According to the law, the average of the results obtained from a large number of trials should be close to the expected value and will tend to become closer to the expected value as more trials are performed.<br>

We use a fair dice as an example to demonstrate this law. All the faces of the die are equally likely to occur but initially, when the number of die rolls is small, the frequencies of the faces is uneven and the probability may be more for one face than others.
When we roll the die for a large number of times, we see that the result indeed approaches the expected value 1/6 (= 0.166666) or 16.667%.

### Initial script

We create a script that rolls a die (generates a random number between 1 to 6), a specific number of times, e.g. 1000, 5000 then the frequency of each face should be 1000/6 or 5000/6 respectively.
Let's take 6,000,000 for simplicity. Then the frequency for each face should be 1,000,000.<br>

```python
# !/bin/python3
# roll_die.py
"""Roll a six-sided die 6,000,000 times."""

import random

# number of die rolls
num_roll = 100
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

```
Running the above script would display an output like:
```bash
$ python3 roll_die.py                                              
Face    Frequency
   1           15
   2           10
   3           16
   4           22
   5           13
   6           24
```
Here, the probability is maximum for the face '6'  (24%) and minimum for the face '2' (10%). Which is not true because all the face of the die are equally likely to be the outcome.

If the same script were to run by changing the value of `num_roll` from 100 to 6,000,000; the output would be:
```bash
$ python3 roll_die.py          
Face    Frequency
   1      1000104
   2       999846
   3      1000645
   4       999434
   5      1001315
   6       998656
```
We can see that the frequency for each face is almost equal to 1,000,000 and therefore the probability for each face is almost 16.67%. Depending upon your system, this script would take time to execute since we are generating random numbers, 6 million times.
Now, we'll create a script to visualize the distribution using matplotlib and seaborn.

## Setup

-   Install venv for Python3 by running `sudo apt-get install python3-venv` in your Linux terminal.
-   Clone this repository locally, using `git clone https://github.com/adviksinghania/diceroll-visualization.git`
-   Navigate inside the directory using `cd diceroll-visualization`
-   Run `python3 -m venv ./env` to create a virtual environment in the current directory.
-   Run `pip install -r requirements.txt` to install the dependencies. or just `pip install matplotlib seaborn` to install matplotlib and seaborn.

### Static visualization

Now, run the `roll_die_plot.py` in your Linux terminal to create a static graph of the frequency distribution.
Example 1:
```bash
$ python roll_die_plot.py 100
```
![Figure 1](https://github.com/adviksinghania/diceroll-visualization/raw/main/Figure_1.png)
```bash
Face |   Frequency | Probability
   1 |          14 |     14.000%
   2 |          19 |     19.000%
   3 |          14 |     14.000%
   4 |          25 |     25.000%
   5 |          16 |     16.000%
   6 |          12 |     12.000%

```
<br>
Example 2:
```bash
$ python roll_die_plot.py 6000000
```
![Figure 2](https://github.com/adviksinghania/diceroll-visualization/raw/main/Figure_2.png)
```bash
Face |   Frequency | Probability
   1 |      999521 |     16.659%
   2 |      999198 |     16.653%
   3 |      998664 |     16.644%
   4 |     1002321 |     16.705%
   5 |      999494 |     16.658%
   6 |     1000802 |     16.680%

```
<br>
