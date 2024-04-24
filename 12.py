def calculate_tax():
    amount = 95
    nalog = 16
    amount_nalog = (amount * nalog)/100
    total_with_tax(amount, nalog, amount_nalog)


def total_with_tax(some_amount, some_nalog, some_amount_nalog):
    total = some_amount + some_amount_nalog
    print(total)


calculate_tax()