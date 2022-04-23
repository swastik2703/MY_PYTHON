from enum import unique


list = [1,2,2,2,3,5,3,4,4,4]
unique = []

for i in list:
    if i not in unique:
        unique.append(i)
print(unique)
