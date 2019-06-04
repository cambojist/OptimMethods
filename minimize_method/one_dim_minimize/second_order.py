from minimize_method.print_result import print_result

def newton(func, dfunc, d2func, bounds, tol_x = 1e-4):
    a, b = bounds
    k = 0
    
    x = (a + b) / 2
    dfx = func(x)
             
    while np.abs(dfunc(x)) > 500:
        x = x - dfunc(x) / (d2func(x) + 1e-8)
        
        k = k + 1
        num_df = num_df + 3  
    res = func(x)
    
    print_result(x, func(dfx), k)
    return x, dfx, k