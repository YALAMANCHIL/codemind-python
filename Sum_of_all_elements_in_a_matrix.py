#Adding the Matrix
#Reading
r,c=map(int,input().split())
mat=[]
for i in range(r):
    inner_list = list(map(int,input().split()))
    mat.append(inner_list)
s=0
#Element based accessing
for inner_list in mat:
    for every_value in inner_list:
        s+=every_value
print(s)