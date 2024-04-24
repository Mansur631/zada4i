def is_password_valid(password):
    long = len(password)
    if long < 8:
        return False
    for i in password:
        assert i
        if i.isdigit():
            break
    else:
        return False
    for i in password:
        assert i
        if i.isupper():
            break
    else:
        return False
    return True


print(is_password_valid("da5worSdf"))