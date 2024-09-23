Money=input("请输入要转化的币种和金额")
if Money[0:3] in ['RMB']:
    U=eval(Money[3:])/6.78
    print("USD{:.2f}".format(U))
elif Money[0:3] in ['USD']:
    R=eval(Money[3:])*6.78
    print("RMB{:.2f}".format(R))
else:
    print()