file = open('students.txt', 'r')


def read_from_file(file):
    files = file.read()
    my_list = []
    for row in files.split('\n'):
        my_list.append(tuple(row.split(',')))
    return my_list


def is_adult(age):
    return int(age) >= 18


def filter_adults(my_list_age):
    new_my_list_age = []
    for elements in my_list_age[1:]:
        if is_adult(elements[1]):
            new_my_list_age.append(elements)
    return new_my_list_age


def count_high_grades(my_list_grade):
    new_list_grade = []
    for student in my_list_grade[1:]:
        if int(student[2]) >= 80:
            new_list_grade.append(student)
    return len(new_list_grade)



my_list = read_from_file(file)
big_age = filter_adults(my_list)
student_grade = count_high_grades(my_list)

file.close()