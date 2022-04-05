from itertools import groupby
string=input()
modified_string=groupby(string,lambda x:x)
for key,group in modified_string:
    print((len(list(group)),int(key)),end=' ')
