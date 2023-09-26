# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:48:03 2023

@author: user
"""
from functools import cache
import matplotlib.pyplot as plt
import random 
import time
plt.style.use("seaborn-poster")



@cache
def roll_dices(times):
    """ simulate rolling the dice 
    and return probability list of simulation  """
    count_list = [0,0,0,0,0,0]
    for i in range(times):
        x = random.choice([1,2,3,4,5,6])#dice points 1 to 6
        count_list[x-1]+=1#counting how many times we get the point
    
    prob_list = [] # to store prob
    for j in range(len(count_list)):
        prob_list.append(count_list[j]/times)#probability counting
        
    return prob_list

@cache
def draw_dice_prob(time_start,time_end,interval):
    """"draw picture"""
    prob1 = []
    prob2 = []
    prob3 = []
    prob4 = []
    prob5 = []
    prob6 = []
    theor_prob = []
          
    for i in range(time_start,time_end,interval):
        prob = roll_dices(i)
    
        prob1.append(prob[0])
        prob2.append(prob[1])
        prob3.append(prob[2])
        prob4.append(prob[3])
        prob5.append(prob[4])
        prob6.append(prob[5])
        theor_prob.append(1/6)

    x_diff = range(time_start,time_end,interval)

    plt.figure(figsize = (12, 8))
    plt.plot(x_diff,prob1,label = 'one')
    plt.plot(x_diff,prob2,label = 'two')
    plt.plot(x_diff,prob3,label = 'three')
    plt.plot(x_diff,prob4,label = 'four')
    plt.plot(x_diff,prob5,label = 'five')
    plt.plot(x_diff,prob6,label = 'six')
    plt.plot(x_diff,theor_prob,linewidth = 8,label = 'theoretical probability')
    plt.xlabel("number of times")
    plt.ylabel("probability")
    plt.legend()
    plt.show()  
        
start = time.process_time() 
      
draw_dice_prob(6, 1000, 1)

end = time.process_time()
print(str(end - start) + "s")         
        
        
    
        
       

    
    