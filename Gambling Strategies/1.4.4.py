# -*- coding: utf-8 -*-
# A gambler has 300$ and plays roulette with the following
# strategy:
#    he bets 100$ on the red color, which has a 47.4% chance of win;
#    if the red color comes up, he gets his 100$ back and the casino pays him
#     an extra 100$;
#    if the red color does not come up, he does not get his 100$ back.
# He plays with this strategy until: either he has no money left or he doubles
# his initial money.

import numpy as np

def roulette_gambler(budget, N):
    sums = budget*np.ones(N)
    for i in range(N):
        while ((sums[i] > 0) & (sums[i] < budget*2)):
            sums[i] += np.random.choice([-100, 100], size=1, p=[1-0.474, 0.474]) #1-47.4 chance of being black (so lose 100)
    return sums

print("The simulated probability {}".format(np.mean(roulette_gambler(300, 20000) == 600)))
print("The simulated probability {}".format(np.mean(roulette_gambler(300, 40000) == 600)))
print("The simulated probability {}".format(np.mean(roulette_gambler(300, 60000) == 600)))

#Note: the real probability is approx 42.2
#By following all the programs in the Gambling strategies folder one can find the best
#gambling strategy for casinos:
#
#
#
#
#don't gamble your money in casinos
            
            
    
