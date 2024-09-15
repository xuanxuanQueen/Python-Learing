import sys,os

Pets = ['小狗','一个月','小猫','一年','鹦鹉','半年']
print(Pets)

Pets.append('边牧')
print(Pets)

Pets.insert(6,'2个月')
print(Pets)

Pets.reverse()
print(Pets)

num = 0
for i in Pets:
    num = num + 1
    print(str(num) + i)








        