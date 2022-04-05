from itertools import combinations_with_replacement
string,number=input().split()
string=list(map(lambda x: x,string))
string.sort()
string=list(combinations_with_replacement(string,int(number)))
for chr in string:
    print(''.join(chr))