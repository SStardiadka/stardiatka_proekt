class ListObject:
    """
    Вам необходимо реализовать односвязный список
    (не список языка Python, объекты в списке не хранить,
    а формировать связанную структуру, показанную на рисунке)
    из объектов класса ListObject:
    """

    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
head_obj = ListObject(lst[0])
obj = head_obj

for i in range(1, len(lst)):
    obj_new = ListObject(lst[i])
    obj.link(obj_new)
    obj = obj_new
