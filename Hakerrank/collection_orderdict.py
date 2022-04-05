from collections import defaultdict
name_price=defaultdict(list)
number=int(input())
for i in range(number):
    a=input().split()
    name_price[' '.join(a[:-1])].append(int(a[-1]))
for key,val in name_price.items():
    print(f'{key} {sum(val)}')