# -*- coding: utf-8 -*-
"""
Credits: Haggstorm O.: Finite Markov chains and algorithms
We will simulate the weather in Goethenburg as a Markov chain.
This simualtion follows the assumption "the best way to predict the weather from tomorrow
is to look at the weather for today".
This is obviously not true but it does show the "memoryless" property which all Markov chains have

We have the following transition matrix:
        | rain  |  sun |
    rain| 0.75 | 0.25 |
     sun| 0.25 | 0.75 |
     
We adopt the convention:
    0 -> rain
    1 -> sun
@author: Darius
"""
import numpy as np

def initiation_function(x):
    #we start on a rainy day
    return 0

def update_function(s,x):
    if(s == 0):
        if(x < 0.75):
            return 0
        if(x>=0.75):
            return 1
    if(s == 1):
        if(x < 0.25):
            return 0
        if(x>=0.25):
            return 1

def simulate_weather(days):
    #first we will generate a number of "days" values uniformly distributed in the [0,1] itnerval
    vals = np.random.default_rng().uniform(low=0.,high=1.0,size=days)
    current=initiation_function(vals[0])
    weather_list = [current]
    for i in range(1,days):
        current = update_function(current,vals[i])
        weather_list.append(current)
    return weather_list

def display_weather(days):
    day = 0;
    weather_list = simulate_weather(days)
    for weather in weather_list:
        day+=1
        print("Day {}: ".format(day), end="")
        
        if(weather == 0):
            print("rainy")
        else:
            print("sunny")

display_weather(30)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

