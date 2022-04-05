A=set(map(int,input().split()))
B=set()
number=int(input())
for n in range(number):
    element=set(map(int,input().split()))
    B.update(element)
if len(A.intersection(B))==len(B):
    print(True)
else:
    print(False)

