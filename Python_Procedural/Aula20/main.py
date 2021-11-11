
file = open('abc.txt','w+')#abre o arquivo em forma leitura escrita
file.write('linha 1\n')
file.write('linha 2\n') #escreve no arquivo
file.write('linha 3\n')

#--------leitura de arquivo--------
file.seek(0,0)#move o cursor para o  incio do arquivo para fazer a leitura
print('LENDO ARQUIVO ...')
print(file.read())

#---------ler linha por linha
print('############')
file.seek(0,0)
print(file.readline() , end='') #le uma linha
print(file.readline() , end='')
print(file.readline() , end='')



print('############')

file.seek(0,0)
print(file.readlines()) #le todas as linhas e coloca em lista
print ('-'*30)

file.seek(0,0) #sempre retorne o cursor
for linha in file.readlines():
    print(linha, end='')


file.close()
