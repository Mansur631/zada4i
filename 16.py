file = open('students.txt', 'r')


def read_from_file(file):
    files = file.read()
    my_list = []
    for row in files.split('\n'):
        my_list.append(tuple(row.split(',')))
    return my_list


print(read_from_file(file))


file.close()
