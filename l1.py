import math


def q1(integer):
    return 'Número {}, sucessor {}, antecessor {}'.format(
        integer,
        integer + 1,
        integer - 1,
    )


def q2(number):
    return 'Número {}, dobro {}, triplo {}, raiz quadrada {}'.format(
        number,
        number * 2,
        number * 3,
        math.sqrt(number),
    )


def q3(meters):
    return 'Metros {}, centimetros {}, milimetros {}'.format(
        meters,
        meters * 100,
        meters * 1000,
    )


def q4(integer):
    tabuada = [
        '{} x {} = {}'.format(
            integer,
            i,
            integer * i,
        ) for i in range(1, 10)
    ]
    return '\n'.join(tabuada)


def q5(money):
    return 'Dinheiro em real {}, em dólares {}'.format(
        money,
        money / 4.20,
    )


def q6(height,  width):
    area = height * width
    return 'Área {} m², quantidade de tinta necessária {} L'.format(
        area,
        area / 2,
    )


if __name__ == "__main__":
    while True:
        exercise = int(input('escolha um exercicios(1,2,3,4,5,6):'))
        if exercise > 6 or exercise < 1:
            break
        func = globals()['q{}'.format(exercise)]

        if exercise == 6:
            height = float(input('Escolha um altura:'))
            width = float(input('Esolha uma largura:'))
            print(func(height, width))
        else: 
            number = float(input('Escolha um numero:'))
            print(func(number))