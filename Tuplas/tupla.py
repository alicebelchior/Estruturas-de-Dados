#Tuplas são como as Listas, porém elas usam parenteses
tupla = ()
print(tupla)
print(type(()))
print(type(tupla))

tupla = (1,2,3)
print(tupla)

print(tupla[0])
print(tupla[1])

# tuplas é uma "lista fechada" (completamente imutável), não permite adição, remoção ou alteração de elementos
# é útil para dados fixos
# tupla.append(4)
# tupla[1] = 4
# tupla[2] = 5