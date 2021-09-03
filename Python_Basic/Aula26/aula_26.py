"""
Inversão de variaveis
"""

#metodo comum

x = 10
y = 5

z=x
x=y
y=z

print(f'x = {x} , y = {y}')


#metodo python

x,y = y,x
print(f'x = {x} , y = {y}')


m = 'mauricio'
k = 'kira'
d = 'dick'

print (m, k , d )

m, k, d = d, m, k
print (m, k, d)