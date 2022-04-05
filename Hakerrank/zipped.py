x,n=input().split()
scores=[]
for _ in range(int(n)):
    score=list(map(float,input().split()))
    scores.append(score)
for tuple in list(zip(*scores)):
    print(sum(tuple)/int(n))
