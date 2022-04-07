print("enter the first number:")
num1 = int(input())
print("enter the second number:")
num2 = int(input())

if (num1 < num2):
    print(num1,"is smallest")
elif (num2 < num1):
    print(num2,"is smallest")
else:
    print("both are equal")