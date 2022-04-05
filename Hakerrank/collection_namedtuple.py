from collections import namedtuple
number=int(input())
title=input().split()
markas=[]
indext=title.index('MARKS')
for _ in range(number):
    a=input().split()
    markas.append(int(a[indext]))
print(sum(markas)/number)


   





