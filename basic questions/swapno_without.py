from tkinter import Y


x = int(input("enter first number: "))
Y = int(input("enter second number: "))
print("before swapping:")
print("x =",x , "Y =",Y)
x = x + Y
Y = x - Y
x = x - Y
print("after swapping:")
print("x =",x , "Y =",Y)
