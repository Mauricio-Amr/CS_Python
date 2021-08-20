"""
TIPOS DE DADOS
str - string - texto "Assim" ou 'Assim'
int - inteiro - numero reais - 123456 , 0 , -10 -20 ...
float - Real / flutuante - numero  com virgula  - 10.25, 0.50 , -10.10 , 0.0 ...
bool - booleano / lógico - True/ False
"""

print('mauricio', type('mauricio'))
print(10, type(10))
print(3.1416, type(3.1416))
print(10 == 10, type(10 == 10))

#type cast
print ('Mauricio', type('Mauricio'), bool('mauricio'))
print ('100 ', type('100'), type(int('100')))

#type cast q não funciona
#print ('mauricio', type(int('mauricio')))
#print ('10.53', type(int(10.53)))


#string : nome
print('Mauircio', type('Mauricio'))

#inteiro :idade
print(36 , type(36))

#float : Altura
print(1.85, type(1.85))

#Bool : é maior de idade
print(36> 18, type(36>18))