# -*- coding: utf-8 -*-
"""
input: a vector v of 100 distinct real numbers
    choose randomly a number k from the set {1,2,...,100}
    choose randomly k elements from v without replacement
    in order to form a subvector w of v
output: the maximum of w
"""
import numpy as np

def random_maximum(v):
    k = np.random.randint(1,100)
    return np.max(np.random.choice(v, replace = False, size = k))

def maximum_sim(v, N):
    count = 0;
    max_v = np.max(v)
    for i in range(N):
        if (max_v == random_maximum(v)):
            count += 1
    return count/N

v = np.arange(1,100,1)
sim_p = maximum_sim(v,10000)
print("Simulated probability: {}\nReal probability: {}\nAbsolute error: {}"
      .format(sim_p, 0.505, abs(sim_p-0.505)))

errors = np.zeros(10)
for i in range(10):
    errors[i] = abs(maximum_sim(v,10000)-0.505)
print("Min = {} \nMax = {}".format(np.min(errors), np.max(errors)))
