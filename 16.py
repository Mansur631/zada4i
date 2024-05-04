file = open('students.txt', 'r')


def read_from_file(file):
    files = file.read()
    my_list = []
    for row in files.split('\n'):
        my_list.append(tuple(row.split(',')))
    return my_list


def is_adult(age):
    return int(age) >= 18


def filter_adults(my_list):
    new_my_list = []
    for elements in my_list[1:]:
        if is_adult(elements[1]):
            new_my_list.append(elements)
    return new_my_list


my_list = read_from_file(file)
big_age = filter_adults(my_list)
print(big_age)

file.close()
