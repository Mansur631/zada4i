def point_to_grade(amount_grade):
    if amount_grade >= 100:
        return "A"
    if amount_grade >= 80:
        return "B"
    if amount_grade >= 60:
        return "C"
    if amount_grade >= 40:
        return "D"


def grade_description(grade):
    if grade == "A":
        return "Nice"
    if grade == "B":
        return "Good"
    if grade == "C":
        return "Normal"
    if grade == "D":
        return "Bad"


grade = point_to_grade(99)
print(grade_description(grade))


