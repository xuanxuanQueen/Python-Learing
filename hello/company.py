# 再给自己加一个buff吧
# 时间宝贵2024/9/1619:46
class people:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"I am {self.name},I am your manager.")


class staff(people):
    def __init__(self, name, age, gender, work):
        super().__init__(name, age, gender)
        self.work = work

    def introduce(self):
        print(f"I am {self.name},a {self.age} years old {self.gender},I can {self.work}.")


class mangers(people):
    def speak(self):
        print("Welcome to our company!")

b = staff("YYF",24,"female","design")
b.introduce()
a = mangers("SY",30,"male")
a.introduce()
a.speak()

