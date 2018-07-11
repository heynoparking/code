import random
answer= random.randint(1,100)
guess=0

while guess != answer:
    guess = int(input("enter a number"))

    if guess>answer:
        print("too big")
        print"answer",answer
    elif guess<answer:
        print("too small")
        print"answer",answer
    else:
        print("correct")
   