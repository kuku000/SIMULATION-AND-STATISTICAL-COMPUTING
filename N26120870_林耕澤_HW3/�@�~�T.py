# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 18:54:04 2023

@author: user
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import math
import time
from collections import Counter 
def geo_p_q(p):
    count = 1
    while random.random() > p:
        count += 1
    return count

def geo_r_i_t(p):
    U = random.random()
    i = 1
    count = 1
    baseline = p*(1-p)**(i-1)
    while U >= baseline:
        count += 1
        i += 1
        baseline += p*(1-p)**(i-1)
        
    return count

def geo_formula(p):
    U = random.random()
    X = math.floor(math.log(U) / math.log(1 - p)) + 1
    return X
        
def draw(p, num,pic = True):
   
    t1 = time.time()
    list_pq = []     
    for i in range(num):
        list_pq.append(geo_p_q(p))
    t2 = time.time()
    list_rit = []
    for i in range(num):
        list_rit.append(geo_r_i_t(p))
    t3 = time.time()
    list_formula = []
    for i in range(num):
        list_formula.append(geo_formula(p))
    t4 = time.time()
    
    if pic:
        element_counts_pq = Counter(list_pq)
        sorted_elements_pq = sorted(element_counts_pq.items()) 
        print(sorted_elements_pq)
        elements_pq, counts_pq = zip(*sorted_elements_pq)    
        plt.bar(elements_pq, counts_pq, color = 'r')
        plt.xlabel('random variables')
        plt.ylabel('count')
        plt.title('distribution')
        plt.show()
        
        element_counts_rit = Counter(list_rit)
        sorted_elements_rit = sorted(element_counts_rit.items()) 
        print(sorted_elements_rit)
        elements_rit, counts_rit = zip(*sorted_elements_rit)    
        plt.bar(elements_rit, counts_rit, color = 'g')
        plt.xlabel('random variables')
        plt.ylabel('count')
        plt.title('distribution')
        plt.show()
        
        element_counts_formula = Counter(list_formula)
        sorted_elements_formula = sorted(element_counts_formula.items()) 
        print(sorted_elements_rit)
        elements_formula, counts_formula = zip(*sorted_elements_formula)    
        plt.bar(elements_formula, counts_formula, color = 'b')
        plt.xlabel('random variables')
        plt.ylabel('count')
        plt.title('distribution')
        plt.show()
    else:
        return t1,t2,t3,t4
    
    #list_time = []
    #list_time.append((t2 - t1))
    #list_time.append((t3 - t2))
    #list_time.append((t4 - t3))
    #print(list_time)
   # plt.bar(['pq','R.I.T','formula'],list_time, color = 'y')
    #plt.xlabel('approach')
    #plt.ylabel('time spent')
    #plt.title('time spent')
    #plt.show()


time_pq = []
time_rit = []
time_formula = []    
for p in [0.7,0.5,0.3,0.1,0.05] :
    draw(p, 100)
    t1,t2,t3,t4 = draw(p, 10000, pic = False)
    time_pq.append(t2-t1)
    time_rit.append(t3-t2)
    time_formula.append(t4-t3)
    
plt.plot([0.7,0.5,0.3,0.1,0.05],time_pq, label ='pq')
plt.plot([0.7,0.5,0.3,0.1,0.05], time_rit, label = 'RIT')
plt.plot([0.7,0.5,0.3,0.1,0.05], time_formula, label = 'formula')
plt.xlabel("p")
plt.ylabel("time spent (10000 times)")
plt.legend()
plt.show()     
    






        
    