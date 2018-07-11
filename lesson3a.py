def f (x):
    for i in range (1,x+1):
        for j in range (1,x+1):
            print i,"*",j,"=",i*j,"\t", 
        print"\n"
    return   i , j
    
y= f(9)




def f(x,y):
    a , b = y , x
    return a,b

a , b = 1 , 2
print f(a,b)




def f(x,y):
    if x>y:
        return "a>b"
    elif x<y:
        return "a<b"
    else:
        return "a=b"

a , b = 7 , 2
print f(a,b)




