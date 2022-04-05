def average(array):
    array=set(map(int,array))
    averg=sum(array)/len(array)
    return averg
print(average(input().split()))