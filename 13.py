list_category = ["Ребенок", "Подросток", "Взрослый"]
child = ["1", "2", "3", "4"]
young = ["5", "6", "7", "8"]
old = ["9", "10", "11", "12"]


def age_category(age):
    if age <= 14:
        return list_category[0]
    if 15 <= age <= 30:
        return list_category[1]
    if age >= 31:
        return list_category[2]


def recommended_sports(your_age):
    if list_category[0] == your_age:
        return child
    elif list_category[1] == your_age:
        return young
    elif list_category[2] == your_age:
        return old


your_age = age_category(30)

print(recommended_sports(your_age))
