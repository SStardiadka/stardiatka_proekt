class Money:
    def __init__(self, money):
        if type(money) in (int, float):
            self.__money = money
        else:
            raise TypeError("сумма должна быть числом")

    @property
    def money(self):
        return self.money

    @money.setter
    def money(self, value):
        if type(value) not in (int, float):
            raise TypeError("сумма должна быть числом")
        else:
            self.__money = value


m = Money(123)
# m.money = '5678'
m.money = 12345
# m.__money = "5678"
print(m.__dict__)
