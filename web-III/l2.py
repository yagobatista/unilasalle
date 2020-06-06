import random


def q1(product_price):
    return product_price * 0.95


def q2(salary):
    return salary * 1.15


def q3(celcius):
    return (celcius * 9) / 5 + 32


def q4(km, days):
    return 0.15 * km + 60 * days


def q5a1(name):
    return name.lower()


def q5a2(name):
    return name.upper()


def q5b(name):
    return len(name.replace(" ", ""))


def q5c(name):
    return len(name.split(" ")[0])


def q6(number):
    return list(str(number)[0:4])


def q7(guess):
    random_number = random.randrange(1, 5)
    return guess == random_number


def q8(speed):
    return (speed - 80) * 7 if speed > 80 else 0


def q9(distance):
    return distance * (0.45 if distance > 200 else 0.5)


def q10(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def q11(val1, val2, val3):
    sortedList = sorted([val1, val2, val3])
    return sortedList[-1]


def q12(salary):
    return salary * (1.1 if salary > 1250 else 1.15)


def q13(a, b, c):
    return a + b > c and a + c > b and b + c > a
