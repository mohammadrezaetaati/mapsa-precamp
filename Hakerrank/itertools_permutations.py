from itertools import permutations
string,count=input('Enter string and line containing ').split()
string=list(map(lambda x:x,string)) 
string.sort() 
per=permutations(string,int(count))   
for tup in per:
    for chr in tup:
        print(chr,end='')
    print()