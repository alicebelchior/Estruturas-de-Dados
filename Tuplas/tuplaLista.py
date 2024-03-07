# Declaração da tupla
tuplaAnimal = ("Cachorro", "Gato", "Piriquito", "Papagaio", "Taruira")

#tupla antes da modificação
print(f'Tupla antes da modificação: {tuplaAnimal}')

#convertendo tupla -> lista
listaTupla = list(tuplaAnimal)

#modificando a lista
listaTupla.append("Tigre")
listaTupla[4] = "Iguana"

#lista -> tupla
novaTupla = tuple(listaTupla)
print(f'Tupla depois da alteração: {novaTupla} \n')