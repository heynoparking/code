class Car:
    def s (self,speed,color):
        self.s__peed = 0
        self.color = color
        print (self.__speed,self.color)

    def boost (self):

        self.__speed += 10 
        print (self.__speed)

    def stop (self):

        self.__speed -=1
        print (self.__speed)

    def set_speed(self,speed):
        self.__speed = speed 
    
    def get_speed (self):

        return self.__speed
  

m = Car()
m.set_speed(180)
print (m.get_speed())
