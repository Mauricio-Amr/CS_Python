from ctypes.wintypes import tagMSG
import os

caminho_procura = '/home/mauricio/Downloads/teste'
termo_procura = 'google'

for raiz, diretorio, arquivos in os.walk(caminho_procura):
    # print(arquivos)
    for arquivo in arquivos:
        if termo_procura in arquivo:
            caminho_completo = os.path.join(raiz, arquivo)
            nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
            tamanho_arquivo = os.path.getsize(caminho_completo)

            """print(nome_arquivo, ext_arquivo, sep='---')
            print(tamanho_arquivo)"""

            print()
            print('Encontrei o  arquivo : ', arquivo)
            print('Caminho : ', caminho_completo)
            print('Nome : ', nome_arquivo)
            print('Extensão : ', ext_arquivo)
            print('Tamanho :', tamanho_arquivo)
