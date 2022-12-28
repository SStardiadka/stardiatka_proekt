from prettytable import PrettyTable
table = PrettyTable()
table.field_names =(['name','age','citi', 'er'])
table.add_row(['дима','48','дунаев','1'])
table.add_row(['ало','7','дунаев', '2'])
table.align = 'c'
table.sortby = 'age'
print(table)
with open(r'C:\stardiatka_proekt-1\python\Rfiles\tabl.png', 'w', encoding= 'utf-8"') as f:
    print(table, file=f)