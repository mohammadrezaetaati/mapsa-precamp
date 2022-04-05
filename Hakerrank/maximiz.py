from itertools import product
number_list,k=input().split()
input_list=[]
mod=[]
for i in range(int(number_list)):
    input_user=input().split()
    input_user=list(map(int,input_user))
    input_list.append(input_user[1:])
pro=list(product(*input_list))
for l in pro:
    pow=0
    for i in l:
        pow+=i**2
    pow=pow%int(k)
    mod.append(pow)
print(max(mod))



