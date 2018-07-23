"""
 dice_sim.py
 probabilities of a dice roll using simulation
"""

import random
import numpy as np


def main():
    """
    main function
    """
    dice1 = (1, 2, 3, 4, 5, 6)
    freq = [0, 0, 0, 0, 0, 0]
    trials = 1000
    ctr = 1
    while ctr < trials:
        roll_dice = random.choice(dice1)
        freq[roll_dice - 1] += 1
        ctr += 1

    print("Probabilities:")
    print(np.array(freq) / trials)

if __name__ == "__main__":
    main()
    