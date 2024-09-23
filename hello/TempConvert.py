T = input("请输入想转化的温度")  # 格式数字加单位
if T[-1] in ["C", "c"]:
    F = eval(T[0:-1]) * 1.8 + 32
    print("转化后的温度为{:.2f}F", format(F))  # 输出保留运算后两位小数
elif T[-1] in ["F", "f"]:
    C = (eval(T[0:-1]) - 32) / 1.8
    print("转化后的温度为{:.2f}C", format(C))
else:
    print("输入格式错误")
