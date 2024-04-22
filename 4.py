def is_bulk_purchase(num):
    if num >= 100:
        return True
    else:
        return False


print(is_bulk_purchase(11))
