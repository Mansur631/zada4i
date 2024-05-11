list = [-13, -1, -2, 0, 3, 5, 7, -10, 19]
words_list = [
    "яблоко", "апельсин", "банан", "груша", "виноград",
    "ананас", "манго", "киви", "персик", "слива",
    "абрикос", "черешня", "мандарин", "лимон", "гранат"
]
coordinate_list = (0,0)
numbers = (0, 1, -1, -2, 5, -10, 7, 8)
fruits_dict = {"яблоко": 3, "апельсин": 2, "банан": 5, "груша": 10,
               "виноград": 1, "ананас": 1, "манго": 7}

my_string = 'сосссоздайте программу для подсчета количества каждого символа в строке и сохраните результаты в виде словаря'


# def summa_all_list(list):
#     num1 = 0
#     for element in list:
#         if element >= 0:
#             num1 += element
#     return num1

# summa = summa_all_list(list)

# def min_max(list):
#     min_num = max_num = list[0]
#     for element in list:
#         if element > max_num:
#             max_num = element
#         if element < min_num:
#             min_num = element
#     return min_num, max_num

# my_list = min_max(list)

# def fruits(first_letter, words_list):
#     my_list = []
#     for element in words_list:
#         if first_letter == element[0]:
#             my_list.append(element)
#     return my_list
#
# fruits('ч', words_list)

# def my_coordinate(coordinate_list):
#     if coordinate_list[0] > 0 and coordinate_list[1] > 0:
#         return "1-ая четверть"
#     elif coordinate_list[0] < 0 and coordinate_list[1] > 0:
#         return '2-ая четверь'
#     elif coordinate_list[0] < 0 and coordinate_list[1] < 0:
#         return '3-ая четверть'
#     else:
#         coordinate_list[0] > 0 and coordinate_list[1] < 0
#         return '4-ая четверть'
#
# my_coord = my_coordinate(coordinate_list)
# print(my_coord)


# def modul_numbers(my_numbres):
#     my_list = []
#     for elements in my_numbres:
#         if elements < 0:
#             my_list.append(abs(elements))
#         else:
#             my_list.append(elements)
#     return tuple(my_list)
#
# my_numbers = modul_numbers(numbers)


# def all_my_fruits(my_fruits):
#     my_dict = []
#     for element in my_fruits.values():
#         my_dict.append(element)
#     return my_dict
#
# my_fruits = all_my_fruits(fruits_dict)


# def quantity_symbol(amt_sym):
#     my_dict = {}
#     for elements in amt_sym:
#         if elements in my_dict:
#             my_dict[elements[0]] += 1
#         else:
#             my_dict[elements[0]] = 1
#     return my_dict
#
# amt_sym = quantity_symbol(my_string)