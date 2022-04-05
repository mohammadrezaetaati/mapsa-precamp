input_user=input().split()
input_user=list(map(int,input_user))
length=(input_user[0]-1)//2
for l in range(1,length+1):
    row=l*2-1
    print(('.|.'*row).center(input_user[1],'-'))  
print('welcom'.center(input_user[1],'-'))
for l in range(length+1,1,-1):
    row=l*2-3
    print(('.|.'*row).center(input_user[1],'-'))





