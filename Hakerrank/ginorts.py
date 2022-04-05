from curses.ascii import isalpha, islower, isupper
sort=[]
input_user=input()
lower=list(filter(lambda x:islower(x),input_user))
lower.sort()
sort.append(lower)
upeer=list(filter(lambda x:isupper(x),input_user))
upeer.sort()
sort.append(upeer)
number=list(filter(lambda x: not isalpha(x),input_user))
number.sort()
number.sort(key=lambda x:int(x)%2==0)
sort.append(number)
for l in sort:
    for i in l:
        print(i,end='')




