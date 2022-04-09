x = int(input("enter a number: "))
flag = False
if x > 1:
    for i in range (2,x):
        if(x%i == 0):
            flag = True
            break
if flag:
    print("its not a prime no")
else:
    print("its a prime no")