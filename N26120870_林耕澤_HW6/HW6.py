import numpy as np
import random
import matplotlib.pyplot as plt

#---------------------HW6-1------------------------------------

def exp_rv_generator(Lambda):
    U = random.random()
    X = - np.log(U) / Lambda
    return X



def MM1_model_fixed_time_interval(mean_service_rate, mean_arrivel_rate, end_time):
    '''固定時間區間'''
    arrival_time = []
    service_time = []
    waiting_time = []
    departure_time = []
    T = end_time

    i = 0
    arrt = exp_rv_generator(mean_arrivel_rate)
    if arrt > T:
        return arrival_time, service_time, waiting_time, departure_time, 0
    arrival_time.append(arrt)
    waiting_time.append(0)
    service_time.append(exp_rv_generator(mean_service_rate))
    departure_time.append(service_time[0] + waiting_time[0] + arrival_time[0])
    i += 1
    while arrival_time[i - 1] < T:
        arrt = exp_rv_generator(mean_arrivel_rate)
        if arrt + arrival_time[i - 1] >= T:
            return arrival_time, service_time, waiting_time, departure_time, i + 1
        arrival_time.append(arrt + arrival_time[i - 1])

        if departure_time[i - 1] - arrival_time[i] > 0:
            waiting_time.append(departure_time[i - 1] - arrival_time[i])
        else:
            waiting_time.append(0)
        service_time.append(exp_rv_generator(mean_service_rate))
        departure_time.append(arrival_time[i] + service_time[i] + waiting_time[i])
        i += 1

def MM1_model_fixed_number_of_cumstors(mean_service_rate, mean_arrivel_rate, num):
    '''固定來可客人數'''
    arrival_time = []
    service_time = []
    waiting_time = []
    departure_time = []

    arrival_time.append( exp_rv_generator(mean_arrivel_rate))
    service_time.append( exp_rv_generator(mean_service_rate))
    waiting_time.append(0)
    departure_time.append(arrival_time[0] + service_time[0])
    for i in range(1, num):
        arrival_time.append( arrival_time[i - 1] + exp_rv_generator(mean_arrivel_rate))
        service_time.append( exp_rv_generator(mean_service_rate))

    for i in range(1, num):
        wait_temp = (arrival_time[i - 1] + service_time[i - 1] + waiting_time[i - 1]) - arrival_time[i]
        if wait_temp >= 0:
            waiting_time.append(wait_temp)
        else:
            waiting_time.append(0)
            
        departure_time.append(arrival_time[i] + service_time[i] + waiting_time[i])

    return arrival_time, service_time, waiting_time, departure_time


arrival_time, service_time, waiting_time, departure_time, i = MM1_model_fixed_time_interval(10,5,100)
arrival_time2, service_time2, waiting_time2, departure_time2, i2 = MM1_model_fixed_time_interval(10,10,100)
arrival_time3, service_time3, waiting_time3, departure_time3, i3 = MM1_model_fixed_time_interval(10,20,100)

#service rate > arrival rate
plt.plot(waiting_time, label ="utilization"+ str(np.sum(service_time)/departure_time[-1]))
plt.legend()
plt.xlabel('cumster #')
plt.ylabel('waiting time')
plt.title('service_rate = 10, arrival_rate = 5, T = 100')
plt.show()
print(np.sum(service_time)/departure_time[-1], i)

#service rate = arrival rate
plt.plot(waiting_time2, label ="utilization"+ str(np.sum(service_time2)/departure_time2[-1]))
plt.legend()
plt.xlabel('cumster #')
plt.ylabel('waiting time')
plt.title('service_rate = 10, arrival_rate = 10, T = 100')
plt.show()
print(np.sum(service_time2)/departure_time2[-1], i2)

#service rate < arrival rate
plt.plot(waiting_time3, label ="utilization"+ str(np.sum(service_time3)/departure_time3[-1]))
plt.legend()
plt.xlabel('cumster #')
plt.ylabel('waiting time')
plt.title('service_rate = 10, arrival_rate = 20, T = 100')
plt.show()
print(np.sum(service_time3)/departure_time3[-1], i3)


#---------------------------HW6-2----------------------------confidence interval

# try to get the avg waitin time

def CI_95(waiting_time):
    '''95信賴區間計算及平均值'''
    waiting_time = np.array(waiting_time)
    mean = np.mean(waiting_time)
    std = np.std(waiting_time)
    r = 1.96 * std/(len(waiting_time)**(1/2))
    return mean, r


def draw(num):
    '''製圖'''
    mean_1 = []
    mean_2 = []
    mean_3 = []
    
    listci_1 = []
    listci_2 = []
    listci_3 = []
    
    lam_L = np.arange(1, 21, 0.01)
    
    for lam in lam_L:
        temp_list1 = []
        temp_list2 = []
        temp_list3 = []
        for i in range(num):
            arrival_time, service_time, waiting_time, departure_time, _i = MM1_model_fixed_time_interval(5, lam, 10)
            arrival_time2, service_time2, waiting_time2, departure_time2, _i2 = MM1_model_fixed_time_interval(10, lam, 10)
            arrival_time3, service_time3, waiting_time3, departure_time3, _i3 = MM1_model_fixed_time_interval(15, lam, 10)
            
            temp_list1.append(np.sum(waiting_time) / _i)
            temp_list2.append(np.sum(waiting_time2) / _i2)
            temp_list3.append(np.sum(waiting_time3) / _i3)

        # service rate= 5
        mean1, r1 = CI_95(temp_list1)
        mean_1.append(mean1)
        listci_1.append(r1)

        # service rate= 10
        mean2, r2 = CI_95(temp_list2)
        mean_2.append(mean2)
        listci_2.append(r2)

        # service rate= 20
        mean3, r3 = CI_95(temp_list3)
        mean_3.append(mean3)
        listci_3.append(r3)
    
    color = ['r', 'g', 'b']
    plt.plot(lam_L, mean_1, label="service rate = 5", color=color[0])
    plt.fill_between(lam_L, np.subtract(mean_1, listci_1), np.add(mean_1, listci_1), color=color[0], alpha=0.5)

    plt.plot(lam_L, mean_2, label="service rate = 10", color=color[1])
    plt.fill_between(lam_L, np.subtract(mean_2, listci_2), np.add(mean_2, listci_2), color=color[1], alpha=0.5)

    plt.plot(lam_L, mean_3, label="service rate = 15", color=color[2])
    plt.fill_between(lam_L, np.subtract(mean_3, listci_3), np.add(mean_3, listci_3), color=color[2], alpha=0.5)

    plt.xlabel('lambda')
    plt.ylabel('waiting time')
    plt.title('n = '+str(num))
    plt.legend()
    plt.show()

draw(5)
draw(10)
draw(100)     
        
        
        
        
        
        
        
        
        
    




















