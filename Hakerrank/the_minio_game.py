s=input()
vowels=('A','U','I','E','O')
sture=[]
kevin=[]
for i in range(len(s)):
    for chr in range(1,len(s)+1):
        if i<chr and s[i]not in vowels:
            sture.append(s[i:chr])
        elif i< chr:
            kevin.append(s[i:chr])
if len(sture)>len(kevin):
    print('sture',len(sture))
else:
    print('kevin',len(kevin))
