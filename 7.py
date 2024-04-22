def is_divisible(num1, num2):
    summa = num1 / num2
    if summa % 1 == 0:
        return True
    else:
        return False


print(is_divisible(11, 3))
