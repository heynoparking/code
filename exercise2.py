class Map:

    def __init__ (self,n,p):
        self.len = n
        self.n = [ ["*"] * n for i in range(n) ]

        self.n2 = p
        self.n[int((self.len -1) /2+p)][int((self.len -1) /2)]=0
        self.n[int((self.len -1) /2-p)][int((self.len -1) /2)-p]=0
        self.n[int((self.len -1) /2-p)][int((self.len -1) /2)]=0
        self.n[int((self.len -1) /2-p)][int((self.len -1) /2)+p]=0
        self.n[int((self.len -1) /2)][int((self.len -1) /2)-p]=0



    def display (self):
        print(self.n)
        for i in range(self.len):
            for j in range(self.len):
                print (self.n[i][j], end = ' ')
            print ('')



m = Map(5,1)
m.display()