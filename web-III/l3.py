import math as m


def q14(i, a, b, c):
    choice = int(i)
    if choice not in [1, 2, 3]:
        return

    order = False if choice == 1 else True
    values = sorted([a, b, c], reverse=order)

    if choice == 3:
        bigger_value = values[0]
        values[0] = values[1]
        values[1] = bigger_value

    return values


def q15(price, radius, height):
    area = 2 * 3.1415 * radius * (radius + height)
    ink_necessary = area / 3

    return ink_necessary * price


def q16(car_value, items_code=''):
    items_total_price = 0
    items_prices = {
        'a': 1750,
        'b': 800,
        'c': 1200,
        'd': 2000,
    }

    for item in set(items_code):
        items_total_price += items_prices.get(item)
    
    return car_value + items_total_price


def q17(value):
    number = str(int(value))
    division = m.floor(len(number) / 2)
    return number[division:] == number[:division]


def q18(installment, fee):
    interest = installment + (installment * fee / 100)

    return installment - interest


def q19(radius, height):
    3.1415 * pow(radius, 2) * height


def q20(grade1, grade2, grade3):
    return 0.3 * grade1 + 0.2 * grade2 + 0.5 * grade3

print(q17('454'))
