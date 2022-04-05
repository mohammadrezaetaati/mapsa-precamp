


list_lengh=int(input())
input_list=list(map(int,input().split()))
number=0
for n in range(1,len(input_list)-2):
    if input_list[n]>input_list[n-1] and input_list[n]>input_list[n+1]:
        number+=1
        replace=[input_list[n],input_list[n-1],input_list[n+2]]
        input_list[n+1]=max(replace)

print(number) 
for ele in input_list: 
    print(ele,end=' ')

