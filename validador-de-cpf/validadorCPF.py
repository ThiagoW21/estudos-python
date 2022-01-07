CPF = input('Digite o CPF (com pontos e hífen): ')
cpf = CPF.split('-')[0]


def digito(n):
    soma = 0
    cont = 10 if len(n) == 11 else 11

    for num in n:
        if num == '.':
            continue
        soma += int(num) * cont
        cont -= 1
    digito = 11 - (soma % 11)

    return 0 if digito > 9 else digito

primeiro = str(digito(cpf))
segundo = str(digito(cpf + primeiro))
cpf  += '-' + primeiro + segundo

if cpf == CPF:
    print('CPF válido!')
else:
    print('CPF inválido!')