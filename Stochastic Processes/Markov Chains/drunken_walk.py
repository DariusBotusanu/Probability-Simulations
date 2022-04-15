# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:23:41 2022

An example I thought of that combines Markov chains with random walks (I do not claim originality as
the walk of drunk men seem to fascinate people studying random walks and Brownian motion)

A man has had one too many beers at his local pub and now he has to walk back home.
Luckily for him, his home is down the road so all he has to do is keep a straight line, a deed which
many times proves too ambitious for a lad that's been drinking.
Self-conscious as he is from previous experiences he has the solution to get back home:
-He will walk in front either a bit to the right, or a bit to the left by the following rule:
    -at first he is more likely to go to his right (he is a right handed fella)
    -if he has just walked to the right, next he will be more likely to walk to hsi left
    -similarily, if he has walked to the left, the next step is more likely to be to his right

We will simualte his walk home and impose the following:
    -if he gets too far he faints and the walk stops
    -if he is in a certain radius either to the left or to the right of his house, his helpful wife
    (whom he fears at the moment given the circumstances) will see him and come pick him up, so his walk will stop

Note:
    -we will consider the xOy plane and a walk to the right will be a walk that decreases y
    -a walk to the left will be a walk which increases y


@author: Darius
"""
import numpy as np
from matplotlib import pyplot as plt
#We assume the pub is at position (0,0) and his hime at position (home, 0) so we will see how well his strategy 
#behaves on a longer walk
#also, the likelihood P(Xn+1 = right\Xn = left) = P(Xn+1 = left\Xn = right) = p
#we do this in order to play around with the likelihood he walks around a straight line
#r is the radius of vision of his wife to the right and to the left of his home
def drunken_walk(home, conditional_prob, steps_limit, r):
    walk = [[0,0]] #the points crossed while walking
    last = -1 #represents last step: -1 --> right, 1-left
    position = [0,0] #initial position (the pub)
    got_home=0
    for i in range(steps_limit):
        position[0]+=1
        if(last==1):
            last = np.random.choice([-1, 1], size=None, replace=True, p=[conditional_prob, 1-conditional_prob])
            position[1]+=last
        else:
            last = np.random.choice([-1, 1], size=None, replace=True, p=[1-conditional_prob, conditional_prob])
            position[1]+=last
            
        walk.append(position)
        
        if((position[0] == home) and (abs(position[1]) <= r)):
           #his wife sees him  or he actually gets home
           #also based on past experiences he can assume he won't be having similar walks in the near future
           got_home=1
           break
       
        if(position[0] == steps_limit):
            #he's reached his limits, but he did it with dignity
            break
    return [walk, got_home]

def plot_walks(num_of_trials, home, conditional_prob, steps_limit, r):
    home_arrivals = 0;
    for i in range(num_of_trials):
        walk = drunken_walk(home, conditional_prob, steps_limit, r)
        home_arrivals+=walk[1]
        point_list = walk[0]
        x_list = [point[0] for point in point_list]
        y_list = [point[1] for point in point_list]
        plt.xlim((0, steps_limit))
        plt.ylim((-20, 20))
        plt.grid()
        plt.plot(x_list,y_list, marker = 'o')
    print("The simulated probability that he gets home is {}".format(home_arrivals/num_of_trials))
        

plot_walks(100, 100, 0.6, 100+50, 5)
    
    
    
        
        
            
        

