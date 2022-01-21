from classe import Escritor
from classe import Caneta
from classe import MaquinaDeEscrever

escritor = Escritor('Mauricio')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()


#associação

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
