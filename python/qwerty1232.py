class Cell:
    def __init__(self, is_free=None, value=0):
        if value == 0:
            self.is_free = None
            self.is_free = True
        if value == 1 or value == 2:
            self.is_free = False
        self.value = value

    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self, cell=Cell):
        self.pole = tuple(tuple(cell() for i in range(3)) for j in range(3))

    def clear(self):
        self.pole = tuple(tuple(Cell() for i in range(3)) for j in range(3))

    def indxeror2(self, a, b):
        if a < -3 or a > 2 or b < -3 or b > 2:
            raise IndexError("неверный индекс клетки")

    def indxeror1(self, a):
        if a < -3 or a > 2:
            raise IndexError("неверный индекс клетки")

    def __getitem__(self, key):
        if key.__class__ == list:
            self.indxeror2(key[0], key[1])
            return self.pole[key[0]][key[1]].value
        else:
            self.indxeror1(key)
            return tuple(i.value for i in self.pole[key])

    # def __setitem__(self, key, value):
    #     self.indxeror2(key[0], key[1])
    #     if self.pole[key[0]][key[1]].is_free == False:
    #         raise ValueError('клетка уже занята')
    #     self.pole[key[0]][key[1]].value = value
    #     self.pole[key[0]][key[1]].is_free = False

    def __call__(self):
        for i in self.pole:
            for j in i:
                print(j.value, end=" ")
            print()

    def __setitem__(self, key, value):
        self.indxeror2(key[0], key[1])
        if not self.pole[key[0]][key[1]].is_free:
            raise ValueError("клетка уже занята")
        self.pole[key[0]][key[1]].value = value
        self.pole[key[0]][key[1]].is_free = False
        self()

    # def __getitem__(self, key):
    #     if type(key[0]) == slice:
    #         if key[1] < 3:
    #             return tuple(self.pole[i][key[1]].value for i in range(3))
    #         else:
    #             raise IndexError('неверный индекс клетки')
    #     elif type(key[1]) == slice:
    #         if key[0] < 3:
    #             return tuple(self.pole[key[0]][i].value for i in range(3))
    #         else:
    #             raise IndexError('неверный индекс клетки')
    #     else:
    #         if key[0] < 3 and key[1] < 3:
    #             return self.pole[key[0]][key[1]].value
    #         else:
    #             raise IndexError('неверный индекс клетки')
