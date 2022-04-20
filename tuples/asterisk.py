#use asterisk * symbol 

items = ("apple","manago","banana","guava","pomegranate")
x,y,*z = items
print(f"x = {x}" , f"y = {y}",f"z = {z}")

a,*b,c = items
print(f"a = {a}" , f"b = {b}",f"c = {c}")