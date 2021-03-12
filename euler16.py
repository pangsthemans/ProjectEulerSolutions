from math import pow
nth=0
n1=1
n2=1
count=2
while len(str(nth))<1000:
    nth=n1+n2
    n1=n2
    n2=nth
    # print(nth)
    count+=1
print(count)
print(len(str(nth)))
# print(nth)