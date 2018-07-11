def maker(n):
    def action(x) :
        return  x ** n 
    return  action

h = maker(5)
print(h(9))





def way(n):
    def action(x) :
        return x * n
    return action 

h = way(0.03)
print(h(100))