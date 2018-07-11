a = 1
while a < 20:
    print a,
    a += 2
print("end")


n = 100
iterate = 0
total = 0
while iterate != n:
    iterate += 1
    total += iterate
print(total)


a=5
while a<7:
    if(a%2==0):
        print(a,"is even")
    else:
        print(a,"is odd")
    a+=1


n = 0
ans = []
while n <= 1000:
    if (n % 11 == 0):
        ans.append(n)
        a=max(ans)
    n += 1
print(a)


n=1000
while n>0:
    if(n % 11 ==0):
        print(n)
        break
    n-=1


n=1000
flag = True
while n<=1000:
    if (n % 11 ==0 ) and flag :
        print (n)
        flag = False
    n-=1