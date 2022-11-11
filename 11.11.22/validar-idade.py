#pergunte a idade do usuário, se ele for menor de idade, não libere o acesso
confirma = 1

while confirma == 1:
    idade = int(input('Digite sua idade: '))
    if idade<18:
        print('Menor de idade, bloqueado')
        confirma = int(input('Quer tentar novamente?\n1-Sim\n2-Não\n'))
    else:
        print('Acesso liberado')
        confirma += 1