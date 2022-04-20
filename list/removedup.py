from enum import unique


num = [1,2,3,4,4,5,6,6,1,2,8]
unique = []

for i in num:
    if i not in unique:
        unique.append(i)
print(unique)