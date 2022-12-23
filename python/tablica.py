from prettytable import PrettyTable
table = PrettyTable()
table.field_names =(['name','age','citi'])
table.add_row(['дима','48','дунаев'])
table.add_row(['ало','7','дунаев'])
table.align = 'c'
table.sortby = 'age'
print(table)
