class Cat:
   

    def __init__(self, name={}, age=None, isHappy=None):
        self.name = name
        self.age = age
        self.isHappy = isHappy
        self.get_data()

   
    def get_data(self):
        print(self.name, "age:", self.age, ". Happy:", self.isHappy)


cat1 = Cat()


cat2 = Cat("Жопен", 2, False)
print(cat2.name)