# -*- coding: utf-8 -*-
"""
Mrs. Y and Mr. X take their dogs for a walk every day in
a pocket park. Mrs. Y arrives in the park at 12 and T minutes and walks
her dog for 15 minutes. Mr. X arrives in the park at 13 and S minutes
and walks his dog for 10 minutes. Suppose that T and S are independent
uniformly distributed random variables on the intervals [30, 50], respectively
[−20, 10].

What we will do:
    -   compute by simulations the probability that Mrs. Y and Mr. X
        meet in the park when they walk their dogs.

Note: the theoretical probability is 0.5
        
Source: Hannelore Lisei, Wilfried Grecksch, Mihai Iancu - Probability: Theory, Examples, Problems, Simulations       

@author: Darius
"""
import numpy as np

def walk_dogs(simulations_num):
    #random.uniform(low=0.0, high=1.0, size=None)
    count = 0 #represents the number of time they have met
    for i in range(simulations_num):
        Y = np.random.randint(low=30, high=51, size=None)
        X = 60 + np.random.randint(low=-20, high=11, size=None)
        
        #note that they meet if and only if T < 60 + S < T +15 or 60+S < T < 70+S 
        if max(X+10, Y+15) - min(X,Y) < 25:
            count += 1
            
    simulated_prob = count/simulations_num
    print("Simulated probability {}\nTheoretical probability 0.5\nError {}".format(simulated_prob, abs(simulated_prob-0.5)))
    
walk_dogs(10000)
