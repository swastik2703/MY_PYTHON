l1 = [2,10,12,9,11]
largest = l1[0]

for i in l1:
    if i > largest:
        largest = i
        i+= 1
print(f"largest no is:- {largest}")