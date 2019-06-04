import numpy as np

from minimize_method.print_result import print_result

def gold(func, bounds, eps = 1e-4):
    a, b = bounds
    k = 0
    y = a + ((3 - np.sqrt(5)) / 2) * (b - a)
    z = a + b - y
        
    while (np.fabs(a - b) >= eps) and k <= 500:
        if func(y) <= func(z):
            b = z
            z = y
            y = a + b - y
        else:
            a = y
            y = z
            z = a + b - z
        k = k + 1
    xx = (a + b) / 2

    print_result(xx, func(xx), k)
    return (xx, func(xx), k)

def dyhotomy(func, bounds, eps=1e-4, d=1e-5):
    a, b = bounds
    k = 0
    y = (a + b - d) / 2
    z = (a + b + d) / 2
    
    while np.fabs(b - a) >= eps and k <= 500:
        if func(y) <= func(z):
            b = z
        else:
            a = y
        y = (a + b - d) / 2
        z = (a + b + d) / 2
        k = k + 1
        xx = (a + b) / 2

    print_result(xx, func(xx), k)
    return xx, func(xx), k

def approximation(func, x1, h = 0.01, eps = 1e-4):
    k = 0
    x2 = x1 + h

    
    if func(x1) > func(x2):
        x3 = x1 + 2*h
    else:
        x3 = x1 - h
            
    fx1, fx2, fx3 = func(x1), func(x2), func(x3)
    fmin, xmin = myMin(func, x1, x2, x3)

#     xx = 1/2*(x1 - x2) + ( (1/2) * (fx1 - fx2) * (x2 - x3) * (x3 - x1) ) / ( (x3 - x1)*fx2 + (x2 - x3)*fx1 + (x1 - x2)*fx3 )
    
    a1 = (fx2 - fx1) / (x2 - x1)
    a2 = 1.0 / (x3 - x2) * ((fx3 - fx1) / (x3 - x1) - (fx2 - fx1) / (x2 - x1));
    xx = (x1 + x2)/2 - a1 / (2*a2)
    fxx = func(xx)
    
    while np.fabs(xx - xmin) >= eps and k <= 500:
        if func(x1) > func(x2):
            x3 = x1 + 2*h
        else:
            x3 = x1 - h
            
        fx1, fx2, fx3 = func(x1), func(x2), func(x3)
        fmin, xmin = myMin(func, x1, x2, x3)

        a1 = (fx2 - fx1) / (x2 - x1)
        a2 = 1.0 / (x3 - x2) * ((fx3 - fx1) / (x3 - x1) - (fx2 - fx1) / (x2 - x1));
        xx = (x1 + x2)/2 - a1 / (2*a2)
        fxx = func(xx)
        
        if fxx < fmin:
            x1 = xx
        else:
            x1 = xmin
        k = k + 1
        # print(x1, x2, x3, xmin, xx, k)
#         print(xx - xmin, xx, xmin)
    print_result(x1, func(x1), k)  
    return x1, func(x1), k

def myMin(func, x1, x2, x3):
    fx1, fx2, fx3 = func(x1), func(x2), func(x3)
    fmin = fx1
    xmin = x1
    if fx2 < fmin:
        fmin = fx2
        xmin = x2
    if fx3 < fmin:
        fmin = fx3
        xmin = x3
        if fx2 < fx3:
            fmin = fx2
            xmin = x2
    return (fmin, xmin)