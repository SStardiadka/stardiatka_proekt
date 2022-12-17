#  распокавать_списки_внутри_списка
def get_line_list(d,a=[]):
    for i in d:
        if  not isinstance(i, list):
            a.append(i)
        elif isinstance(i, list):
            get_line_list(i, a)
             
    return a 
print(get_line_list([[[[9]]], [1, 2], [[8]]]))