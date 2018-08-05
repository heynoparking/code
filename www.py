
def Queens (Q):
    x = []
    for i in Q:
        x +=i
    
    print (x)
    
    new_x = []
    for i in range(0,len(x),2):
        new_x.append(x[i])
    

    new_x2 = []
    for i in range (1,len(x),2):
        new_x2.append(x[i])

    add = [a+b for a,b in zip(new_x,new_x2)]
    less = [a+b for a,b in zip(new_x,new_x2)]

    if len(set(new_x)) != 8:
        print ("False")

    elif len(set(new_x2)) !=8:
        print("False")
    elif(len(set(add)))!=8:
        print ("False")
    elif(len(set(less)))!=8:
        print("False")
    else:
        print("True")

Queens(([1,2],[3,4],[5,6],[7,8],[8,7],[6,5],[4,3],[2,1]))