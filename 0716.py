class RelationException(Exception):
    
    
    def __init__(self,pa,pb):
        self.pa = pa
        self.pb = pb


    def __str__(self):
        
        return ("Are you sure that " + self.pa + " and " + self.pb + " are in love with each other?")
        
    
    def check (pa,pb):

        relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}
        
        if relation[pa] != pb :
            raise RelationException (pa,pb) 
            raise KeyError 

    
    
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    RelationException.check (p1,p2)
    print("{} and {} are in love with each other!".format(p1, p2))
    
except RelationException as e :
    print("---encountered MyEception---")
    print (e)
except KeyError as e :
    
    print (e)
    


