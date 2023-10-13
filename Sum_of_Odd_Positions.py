n=int(input())
sum1=list(map(int,input().split()))
s=0
for i in range(n):
    if (i%2!=0):
        s=s+sum1[i]
print(s)