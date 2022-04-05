a='ABCDCDC'
count=0
for i in range(len(a)):
    if a[i:].startswith('CDC'):
        count+=1
print(count)