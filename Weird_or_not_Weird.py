a=int(input())
n=a%2
if (n!=0):
    print("weird")
elif (n==0 and a>=2 and a<=5):
    print("not weird")
elif (n==0 and a>=6 and a<=20):
    print("weird")
else:
    print("not weird")