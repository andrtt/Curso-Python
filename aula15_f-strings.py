import math

nome = input ('Digite seu nome:')
idade = int(input ('Digite sua idade:'))
altura = float(input('Digite sua altura:')) 
peso = float(input('Digite o seu peso:'))

# Cálculo do IMC
imc = peso / altura**2

# formatação de string ( F-String)
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

# Cálculo do IMC
imc = peso / altura**2

# Fórmula de Mosteller (Superficie Corporal)
altura_cm = altura*100
m2_corporal = math.sqrt((altura_cm * peso) / 3600)

# Análise do IMC
if imc < 18.5:
    categoria = 'baixo peso'
elif 18.5 <= imc <= 24.9: 
    categoria = 'peso adequado'
elif 25 <= imc <= 29.9: 
    categoria = 'sobrepeso'
elif 30 <= imc <= 34.9: 
    categoria = 'obesidade grau I'
elif 35 <= imc <= 39.9: 
    categoria = 'obesidade grau II'
else: 
    categoria = 'obesidade grau III'

print(linha_1)
print(linha_2)
print (linha_3)