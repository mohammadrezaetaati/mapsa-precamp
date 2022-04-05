from collections import defaultdict
n,m=input().split()
group_n=defaultdict(list)
group_m=[]
for i in range(int(n)+int(m)):
    if i<int(n):
        a=input()
        group_n[a].append(i+1)
    else:
        group_m.append(input())
for m in group_m:
    if m in group_n.keys():
        for chr in group_n[m]:
            print(chr,end=' ')
    else:
        print(-1,end='')
    print()




