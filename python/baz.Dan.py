import sqlite3

# создаем файл базы данных
db = sqlite3.connect("dbName.db")

# создаем курсор
c = db.cursor()

# создаем поля таблицы
# с.execute('''CREATE TABLE articles (
#     title text,
#     ful_text text,
#     views integer,
#     avtor text)''')

# добавляем записи в поля
# c.execute('''INSERT INTO articles VALUES
#           ('mitri ze best', 'Dima ze best ze Dima ze best ze', 1000, 'mitri')
#           ''')

# изменение в таблице
# c.execute("UPDATE articles SET avtor = 'kracavhik' WHERE title='mitri ze best'")

# УДАЛЕНИЕ
# c.execute('DELETE FROM articles WHERE avtor = "mitri"')

# выборка и вывод данных
# c.execute("SELECT rowid, * FROM articles")

# выборка данных с условием
# c.execute("SELECT rowid, * FROM articles WHERE rowid = 1")

# выборка данных с сортировкой
# c.execute("SELECT rowid, * FROM articles WHERE rowid > 0 ORDER BY rowid DESC")
# print(c.fetchall())

# items = c.fetchall()
# for i in items:
#     print(*i)
# db.commit()

# db.close()
c.execute("SELECT * FROM articles")
with open(
    r"C:\stardiatka_proekt-1\python\Wfiles\temp.txt", "w", encoding="utf-8"
) as file:
    file.write(f"{c.fetchall()}")
print(c.fetchall())
