#copy functions
from pickle import DICT


Dict = {"ram":"maggi","shyam":"burger","lella":"pizza"}
new = Dict.copy()   #method 1
x = dict(Dict)  #method 2
#print(x)


#access function using get key
Dict1 = {"ram":"maggi","shyam":"burger","lella":"pizza"}
x = Dict1.get("shyam")
#print(x)

y = Dict1.values()
print(y)

#check whether key exist or not
Dict = {"ram":"maggi","shyam":"burger","lella":"pizza"}
if 'Ram' in Dict:
    print("yes key is present")
else:
    print("sorry")


#how to update given dictionary
Dict3 = {"ram":"maggi","shyam":"burger","lella":"pizza"}
Dict3.update({'ram':'hot dog'})
#print(Dict3)


#nested  dictionary
child1 = {'name':'swastik','year':'2003'}
child2 = {'name':'mukesh','year':'2005'}
child3 = {'name':'motu','year':'2010'}

myFam = {'child1' : child1, 'child2' : child2, 'child3' : child3}
print(myFam)
