from classe import Cliente , Enderecos

cliente1 = Cliente('Mauricio', 36)
cliente1.insere_enderecos('São Paulo ', 'sp')
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Joao', 32)
cliente2.insere_enderecos('Minas Gerais', 'Mg')
cliente2.lista_enderecos()
print()
