file = open('sales_data.txt', 'r', encoding='utf-8')


def open_from_file(file):
    files = file.read()
    my_dict = []
    for row in files.split('\n'):
        my_dict.append(tuple(row.split(',')))
    return my_dict


def my_dictionary(sale_dict):
    my_dict = {}
    for element in sale_dict:
        if my_dict.get(element[0]):
            my_dict[element[0]] += int(element[1])
        else:
            my_dict[element[0]] = int(element[1])
    return my_dict


def from_dict_on_list(dict_of_list):
    return list(dict_of_list.items())


my_list = open_from_file(file)
my_dict = my_dictionary(my_list)
my_new_list = from_dict_on_list(my_dict)
print(my_new_list)
file.close()
