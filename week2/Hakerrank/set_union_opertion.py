number1=int(input())
student1=input().split()
student1=set(map(int,student1))
number2=int(input())
student2=input().split()
student2=set(map(int,student2))
union=student1|student2
if len(union)==0:
    print('0')
else:
    print(len(union))