import re


class AuthSystem:
    

    def __init__(self):
        """Define regex"""
        self.username = input ("username")
        self.password = input ("password")
        self.username_regex = re.compile(r'(?P<Username>[A-Z][a-z][a-z])')
        self.password_regex = re.compile(r'(?P<Password>[a-z][a-z][a-z][0][0-9][0-9][0-9][0-9][0-9])')
        match = re.search(self.username_regex,self.username)
        match2 = re.search(self.password_regex, self.password)
        

    def _check_username(self):

        if len(self.password) == 9 and len(self.username) ==3 :

            if (self.username_regex.search(self.username) is not None ) and (self.password_regex.search(self.password) is not None):
            
                print("Welcome," + (self.username) + "!")

            

            elif (self.username_regex.search(self.username) is None ) and (self.password_regex.search(self.password) is not None):

                print  ("Username format error! Your username is " + self.username)
            

            elif (self.username_regex.search(self.username) is not None ) and (self.password_regex.search(self.password) is None):

                print ("Password format error! Your password is " + self.password)

            

            else:

                print ("Valid")
        else:

            if len(self.password) != 9 and len(self.username) ==3 :
                print ("Password legnth error! Your password length is " + str( len(self.password))+" . ")

            elif len(self.username) != 3 and len(self.password) ==9 :
                print ("Username legnth error! Your username length is " + str( len(self.username))+" . ")

            else:
                print ("Valid ")


        

    
        
    
        


    
# Construct a object of type AuthSystem
auth = AuthSystem()
auth._check_username()



