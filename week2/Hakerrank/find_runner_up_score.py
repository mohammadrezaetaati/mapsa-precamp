input_user=int(input('Enter A Number :'))
input_arry=list(map(int,input('Enter A Number :').split()))
for i in range(input_arry.count(max(input_arry))):
    input_arry.remove(max(input_arry))
print(max(input_arry))

