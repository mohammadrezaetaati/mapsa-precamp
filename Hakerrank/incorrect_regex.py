import re
number=int(input())
result=[]
for n in range(number):
    regex=input()
    try:
        re.findall(regex,'TestRegex')
        result.append('True')
    except:
       result.append('False')
for r in result:
    print(r)
