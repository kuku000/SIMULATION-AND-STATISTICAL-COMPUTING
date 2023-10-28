# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:03:37 2023

@author: KYLE
"""

import numpy as np
import matplotlib.pyplot as plt
import random, math, time
from collections import Counter 

def expRV_generator(rate):
    U = random.random()
    X = - math.log(U) / rate
    return X

def normalRV_generator(mean, std, real = False):
    commit = False
    while commit == False:
        Y = expRV_generator(1)
        U = random.random()
        c = (2 * math.exp(1) / math.pi) ** 2
        if U < (2 / math.pi) ** 2 * math.exp(Y - (Y ** 2 / 2)) / c:
            commit = True
            
    Y = random.choice([Y, -Y])
    Y = std * Y + mean
    
    if real:
        if Y > 100:
            Y = 100
        elif Y < 0:
            Y = 0
    return Y
    
def simulation(num):
    std_normal_list = []
    normal_list = []
    in_1std = 0
    in_2std = 0
    in_3std = 0
    
    #generate num times RV
    for i in range(num):
        std_normal_list.append(normalRV_generator(0, 1))
        normal_list.append(normalRV_generator(70, 5, True))
    
    #draw std normal distrubution
    plt.hist(std_normal_list, 100, label = " mean = " + 
             str(round(np.mean(std_normal_list), 4)) + "\n" + " std = " + 
             str(round(np.std(std_normal_list), 4)))
    plt.legend()
    plt.xlabel('random variables')
    plt.ylabel('count')
    plt.title('normal distribution with mean = 0 and std = 1')
    plt.show()
    
    #count mean and std
    mean = round(np.mean(normal_list), 4)
    std = round(np.std(normal_list), 4)
    
    #counting how many score within 1std 2std 3std
    for score in normal_list:
        if (mean - 3*std) <= score <= (mean + 3*std):
            in_3std+=1
            if (mean - 2*std) <= score <= (mean + 2*std):
                in_2std+=1
                if (mean - std) <= score <= (mean + std):
                    in_1std+=1
        
    #draw scores distribution
    plt.hist(normal_list, 100, label = " mean = " + 
             str(mean) + "\n" + " std = " + 
             str(std))
    
    #draw 1std 2std 3std line
    plt.axvline(x = mean + std, color = 'r')
    plt.axvline(x = mean - std, color = 'r', label = "1 std")
    plt.axvline(x = mean + 2 * std, color = 'g')
    plt.axvline(x = mean - 2 * std, color = 'g', label = "2 std")
    plt.axvline(x = mean + 3 * std, color = 'y')
    plt.axvline(x = mean - 3 * std, color = 'y', label = "3 std")
    plt.legend()
    plt.xlabel('scores')
    plt.ylabel('count')
    plt.title('normal distribution with mean = 70 and std = 5')
    plt.show()
    
    # draw reality v.s. empirical rule
    std_dis = [in_1std / num, in_2std / num, in_3std / num]
    plt.bar([0,1,2], std_dis, tick_label = ["in 1std", "in 2std", "in 3std"])
    plt.text(0, round(in_1std / num, 4) / 2, round(in_1std / num, 4) * 100)
    plt.text(1, round(in_2std / num, 4) / 2, round(in_2std / num, 4) * 100)
    plt.text(2, round(in_3std / num, 4) / 2, round(in_3std / num, 4) * 100)
    plt.axhline(y = 0.68, color = 'r', label = "68")
    plt.axhline(y = 0.95, color = 'g', label = "95")
    plt.axhline(y = 0.997, color = 'y', label = "99.7")
    plt.xlabel('Within how many standard deviationsstd')
    plt.ylabel('percentage')
    plt.title('simulation v.s. empirical rule')
    plt.legend()
    plt.show()
    return std_normal_list, normal_list
    
    
    
simulation(10000)    
    
    
    
    
        