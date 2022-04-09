print("enter the range:")
n = int(input())
a = 0
b = 1
count = 0
while count < n:
    print(a)
    x = a + b
    a = b
    b = x
    count+= 1