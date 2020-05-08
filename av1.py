def q1():
    number = int(input("Digite o valor:"))
    output = ""

    if number > 10:
        output = "Número fora do Intervalo"
    elif number % 2 == 0:
        output = "Número par menor que Dez"
    else:
        output = "Número Ímpar menor que Dez"

    print(output)


def q2():
    alunos = []
    while True:
        ler_aluno = input("Ler aluno (y/n):")
        if ler_aluno != "y":
            break

        nome = input("Digite o nome do aluno:")
        n1 = float(input("Digite o nome do nota 1:"))
        n2 = float(input("Digite o nome do nota 2:"))

        alunos.append([nome, n1, n2])

    for aluno in alunos:
        nome, n1, n2 = aluno
        print("Nome: {}, média: {}".format(nome, (n1 + n2) / 2))

    while True:
        ler_aluno = input("Deseja consultar um aluno especifico (y/n):")
        if ler_aluno != "y":
            break

        qtd_alunos = len(alunos)
        index = int(
            input(
                "Temos {} alunos, escolha a posição do aluno de 0, {}:".format(
                    qtd_alunos, qtd_alunos - 1
                )
            )
        )
        if index > qtd_alunos - 1 or index < 0:
            print("Número escolhido é inválido")
            continue

        nome, n1, n2 = alunos[index]
        print("O aluno {} obteve primeira nota igual a {} e segunda igual a {}".format(nome, n1, n2))


def q3():
    pes = int(input("Número desejado em pés: "))
    polegadas = pes * 12
    jardas = pes / 3
    milhas = jardas / 1760

    print("{} polegadas, {} jardas e {} milhas".format(polegadas, jardas, milhas))


def q4():
    funcionarios = []
    while True:
        ler_aluno = input("Ler funcionário (y/n):")
        if ler_aluno != "y":
            break

        codigo = input("Digite o código do funcionário:")
        horas = float(input("Horas trabalhadas:"))
        dependentes = int(input("Digite o numero de dependentes:"))

        funcionarios.append([codigo, horas, dependentes])

    for funcionario in funcionarios:
        codigo, horas, dependentes = funcionario

        salario_bruto = (horas * 12) + (40 * dependentes)

        desconto_inss = salario_bruto * 0.085
        desconto_ir = salario_bruto * 0.05

        salario_liquido = salario_bruto - desconto_inss - desconto_ir

        print(
            """ 
            código do funcionário: {}, 
            descontado do inss: {},
            desconto do imposto de renda: {}
            salário líquido: {}
            """.format(
                codigo, desconto_inss, desconto_ir, salario_liquido
            )
        )
