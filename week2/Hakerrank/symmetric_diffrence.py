
size_a=int(input())
a=input().split()
size_b=int(input())
b=input().split()
a_diffe=[]
b_diffe=[]
if size_a==len(a) and size_b==len(b):
    a=list(map(int,a))
    b=list(map(int,b))
    for i in a:
        if i not in b and i not in a_diffe:
            a_diffe.append(i)
    for i in b:
        if i not in a and i not in b_diffe :
            b_diffe.append(i)
    a_diffe.extend(b_diffe)
    a_diffe.sort()
    for i in a_diffe:
        print(i)

    
   

