nome = 'mauricio'
idade = 36
altura = 1.85
peso = 75
ano_at = 2021
ano_nac = ano_at - idade
imc = peso / (altura ** 2)

print('{} tem {} anos de idade , sua altura é {},seu peso é {}Kg , seu imc {}'.format(nome, idade, altura, peso, imc))
print('seu ano de nascimento é {}'.format(ano_nac))
