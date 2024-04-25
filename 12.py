amount = int(input("Цена товара: "))
nalog = int(input("Сумма налога: "))


def calculate_tax(amount, nalog):
    amount_nalog = (amount * nalog) / 100
    return amount_nalog


nalog_amount = calculate_tax(amount, nalog)


def total_with_tax(nalog_amount):
    summa = amount + nalog_amount
    return summa


print(total_with_tax(nalog_amount))
