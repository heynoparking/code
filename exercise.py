class Map:

    
    def set_map (self,n):
        self.len = n
        self.n = [ ["*"] * n for i in range(n) ]

        

    def set_pattern (self,n2):
        
        

        
        self.n[int((self.len -1) /2+n2)][int((self.len -1) /2)]=0
        self.n[int((self.len -1) /2-n2)][int((self.len -1) /2)-n2]=0
        self.n[int((self.len -1) /2-n2)][int((self.len -1) /2)]=0
        self.n[int((self.len -1) /2-n2)][int((self.len -1) /2)+n2]=0
        self.n[int((self.len -1) /2)][int((self.len -1) /2)-n2]=0

    
    
    def display (self):
        print(self.n)
        for i in range(self.len):
            for j in range(self.len):
                print (self.n[i][j], end = ' ')
            print ('')


m = Map()
m.set_map(5)
m.set_pattern(1)
m.display()