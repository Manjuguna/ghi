g=int(input())
s=list(map(int,input().split()))
goo=0
for one1 in range(g):
    for two2 in range(one1,g):  
        for three3 in range(two2,g):
            if s[one1]<s[two2]<s[three3]:
                goo+=1
print(goo)
