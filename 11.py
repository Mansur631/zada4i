def convert_to_celsius(temp_farengate):
    temp_celsius = 5 / 9 * (temp_farengate - 32)
    return temp_celsius


def is_freezing(temp):
    if temp < 0:
        return True
    else:
        return False


temp_cels = convert_to_celsius(100)
print(is_freezing(temp_cels))