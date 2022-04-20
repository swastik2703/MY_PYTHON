#note in tuple we uses paranthesis where as in list we use square bracket
num = (1,2,3,4,1,1,1)
x = num.count(1)
print(f"1 is present {x} times")


#insert item in tuple

item = ("apple","banana","lichi")
x = list(item)
x.append("mango")
item = tuple(x)
print(item)