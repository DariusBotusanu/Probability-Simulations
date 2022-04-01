# -*- coding: utf-8 -*-
"""
We are moving on a straight line:
    - forward : probability p
    - backward : probability 1-p

We start at the position 0 and want to get to a position j in n stepts.
So S1 = 0 and we want to get Sn = j.
We will simulate this experiment and find the experimental probability P(Sn = j) 
The theoretical probability: 
    - P(Sn = j) = C(n, (n+j)/2)*p^((n+j)/2)*(1-p)^((n-j)/2) if n and j have the same parity
    - 0 otherwise
    where C(n, k) denotes n choose k

@author: Darius
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.special import comb #we import the n choose k function

def straight_line_walk(start, steps, p_forward):
    position = start
    points = [[start, start]]
    for i in range(steps):
        position += np.random.choice([-1, 1], size=None, replace=True, p=[1-p_forward, p_forward])
        points.append([start+i+1, position])
        
    return points

def plot_straight_line_walk(start, steps, p_forward):
    point_list = straight_line_walk(start, steps, p_forward)
    x_list = [point[0] for point in point_list]
    y_list = [point[1] for point in point_list]
    plt.xlim((start, steps))
    plt.ylim((-steps-1, steps+1))
    plt.plot(x_list,y_list, marker = 'o')

def simulate_straight_line_walk(times, start, destination, steps, p_forward):
    successes = 0
    for i in range(times):
        walk = straight_line_walk(start, steps, p_forward)
        if (walk[-1][1]==destination):
            successes += 1
    print("Experimental probability: {}".format(successes/times))
    if (steps%2==destination%2):
        theoretical = comb(steps, (steps+destination)/2)*(p_forward**((steps+destination)/2))*((1-p_forward)**((steps-destination)/2))
        print("Theoretical probability: {}".format(theoretical))
    else:
        print("Theoretical probability: 0")
            

#simulate_straight_line_walk(1000, 0, 8, 10, 2/3)
#simulate_straight_line_walk(1000, 0, 8, 10, 1/2)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
