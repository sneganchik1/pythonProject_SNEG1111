#
# class Furniture:
#     """
#     Class Furniture
#     """
#     high = 1
#     width = 2
#     def __init__(self, high1, width1, name):   #позволяет в класс атрибуты
#         self.high1 = high1
#         self.width1 = width1
#         self.name = name
#
#     def show_furniture(self):
#         print(f'show_furniture {self.name}, class arg - {self.high}, {self.width}, obj_arg - {self.high1}, {self.width1}')
#     # pass
#
# # print(type(Furniture))
# # print(Furniture.__doc__)
# # print(Furniture.var_num)
# # print(Furniture.show_furniture)
#
# table = Furniture(10, 20, 'table') # create furniture object
# print(table.show_furniture())
# print(table.high)
#
# chair = Furniture(5, 7, 'chair') # create furniture object
# print(chair.show_furniture())
# print(chair.width)
#
# __________________________________________________________________


class Furniture:
    """
    Class Furniture
    """
    high = 1
    width = 2
    def __init__(self, high1, width1, name):   #позволяет в класс атрибуты
        self.high1 = high1
        self.width1 = width1
        self.name = name
    def func(self):
        print('func in class Furniture')

    def show_furniture(self):
        print(f'show_furniture {self.name}, class arg - {self.high}, {self.width}, obj_arg - {self.high1}, {self.width1}')


class Table(Furniture):
    table = 'table'

    def func(self):
        print('func in class table')
    pass

table = Table(10, 20, 'table')
print(table.show_furniture())
print(table.func())

furn = Furniture(1, 2, 'furn')
print(isinstance(table, Table))
print(isinstance(table, Furniture))
print(isinstance(furn, Furniture))
print(isinstance(furn, Table))