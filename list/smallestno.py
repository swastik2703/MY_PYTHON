from cgitb import small


l1 = [2,10,12,9,11,1]
smallest = l1[0]

for i in l1:
    if i < smallest:
        smallest = i
        i+= 1
print(f"smallest no is:- {smallest}")