file = open('sales_data.txt', 'r', encoding='utf-8')


def open_from_file(file):
    files = file.read()
    my_dict = []
    for row in files.split('\n'):
        my_dict.append(tuple(row.split(',')))
    return my_dict


my_list = open_from_file(file)

file.close()
