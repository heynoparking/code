import os
import queue
'''

allfiles = os.listdir('./testdata')
print (allfiles)

p1 = os.path.join('./testdata/', allfiles[10])
print (p1)

p2 = os.path.join('./testdata/', allfiles[9])
print (p2)

if os.path.isdir(p1):
    print ("It's dir")
else:
    print ("It's file")


if os.path.isfile(p2):
    print ("It's file")
else:
    print ("It's not file")

'''


count = 0
queue = queue.Queue()
queue.put('./testdata/')


while not queue.empty():
    top = queue.get()
    

    allfiles = os.listdir(top)
    num = len(allfiles)
    
    
    for i in range(num):
        p1=os.path.join('./testdata/', allfiles[i])
   
        if os.path.isfile(p1):
            count +=1
    
        if os.path.isdir(p1):
            print(os.listdir('./testdata/subdir/'))

print(count)