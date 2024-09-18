c = 500
n=0
w=[100,200,100,300]
p=sorted(w)


print(p)
ans=0
tmp=0
j = 0

for j in range(0,len(p)):
    tmp = tmp+w[j]

    if tmp<c:
        ans = ans+1
    else:
        break
    j=j+1
print(ans)