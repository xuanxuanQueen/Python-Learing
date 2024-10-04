import sys,os

# 总重量
total = 100
totalnum = []

# 物品重量列表
num = [10,20,30,100,39,28]

num.sort()
print(num)

ans = 0
temp = 0.0
aa = len(num)
print(aa)
for i in range(0,aa):
    temp += totalnum[i]
    if(temp<=total):
        ans = ans + 1
    else:
        break
    
print(ans)