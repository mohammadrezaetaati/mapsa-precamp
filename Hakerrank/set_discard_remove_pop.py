number_elements=int(input())
element_contains=input().split()
element_contains=set(map(int,element_contains))
number_commands=int(input())
for n in range(number_commands):
    command=input().split()
    if command[0]=='pop':
        element_contains.pop()
    elif command[0]=='remove' and int(command[1]) in element_contains:
        element_contains.remove(int(command[1]))
    elif command[0]=='discard':
        element_contains.discard(int(command[1]))
if len(element_contains)==0:
    print('0')
else:
    print(sum(element_contains))



