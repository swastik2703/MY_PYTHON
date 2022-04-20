number = [1,3,5,6,7]
#append function
number.append(50)
print(number)

#to insert at start or mid

number1 = [2,3,4,5]
print("before inserting at start")
print(number1)
number1.insert(0,1)

print("after inserting at start")
print(number1)


print("after inserting at mid")
number1.insert(2,33)
print(number1)

#remove element
print("these are the fruits name:- ")
fruits = ["apple","mango","banana","lichi"]
print(fruits)

fruits.remove("apple")
print("after removing")
print(fruits)


#clear function

num = [12,33,45,66,70]
print(f"before clearing{num}")

num.clear()
print(f"after clearing{num}")

#reverse function

str = [0,"swastik",'a',10]
print(str)

print("after reversing")
str.reverse()
print(str)
