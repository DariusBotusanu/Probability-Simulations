'''
The problem:
    In an urn we have ai balls of color ci, i=1,...,m
    We draw a ball, note its color and do not put it back. We do this n times
    Find the probability that the ball with color ci to appear ki times, i=1,...,m

Note that the theoretical probability is:
    product(C(ai,ki), i from 1 to m)/C(a1+...+am, k1+...+km)

We will simulate the extarction of balls
That means we will have a vector v_wanted having on ith entry the number of balls we wanted to extract for
the color ci, and another vector v_actual with the actual number of balls we subtracted
Their difference in norm will tell us how far they are from one another
So the probability is the proportion: 1-||difference||/||v_wanted||

CURRENTLY WORKING ON IMPROVEMENT
'''
import numpy as np
from scipy.special import comb #we import the n choose k fucntion

def sampling_no_replacement(n, balls):
    '''
    m denotes the number of states
    n denotes the number of balls we extract (without replacing them)
    balls is an array which has on position i the number of balls of colour i
    k is an
    '''
    m = len(balls)
    extracted_balls = np.zeros((m,), dtype=int) #is an array representing the number of balls we drew for each color
    for count in range(n):
        repeat = True
        while(repeat):
            i = np.random.randint(low=0, high=m)
            if(balls[i] != 0):
                balls[i] -= 1
                extracted_balls[i] += 1
                repeat = False
    return extracted_balls

def prob_sampling_no_replacement(balls, wanted_numbers):
    
    denominator = comb(np.sum(balls), np.sum(wanted_numbers))
    nominator = 1
    for i in range(len(wanted_numbers)):
        nominator *= comb(balls[i], wanted_numbers[i])
    return nominator/denominator
        
    

def simualte_sampling_no_replacement(num_of_times):
    for j in range(num_of_times):
        m = np.random.randint(low=10, high=100)
        balls = np.zeros((m,),dtype=int)
        v_wanted = np.zeros((m,),dtype=int)
        total = 0;
        extractions = 0;
        for i in range(m):
            balls[i] = np.random.randint(low=1, high=10)
            total += balls[i]
            v_wanted[i] = np.random.randint(low=0, high=balls[i]+1)
            extractions += v_wanted[i]
        
        #theoretical_prob = prob_sampling_no_replacement(balls, v_wanted)
        extracted_balls = sampling_no_replacement(extractions, np.copy(balls))

        difference_vector = np.subtract(v_wanted, extracted_balls)
        diff_norm = np.linalg.norm(difference_vector)
        wanted_norm = np.linalg.norm(v_wanted)
        computed_prob = 1-diff_norm/wanted_norm
        print("p = {}".format(computed_prob))

simualte_sampling_no_replacement(10)
        
    