file = open('sales_data.txt', 'r', encoding='utf-8')


def open_from_file(file):
    files = file.read()
    my_dict = []
    for row in files.split('\n'):
        my_dict.append(tuple(row.split(',')))
    return my_dict


def my_dictionary(sale_dict):
    num1 = 0
    num2 = 0
    num3 = 0
    my_dict = {}
    for element in sale_dict:
        my_dict[element[0]] = int(element[1])
        if my_dict.get(element[0]):
            my_dict[element[0]] += int(element[1])


# def sum_all_vse():
#     pass
#
#
# def summa_sale(all_sale_dict):


# def summa_sale(all_sale_dict):
#     num1 = 0
#     num2 = 0
#     num3 = 0
#     my_dict = []
#     for elements in all_sale_dict:
#         if elements[0] == 'яблоки':
#             # my_dict.append(num1 += int(elements[1]))
#             num1 += int(elements[1])
#             # my_dict.append(elements[0])
#             # my_dict.append(num1)
#         elif elements[0] == 'апельсины':
#             num2 += int(elements[1])
#             # my_dict.append(int(elements[1]))
#         elif elements[0] == 'бананы':
#             num3 += int(elements[1])
#             # my_dict.append(int(elements[1]))
#     return my_dict


my_list = open_from_file(file)
# my_fruits_dict = my_dictionary(my_list)
my_dict = my_dictionary(my_list)
# sales = summa_sale(my_list)

file.close()
