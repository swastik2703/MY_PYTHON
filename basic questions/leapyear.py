print("leap year")

print("enter your year:")
year = int(input())
if (year % 400 == 0) and (year % 100 == 0):
    print("Its a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("Its a leap year")
else:
    print("its not a leap year")