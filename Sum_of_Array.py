n=int(input())
sum1=list(map(int,input().split()))
s=0
for i in range(n):
    s+=sum1[i]
print(s)