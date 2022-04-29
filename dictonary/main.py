#store key value pair
d1 = {}
#print(type(d1))

d2 = {"sv":"burger","rew":"dal","rhda":"roti"}
print(d2)
print(d2["rew"])
print(d2["sv"])


#dictionary in dictionary
d = {'a':'maggi','b':'pasta','c':"noodles",'d':{'B':'tea','L':'curd','D':'milk'}}
print(d['d']['B'])

#how to add more keys

d["swastik"] = "cool blue"
d[12] = "ice cream"
print(d)

#how to delete
print("\n")
print("after deleting\n")
del d['c']
print(d)
