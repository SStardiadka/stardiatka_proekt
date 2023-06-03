import pprint


#  распаковать_словарь красиво через рекурсию
def flatten_dict(d):
    # if dk1 == None:
    for i in d:
        if d[i].__class__ == dict and d[i] != {}:
            for j in d[i]:
                d[f"{i}_{j}"] = d[i][j]
                if len(d[i]) == 1:
                    d.pop(i)
                    return flatten_dict(d)
                else:
                    d[i].pop(j)
                    return flatten_dict(d)
        if d[i] == {}:
            d.pop(i)
            return flatten_dict(d)

        else:
            continue
    return d


pprint.pprint(
    flatten_dict(
        {
            "a": 1,
            "b": {
                "c": 2,
                "d": 3,
                "e": {
                    "f": 4,
                    "6": 100,
                    "5": {"g": 6},
                    "l": 1,
                },
            },
        }
    )
)
