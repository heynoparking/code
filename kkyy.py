class MyException(Exception):
    def __init__(self, err_msg):
        self.msg = err_msg
    def __str__(self):
        return "abc" + self.msg

try:
    raise MyException("I'm an exception message!")
except MyException as e:
    print("---encountered MyEception---")
    print(e)