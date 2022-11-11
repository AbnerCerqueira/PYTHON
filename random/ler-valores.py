#Leia 10 valores e exiba quantos são
#menores que zero

negativo = 0
positivo = 0
zeros = 0
cont = 1
while cont < 11:
    valor = int(input(f'Digite o {cont}º número: '))
    cont += 1
    if valor<=-1:
        negativo += 1
    elif valor == 0:
        zeros += 1
    else:
        positivo += 1
        

    print (f'Números negativos: {negativo}\nNúmeros positivos: {positivo}\nZeros: {zeros}')