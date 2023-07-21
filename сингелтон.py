class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name


s = Singleton(1)
print(s.instance)
# print("Object created", s.__dict__, s)
# print(s.name)
# s1 = Singleton(2)


# print("Object created", s1.__dict__, s1)
# print(s1.name)
# print(s.instance)
