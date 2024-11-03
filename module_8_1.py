def add_everything_up(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b


    elif isinstance(a, str) or isinstance(b, str):
        return str(a) + str(b)

    else:
        raise TypeError("Не могу сложить данные разных типов")


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
