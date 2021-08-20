"""
OPERADORES ARITIMETICOS
+ : SOMA
- : SUBTRAÇÃO
* : MULTIPLICAÇÃO
/ : DIVISÃO
// : DIVISÃO ARRENDONDADA
** : EXPONECIAÇÃO
% : MODULO / RESTO DA DIVISÃO
() :

Regra de precedencia
(n op N ),
**,
*, /, //, %,
+ , -,
"""

print('Multiplicação * : ', 10 * 10)
print('Adição + : ', 10 + 10)
print('Subtração - : ', 10 - 5)
print('Divisão / : ', 10 / 2)
print('potencia 2 : ', 2 ** 2)
print('resto da divisão/ modulo : ', 10 % 3)

# divisão arrendondada
print(10 // 3)

# utilizando multiplicação para repetição destring
print('mult string', 10 * 'rep ')

# concatenação é quando soma uma string
print('concatenação')
print('10' + '10')
print('ou')

print('mauricio' + 'Amaral')

# para concatenar numero  temos que fazer um cast
print('mauricio' + ':' + 'idade : ' + str(36))
