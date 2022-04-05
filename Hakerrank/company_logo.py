
from collections import defaultdict
str_input=input()
default_str=defaultdict()
default_list=[]

for s in str_input:
    default_str[s]=str_input.count(s)

for key,val in default_str.items():
    default_list.append((key,val))
default_list.sort(key=lambda x:x[0])
default_list.sort(key=lambda x:x[1],reverse=True)

for tup in default_list[:3]:
    for chr in tup:
        print(chr,end=' ')
    print()
   

    
   

