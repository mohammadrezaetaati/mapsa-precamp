
A_element=int(input())
A=list(map(int,input().split()))
A=set(A)
number_sets=int(input())
for n in range(number_sets):
    operation,number=input().split()
    set_input=list(map(int,input().split()))
    set_input=set(set_input)
    if operation=='intersection_update':
        A.intersection_update(set_input)
    elif operation=='update':
        A.update(set_input)
 
    elif operation=='symmetric_difference_update':
        A.symmetric_difference_update(set_input)
    elif operation=='difference_update':
        A.difference_update(set_input)
print(sum(A))