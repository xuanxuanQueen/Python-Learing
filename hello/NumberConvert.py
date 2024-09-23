number = input(' 请输入整数数字')
a = "零一二三四五六七八九"
for i in number:
    print(a[eval(i)], end='')
