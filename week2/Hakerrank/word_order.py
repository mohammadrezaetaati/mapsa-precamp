from collections import defaultdict
number=int(input())
word_order=defaultdict(list)
for n in range(number):
    word=input()
    word_order[word].append(n)
print(len(word_order))
for val in word_order.values():
    print(len(val),end=' ')
    
    
