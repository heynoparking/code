def f(n):
    print('n:',n) # Trace recursive levels
    if n==1:
        return 1 
    else:
        return f(n-1)+n

print('answer: ',f(10))