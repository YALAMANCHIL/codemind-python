n=int(input())
sum1=list(map(int,input().split()))
m=int(input())
s=0
for i in range(n):
    if sum1[i]==m:
      s=1
      break
if (s==1):
    print("True")
else:
    print("False")
       