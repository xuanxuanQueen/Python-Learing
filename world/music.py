# 再给自己加一个buff吧
# 时间宝贵2024/9/1614:43
class Music:
    def __init__(self, name, singer ):
        self.name = name
        self.singer=singer

    def get_name(self):
        return self.name

    def get_singer(self):
        return self.singer

m=Music("Rolling","Adele")
print(m.get_name())