a = int(input("enter the first no: "))
b = int(input("enter the second no: "))
c = int(input("enter the third no: "))
if(a < b) and (a < c):
    if(b < c):
        print(a,b,c)
    else:
        print(a,c,b)
elif(b < a) and (b < c):
    if(a < c):
        print(b,a,c)
    else:
        print(b,c,a)
else:
    if(c < a) and (c < b):
        if(a < b):
            print(c,a,b)
        else:
            print(c,b,a)