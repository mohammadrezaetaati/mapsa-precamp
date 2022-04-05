
number=int(input())
title=input().split()
markas=[]
indext=title.index('MARKS')
for _ in range(number):
    column=input().split()
    markas.append(int(column[indext]))
print(sum(markas)/number)


   





