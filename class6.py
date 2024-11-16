import random

marks=[]
for i in range(20):
    x=random.randint(0,100)
    marks.append(x)
print(marks)
high=[]
mid=[]
low=[]
for mark in marks:
    if mark<=30:
        low.append(mark)
    elif mark>=31 and mark<=69:
        mid.append(mark)
    else:
        high.append(mark)


twoD=[[6,2],[4,7]]
print(twoD[1][1])










