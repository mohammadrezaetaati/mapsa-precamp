input_count=int(input('Enter Number commands :'))
list_custom=[]
for c in range(input_count):
    command,*number=input().split()
    number_list=list(map(int,number))
    if command=='insert':
        list_custom.insert(number_list[0],number_list[1])
    elif command=='print':
        print(list_custom)
    elif command=='remove':
        list_custom.remove(number_list[0])
    elif command=='append':
        list_custom.append(number_list[0])
    elif command=='sort':
        list_custom.sort()
    elif command=='pop':
        list_custom.pop(number_list[0])
    elif command=='reverse':
        list_custom.reverse()

