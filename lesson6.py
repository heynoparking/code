class Newtype:
    weight = 50
    hight = 165
    age = 25

z = Newtype()
z.weight = 45
z.hight = 157
z.age = 23

print (z.weight,z.hight,z.age)




class Newtype2:
    weight = 50
    hight = 165
    age = 25
    def name(self,myname):
        self.name = myname

x = Newtype2()
x.myname = ('yurou')
print(x.myname)



class Shape:
    
    def set_edge (self,edge):
        self.edge = edge
        
    def display (self):
        for i in range (self.edge):
            for j in range (i):
                print ('*',sep='',end='')
            print("")

w = Shape()
w.set_edge(5)
w.display()






class Map:
    
    def set_map (self,num):
        listA.append(num)

         [[＊, ＊],[＊, ＊]]
        
        self.num = num
        print (self.num)
    
    def set_pattern (self,num2):
        self.num2 = num2
    
    def display(self):
        for i in range (self.num):
            a = self.num
            for j in range (a):
                print ('*',sep='',end='')
            print("")

m = Map()
m.set_map(5)
m.display()
