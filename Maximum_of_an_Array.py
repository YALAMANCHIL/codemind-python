n=int(input())
sum1=list(map(int,input().split()))
min1=sum1[0]
for i in range(n):
    if(min1<sum1[i]):
        min1=sum1[i]
print(min1)
        