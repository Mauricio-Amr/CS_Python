'''
Manipulando Strings
*String indice
*Fatiamento de string [inicio: fim :passo]
*Função Built-in len , abs, type, print, etc ...
essas funçoes podem ser usadas diretamente em cada tipo.

https://docs.python.org/3.9/library/stdtypes.html
https://docs.python.org/3.9/library/functions.html
'''
#pos     [01245678]
texto = 'python s2'
#neg     [987654321]

print(texto[-4])

url = 'www.google.com.br/'

print(url[:-9])

nova_str = texto[:5]
print(nova_str)


nova_str2 = texto[0::3]
print(nova_str2)

print ('len : ', len(texto))