n=int(input())
sum=list(map(int,input().split()))
s=0
for i in range(0,n):
    if sum[i] % 2!=0:
        s+=sum[i]
print(s)