from hashlib import new
from operator import index
from turtle import color


l1 = ["red","green","white","black","pink","yellow"]
new_list = []
for index,color in enumerate(l1):
    if index not in (0,4,5):
        new_list.append(color)
print(new_list)