from itertools import combinations
string,number=input().split()
string=list(map(lambda x:x,string))
string.sort()
for n in range(1,int(number)+1):
    comb=list(combinations(string,n))
    for chr in comb:
            print(''.join(chr))
