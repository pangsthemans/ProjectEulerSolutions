from math import factorial
num=factorial(100)
num=str(num)
total=0
print(int(num[0]))
for x in num:
    total=total+int(x)
print(total)