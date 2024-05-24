def mid(data_in):
    data_in = list(((str(data_in)).strip()).split(" "))
    data_str_num = []
 
    for i in data_in:
        if i != '':
            data_str_num.append(int(i))
        else:
            continue
 
    return str(round((sum(data_str_num) / len(data_str_num)), 1))
 
 
while var := input():
    print(mid(var))