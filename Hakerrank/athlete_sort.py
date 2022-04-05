n,m=input().split()
arr=[]
for _ in range(int(n)):
    athletes=list(map(int,input().split()))
    arr.append(athletes)
k=int(input())
arr.sort(key=lambda x:x[k])
for l in arr:
    for el in l:
        print(el,end=' ')
    print()




    
