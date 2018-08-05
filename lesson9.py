import re

text = "Yurou Wang"

# Define pattern
pattern = r'(?P<First_Name>Yurou) (?P<Last_name>Wang)'

# search pattern
match = re.search(pattern, text)

# Check
d = match.groupdict()
print(type(d))
print(d)




import re

text = "NCKU-65405"

pattern = r'(?P<school>\w\w\w\w)-(?P<room>\d\d\d\d\d)'

match = re.search(pattern,text)

print (match.groupdict())





import re

text = input("your name: ")
text1 = input("your name: ")
text2 = input("your name: ")

pattern = r'(?P<First_name>\w\w\w) (?P<Last_name>\w\w\w\w)'

match = re.search(pattern,text)
match1 = re.search(pattern,text1)
match2 = re.search(pattern,text2)


# if match != None:


print (match.groupdict())
print (match1.groupdict())
print (match2.groupdict())





import re

class AuthSystem:
    
    def __init__(self):
        """Define regex"""
        self.username_regex = re.compiler(r'(?P<First_name>\w\w\w)')
        self.password_regex = re.compile(r'(?P<Last_name>\w\w\w\w)')
    
    def _check_username(self, username):
        """Check username is valid or not"""
        if self.username_regex.search(username) is not None:
            print("Correct username")
            return True
        else: 
            print("Wrong username")
            return False
        
    def _check_password(self, password):
        """Check password is valid or not"""
        if self.password_regex.search(password) is not None:
            print("Correct password")
            return True
        else:
            print("Wrong password")
            return False
        
    def authenticate(self, username, password):
        """authenticate the user"""
        if not self._check_username(username):
            return
        
        if not self._check_password(password):
            return
        
        print("Valid user")

    
# Construct a object of type AuthSystem
auth = AuthSystem()

# authenticate the user's credentials
auth.authenticate("johnny", "johnny860410")





import re

# texts which re applies to
text1 = " and cookie"
text2 = "CakeCakeCake and cookie"

# Define pattern
plus_pattern = "(Cake)+ and cookie"

# search pattern in texts # 
plus_match1 = re.search(plus_pattern, text1)
plus_match2 = re.search(plus_pattern, text2)

# check
print(plus_match1)
print(plus_match2.group())