
# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y
# def div(x,y):
#     return x/y
# def mod(x,y):
#     return x%y

# print("choose operation")
# print("1.ADD")
# print("2.subtract")
# print("3.Multiply")
# print("4.division")
# print("5.modulo")

# while True:
#     choise = input("enter the choise(1/2/3/4): ")
#     if choise in ('1','2','3','4'):
#         num1 = float(input("enter the first no: "))
#         num2 = float(input("enter the second no: "))
#         if choise == '1':
#             print(num1,"+",num2 ,"=",add(num1,num2))
#         elif choise == '2':
#             print(num1,"-",num2,"=",sub(num1,num2))
#         elif choise == '3':
#             print(num1,"*",num2,"=",mul(num1,num2))
#         elif choise == '4':
#             print(num1,"/",num2,"=",div(num1,num2))
#         elif choise == '5':
#             print(num1,"%",num2,"=",mod(num1,num2))       
#         again = input("want to do some more calculations(y/n): ")
#         if again == 'no':
#             break
#     else:
#         print("invalid input")



def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y
def mod(x,y):
    return x % y

print("select the operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.division")
print("5.modulos")

while True:
    choise = input("enter your choise(1/2/3/4/5): ")
    if choise in ('1','2','3','4','5'):
        num1 = float(input("enter first number- "))
        num2 = float(input("enter second number- "))
        if choise == '1':
            print(add(num1,num2))
        elif choise == '2':
            print(sub(num1,num2))
        elif choise == '3':
            print(mul(num1,num2))
        elif choise == '4':
            print(div(num1,num2))
        elif choise == '5':
            print(mod(num1,num2))
        next_calculation = input("want to do more calculation(yes/no): ")
        if next_calculation == 'no':
            break
    else:
        print("invalid input")