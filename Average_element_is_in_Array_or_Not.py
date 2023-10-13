n=int(input())
sum1=list(map(int,input().split()))
s=0
for i in sum1:
    s+=i
d=s//n
if (d in sum1):
    print('True')
else:
    print('False')
       