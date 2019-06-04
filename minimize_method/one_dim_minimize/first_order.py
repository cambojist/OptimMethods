import numpy as np

from minimize_method.print_result import print_result

def min_midlle_point(func, dfunc, bounds, tol_x = 1e-4):    
    a, b = bounds
    k = 0
    
    x = (a + b) / 2.0
    dfx = func(x)
    
    while np.abs(dfunc(x)) > tol_x and k < 500:
        if dfunc(x) > 0:
            b = x
        else:
            a = x
        k = k + 1
        
        x = (a + b) / 2.0
        dfx = func(x)
    print_result(x, dfx, k)
    return x, dfx, k

def horde(func, dfunc, bounds, tol_x = 1e-4):    
    a, b = bounds
    k = 0
    
    x = a - dfunc(a) / (dfunc(a) - dfunc(b) + 1e-8) * (a - b)
    dfx = func(x)
    
    while np.abs(dfunc(x)) >= tol_x and k < 500:
        if (dfunc(x) > 0):
            b = x
        else:
            a = x
            
        x = a - dfunc(a) / (dfunc(a) - dfunc(b)) * (a - b)
        dfx = func(x)
        
        k = k + 1 
    print_result(x, dfx, k)
    return x, dfx, k