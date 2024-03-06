lista = ["Mateus", "Marcos", "Lucas", "João", "Pedro", "Tomé", "Tiago", "Judas"]

#print(lista)
#print(f"Valor da posição 4: {lista[4]}")
for nome in lista:
    print(nome)
print()

for numero in range(10):
     print(numero)     
print()

for numero in range(8):
    print(f'Posição: {numero+1} - {lista[numero]}')
print()
    
lista.append("Maria Madalena")

print(lista)
print()

lista.remove("Judas")
for numero in range(8):
    print(f'Posição: {numero+1} - {lista[numero]}')
print()