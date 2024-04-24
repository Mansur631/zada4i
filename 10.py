def is_full_price(age):
    full_price = True
    small_price = False
    if age <= 18:
        return small_price
    else:
        return full_price


print(is_full_price(19))