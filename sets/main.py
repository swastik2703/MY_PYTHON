#declaration
# s = set()
# print(type(s))

#how to print set values
# s1 = set({1,2,3,4})
# print(s1)
# print(type(s1))

#alternate way to add elements in set
# s.add(1)
# s.add(2)
# print(s)

#access items of set

new_set = set({"apple","mango","orange"})
new_set.add("guava")
for i in new_set:
    print(i)



new_set1 = set({"apple","mango","orange"})

new_set2 = set({"pineapple","papaya","grapes"})

new_set1.update(new_set2)
print(new_set1)


#remove element
x = set({"apple","mango","orange"})
x.remove("apple")
print(x)

#alternate way

y = set({"apple","mango","orange"})
y.discard("mango")
print(y)

#alternate

a = {1,2,3,4}
# a.pop()
# print(a)

#a.clear()
del a
print(a)

#join set

s1 = {'a','b','c'}
s2 = {1,2,3,4}
