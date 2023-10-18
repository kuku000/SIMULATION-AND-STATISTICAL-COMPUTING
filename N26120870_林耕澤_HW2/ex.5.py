import matplotlib.pyplot as plt
import random 
from scipy import integrate
import numpy as np
plt.style.use("seaborn-poster")

def function(x):
    '''欲積分函式樣式:'''
    return np.exp(x + x**2)

def Monte_Carlo(start,end,n):
    '''蒙地卡羅實作:
        start 積分起始點
        end 積分終點
        n 次數
        '''
    total = 0 #總和
    for i in range(n): #給n次積分範圍內隨機值
        x = random.uniform(-2,2) #uniform random var in -2~2
        total += function(x) #將隨機x所得到的output加入total
    return (total/n)*(end - start),(total/n) #回傳用蒙地卡羅方法所得到的積分面積以及高
        
def normal_integral(start,end):
    '''一般積分所得到的值:
        start 積分起始點
        end 積分終點
    '''
    area,err = integrate.quad(function,start, end)
    return area
        

def draw():
    '''製圖'''
    area_mon, height_mon = Monte_Carlo(-2,2,1000000)
    area = normal_integral(-2,2)
    
    x_diff = np.linspace(-2,2,1000)
    y = function(x_diff)
    
    plt.plot(x_diff,[height_mon]*1000,color = 'green',label = 'Monte_Carlo: Area =' + str(area_mon))
    plt.fill_between(x_diff,y1=height_mon,y2=0,where=(x_diff>=-2)&(x_diff<=2),facecolor='green',alpha=0.2)
    plt.plot(x_diff,y,color = 'blue',label = 'e^(x^2+x): Aera =' + str(area))
    plt.fill_between(x_diff,y1=y,y2=0,where=(x_diff>=-2)&(x_diff<=2),facecolor='blue',alpha=0.2)
    plt.legend()
    plt.show() 
       
draw()

area_mon, height_mon = Monte_Carlo(-2,2,10)
print('N = 10  '+str(area_mon))
area_mon, height_mon = Monte_Carlo(-2,2,100)
print('N = 100  '+str(area_mon))
area_mon, height_mon = Monte_Carlo(-2,2,1000)
print('N = 1000  '+str(area_mon))
area_mon, height_mon = Monte_Carlo(-2,2,10000)
print('N = 10000  '+str(area_mon))
area_mon, height_mon = Monte_Carlo(-2,2,100000)
print('N = 100000  '+str(area_mon))
