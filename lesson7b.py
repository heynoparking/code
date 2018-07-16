class Animal():
    def __init__ (self):
        self.feet_number = 4
    def scream (self):
        print ( "Hello! I'm an animal." )

class Dog(Animal):

    pass

animals = Animal()
dogs = Dog()

dogs.scream ()
print (dogs.feet_number)



def div(dividend, divisor):
    print("The answer is {}".format(dividend/divisor))

for i in range(5, -1, -1):
    for j in range(5, -1, -1):
        if i == 0 or j == 0 :
            continue
            
        else: 
            div(i, j)



try :
    print ("in try block")
except Exception:
    print ("In Exception block")
else:
    print ("No exxeption")


      

def div(dividend, divisor):
    print("The answer is {}".format(dividend/divisor))

for i in range(5, -1, -1):
    for j in range(5, -1, -1):
        try :
            div(i,j)
        except Exception:
            print ("nonono")
        else:
            print ("okok")

try:
    num = x  
except NameError as e:
    print(e)
    print (type(e))
    print (e.args)



a = [1, 2, 3]
try:
    num = x
    print(a[100])
    
except NameError as e:
    print("I'm in NameError! ")
    print(e)
except IndexError as e:
    print("I'm in IndexError!" )
    print(e)
else:
    print("I'm in else!")







try:
    print("hello!")
    x = gggggg
except Exception as e:
    print(e)
else:
    print("In else")
finally:
    print("I'm in finally!")


try:
    print("hello!")
    x = gggggg
except Exception as e:
    print(e)
else:
    print("In else")

print("I'm in finally!")



def func():
    try:
        print("I'm in try block!")
        a = bggggggg
    except Exception:
        print("I'm in except block!")
        return
    finally:
        print("do something")
        
func()



a = [1, 2, 3]
try:

    num = x 
    print(a[100])
    

except (NameError,IndexError) as e:
    
    print(e)


def div(a, b):
    if b == 0:
        raise ValueError("divisor cannot be zero!")
    else: return a/b

num = div(1,0)
print(num)


class MyException (Exception):

    def __init__(self,err_msg):
        self.msg = err_msg
    def __str__(self):
        return "abc" + self.msg

try:
    raise MyException("I'm an exception message!")
except MyException as e:
    print("---encountered MyEception---")
    print(e)