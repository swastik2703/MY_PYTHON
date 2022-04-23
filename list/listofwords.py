from enum import unique


list = ["abc","bda","hdaf","ghfscj","fsjf","djfghwegfrukwe"]
unique = []
n = 4
for i in list:
    if len(i) >= n:
        unique.append(i)
print(unique)