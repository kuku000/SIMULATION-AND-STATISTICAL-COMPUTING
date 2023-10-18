import matplotlib.pyplot as plt
import random 
import numpy as np
plt.style.use("seaborn-poster")

def sum_to_exceed_1(time):
    '''time 次數'''
    N_list = [] #儲存每次需要的N次數
    for i in range(time):
        total = 0
        N = 0
        while(total <=1):#當total超過1則停止
            total += random.uniform(0, 1) #uniform random var in 0~1
            N+=1
        N_list.append(N)
    expect_value = sum(N_list)/time #期望值計算
    return expect_value


        

def draw():
    '''製圖'''
    x_diff = range(100,100000,100)
    y = []
    for i in x_diff:
        y.append(sum_to_exceed_1(i))
    plt.plot(x_diff,y,label = 'E[N] by generating 100 to 100000 values of N')    
    plt.legend()
    plt.show()
    print('E[N] by generating 100000 values of N: '+str(y[-1]))
    
    
print(sum_to_exceed_1(100))
print(sum_to_exceed_1(1000))
print(sum_to_exceed_1(10000))
print(sum_to_exceed_1(100000))
draw()