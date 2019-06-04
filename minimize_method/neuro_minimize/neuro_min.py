import numpy as np
import random as rd

from minimize_method.print_result import print_result

def annealing(func, x0):
    k = 1
    energy = func(x0)
    tStart = 100
    tEnd = 1e-6
    temp = tStart
    
    while temp > tEnd and k <= 500:
        xNew = x0 + 0.5 * np.array([rd.normalvariate(0, 1), rd.normalvariate(0, 1)])
        energyNew = func(xNew)
        deltaEnergy = energyNew - energy
        if deltaEnergy < 0:
            x0 = xNew.copy()
            energy = energyNew
            temp = temp / np.log(1 + k)
            k = k + 1
        else:
            p = np.exp(-deltaEnergy / temp)
            alpha = rd.random()
            if alpha < p:
                x0 = xNew.copy()
                energy = energyNew
                temp = temp / np.log(1 + k)
                k = k + 1
    x_min = xNew
    f_min = energyNew

    print_result(x_min, f_min, k)

    return x_min, f_min, k

def pso(func, d, s):
    n = 100
    xmin = -10
    xmax = 10
    
    funp = np.zeros(s)
    fitness = np.zeros(s)
    x = np.zeros((s, d))
    v = np.zeros((s, d))
    p = np.zeros((s, d))
    
    
    w = 1 / (2 * np.log(2))
    c1 = 0.5 + np.log(2) 
    c2 = 0.5 + np.log(2)
    
    for i in range(0, s):
        for j in range(0, d):
            x[i][j] = rd.uniform(xmin, xmax)
            v[i][j] = rd.uniform(xmin, xmax - x[i][j]) / 2
            p[i][j] = x[i][j]
        fitness[i] = func(x[i])
        funp[i] = fitness[i]
    
    gbest = 0
    for i in range(1, s):
        if funp[i] < funp[gbest]:
            gbest = i
    
    for k in range(0, n):
        for i in range(0, s):
            for j in range(0, d):
                r1 = rd.random()
                r2 = rd.random()
                
                v[i][j] = w * v[i][j] + c1 * r1 * (p[i][j] - x[i][j])
                if (i != gbest): 
                    v[i][j] = v[i][j] + c2 * r2 * (p[gbest][j] - x[i][j])
                
                x[i][j] = x[i][j] + v[i][j]
                
                if x[i][j] < xmin:
                    x[i][j] = xmin
                    v[i][j] = 0
                
                if x[i][j] > xmax:
                    x[i][j] = xmax
                    v[i][j] = 0
                    
        for i in range(0, s):
            fitness[i] = func(x[i])
            if fitness[i] < funp[i]:
                funp[i] = fitness[i]
                for j in range(0, d):
                    p[i][j] = x[i][j]
                    
        for i in range(0, s):
            if funp[i] < funp[gbest]:
                gbest = i

    f_best = funp[gbest]
    x_best = p[gbest]
    print_result(x_best, f_best, None)
    return x_best, f_best