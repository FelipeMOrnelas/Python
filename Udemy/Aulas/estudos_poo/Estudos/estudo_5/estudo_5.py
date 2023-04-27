from classes import Escritor
from classes import Caneta
from classes import MaquinadeEscrever

escritor = Escritor('Felipe')
maquina = MaquinadeEscrever()
caneta = Caneta('Bic')

escritor.ferramenta = caneta
escritor.ferramenta.escrever()


