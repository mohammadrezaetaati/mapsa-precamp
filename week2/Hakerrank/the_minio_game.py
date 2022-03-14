str=input('Enter string :')
vowels=('A','U','I','E','O')
sture=[]
kevin=[]
for i in range(len(str)):
    for chr in range(1,len(str)+1):
        if i<chr and str[i]not in vowels:
            sture.append(str[i:chr])
        elif i< chr:
            kevin.append(str[i:chr])
if len(sture)>len(kevin):
    print('sture',len(sture))
else:
    print('kevin',len(kevin))
