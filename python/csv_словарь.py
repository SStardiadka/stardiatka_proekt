#  csv_словарь


def read_csv():
    with open('data (1).csv', encoding='utf-8') as files:
        kluch = files.readline()
        kluch = [i.rstrip() for i in kluch.split(',')]
        lst = files.readlines()
        lst = [i.rstrip().split(',') for i in lst]
        return [dict(zip(kluch, lst[i])) for i in range(len(lst))]
