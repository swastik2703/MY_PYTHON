from inspect import istraceback


def last(n):
    return n[-1]

def sort_list(lists):
    return sorted(lists,key = last)

list = [(2,5),(1,2),(4,4),(2,3),(2,1)]

print(sort_list(list))
