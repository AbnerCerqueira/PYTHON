#Leia a idade de uma pessoa em anos calcule e exiba
#ela em meses, dias e horario(considere que todos os meses tem 30 dias

idade = int(input('Digite sua idade\n'))

mes = idade*12
dias = mes*30
horas = dias*24

print(f'Você viveu {mes} meses {dias} dias e {horas}horas')