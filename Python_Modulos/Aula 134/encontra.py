from ctypes.wintypes import tagMSG
import os

caminho_procura = input('Digite um caminho : ')
termo_procura = input('Digite um termo : ')


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        tamanho = base
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'p'

    tamanho = round(tamanho, 2)
    return f'{tamanho} {texto}'


for raiz, diretorio, arquivos in os.walk(caminho_procura):
    # print(arquivos)
    conta = 0
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta = + 1
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
                print('Tamanho formatado:', formata_tamanho(tamanho_arquivo))
            except PermissionError as e:
                print('Sem permissões.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido : ', e)
print()
print(f'{conta} arquivo(s) encontrado(s). ', replace('.', ','))
