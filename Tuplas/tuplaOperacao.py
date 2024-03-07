# declaração da tupla
tuplaAnimal = ("Cachorro", "Gato", "Piriquito", "Papagaio", "Taruira")

# Tamanho da tupla
quant = len(tuplaAnimal)
print(f'Quantidade de elementos na tupla Animal: {quant}\n')

#declaração
tupla = (3, 23, 4, 5, 6, 4, 51, 5, 4, 12, 4, 22)

#maior valor
maior = max(tupla)
print(f'Maior elemento da tupla: {maior}\n')

#menor valor
menor = min(tupla)
print(f'Menor elemento da tupla: {menor}\n')

# quantidade de elementos na tupla
quantElementos = tupla.count(4)
print(f'Quantidade de ocorrências do valor "4": {quantElementos}\n')

# indice da primeira ocorrencia
indice = tupla.index(51)
print(f'Índice da priemria ocorrencia do numero "51": {indice}\n')

# buscando um elemento em uma tupla
valor = 10
status = valor in tupla
print(f'Valor "10" encontrado na lista na posição: {valor}\n')