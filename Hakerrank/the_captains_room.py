from collections import defaultdict
k=int(input())
room=input().split()
number=defaultdict(list)

for r in room:
    number[r].append(r)
for v in number.values():
    if len(v)==1:
        print(v[0])

    