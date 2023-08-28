s=int(input())
H=(s//3600)
M=(s-(3600*H))//60
S=(s-(3600*H)-(M*60))
print("H:M:S-{}:{}:{}".format(H,M,S))