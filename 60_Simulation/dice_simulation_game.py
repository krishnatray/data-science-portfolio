#################################
# Program:    dice_simulation_game.py
# Author:     Sushil Sharma
# description: simulate a game of rolling two dice
#
# 

import sys
import random
def dice_game(num_trials=100):
    tot_win = 0
    tot_loss = 0
    win_amount  = 25
    loss_amount = 5
    print("Total Number of simulations: ", num_trials )
    print("Simulating two fair dice game...")
    print(f"Rules: Win=sum equal 7 loss_amount: {loss_amount} win_amount:{win_amount}")
    print("Expected value ", ((1/6) * win_amount - (5/6) * loss_amount) )
   
    for i in range(num_trials):
        #print("\b",i,)
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        #print(dice1, dice2)
        if dice1 + dice2 == 7:
            tot_win += 1
        else:
            tot_loss += 1
    proba_winning = tot_win / (tot_win + tot_loss)
    game_result =  (tot_win * win_amount) - (tot_loss * loss_amount)
    print(f"Wins: {tot_win} Losses: {tot_loss} Result Amount: ${game_result}"  )
    print("Probability of winning:", proba_winning)
    return(game_result)   

if __name__ == "__main__":
    trials = 100000
    dice_game(trials)
#
# End: dice_simulation_game.py
#################################