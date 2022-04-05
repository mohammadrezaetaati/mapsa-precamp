from collections import deque
number=int(input())
deq=deque([])
for _ in range(number):
    command=input().split()
    if command[0]=='append':
        deq.append(int(command[1]))
    elif command[0]=='pop':
         deq.pop()
    elif command[0]=='popleft':
         deq.popleft()
    elif command[0]=='appendleft':
         deq.appendleft(int(command[1]))

for e in deq:
    print(e,end=' ')
