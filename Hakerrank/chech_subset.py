

from unittest import result

resul=[]
number=int(input())
for n in range(number):
    index_A=int(int(input()))
    A=set(map(int,input().split()))
    index_B=int(input())
    B=set(map(int,input().split()))
    if len(A.intersection(B))==len(A):
        resul.append(True)
    else:
        resul.append(False)

for r in resul:
    print(r)