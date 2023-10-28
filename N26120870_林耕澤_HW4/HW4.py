# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:13:48 2023

@author: KYLE
"""

import numpy as np
import matplotlib.pyplot as plt
import random, math, time
from collections import Counter 
from scipy.stats import poisson

def Method_1(Lambda):
    U = random.random()
    i = 0
    baseline = np.exp(-Lambda) # i == 0
    p = baseline
    while U >= baseline:
        p = Lambda * p / (i + 1)
        i += 1
        baseline += p 
    return i

def Method_2(Lambda):
    i = 0
    total = 0
    while total <= 1:
        U = random.random()
        total += -1 / Lambda * math.log(U)
        i += 1
        
    return i - 1
        
def draw(Lambda, num, pic = True, time_return = True):
    list_method_1 = []
    list_method_2 = []
    
    t1 = time.time()
    for i in range(num):
        list_method_1.append(Method_1(Lambda))
    t2 = time.time()
    for i in range(num):
        list_method_2.append(Method_2(Lambda))
    t3 = time.time()
    print('Method 1 time cost per 100000: ', t2 - t1)
    print('Method 2 time cost per 100000: ', t3 - t2)
    print("-----------------------------------------")
    if pic:
        element_counts_method_1 = Counter(list_method_1)
        sorted_elements_method_1 = sorted(element_counts_method_1.items()) 
        elements_method_1, counts_method_1 = zip(*sorted_elements_method_1) 
        #如果要計算機率分布就不要註解掉,註解掉變成計算次數
        #counts_method_1 = [i / num for i in counts_method_1]
        
        plt.bar(elements_method_1, counts_method_1, color = 'r', alpha = 0.4, label = 'Method 1: ' + str(sum(list_method_1)/num))
        #plt.xlabel('random variables')
        #plt.ylabel('probs')
        #plt.title('distribution')
        
        element_counts_method_2 = Counter(list_method_2)
        sorted_elements_method_2 = sorted(element_counts_method_2.items()) 
        elements_method_2, counts_method_2 = zip(*sorted_elements_method_2)
        #如果要計算機率分布就不要註解掉,註解掉變成計算次數
        #counts_method_2 = [i / num for i in counts_method_2]
        
        plt.bar(elements_method_2, counts_method_2, color = 'g', alpha = 0.4, label = 'Method 2: '+ str(sum(list_method_2)/num))
        plt.xlabel('random variables')
        plt.ylabel('probs')
        plt.title('Lambda = '+ str(Lambda) +' distribution')
        #plt.legend()
        #plt.show()
        
        #poisson prods distribution(PMF)
        pmf = poisson.pmf(np.arange(0, max(elements_method_1)), Lambda)
        plt.plot(np.arange(0, max(elements_method_1)), pmf)
        plt.title('Lambda = '+ str(Lambda) +' distribution')
        plt.show()
        
    if time_return:
        return t2 - t1, t3 - t2
    
    
    

def main():   
    M1TL = []
    M2TL = []
    for i in [0.5, 1, 3, 5, 7, 9]:        
        M1t, M2t = draw(i, 10000)
        M1TL.append(M1t)
        M2TL.append(M2t)
    
    plt.plot([0.5, 1, 3, 5, 7, 9], M1TL, label = "Method 1")
    plt.plot([0.5, 1, 3, 5, 7, 9], M2TL, label = "Method 2")
    plt.xlabel('Lambda')
    plt.ylabel('time(s) cost per 10000')
    plt.title("time cost")
    plt.legend()
    plt.show()
    
main()    


    
    