
# with open('abc.txt','w+') as file:
#     file.write("Linha 1\n")
#     file.write("Linha 2\n")
#     file.write("Linha 3\n")
#
#     file.seek(0)
#     print(file.read())
#

#
# with open('abc.txt','r') as file:
#     print(file.read())



with open('abc.txt','a+') as file:
    file.write("outra linha")
    file.seek(0)
    print(file.read())

# #remover o arquivo criado import os
import os
# os.remove('abc.txt')
