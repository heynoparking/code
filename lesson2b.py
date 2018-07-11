a=6

for x in range(0,6):
    a-=1
    for y in range(0,a):
        print "*",
    print "\n"



i = 1
j = 1
a = 6

while i <= 5:
    a-=1
    while j <= a:
        print "*",
        j += 1
    print("\n")
    j = 1
    i += 1