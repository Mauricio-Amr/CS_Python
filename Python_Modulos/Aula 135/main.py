import os
import shutil

caminho_original = '/home/mauricio/Development/CS_Python/Python_Modulos/Aula 135/original'
caminho_novo = '/home/mauricio/Development/CS_Python/Python_Modulos/Aula 135/Novo'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} ja existe.')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        print(files)
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        # print(old_file_path)
        if '.deb' in file:
            #shutil.move(old_file_path, new_file_path)
            #shutil.copy(old_file_path, new_file_path)
            #print(f'Arquivo {file} movido com sucesso !')
            os.remove(new_file_path)
            print(f'file {file} removido')
