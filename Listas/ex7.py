# Em Python crie uma lista para armazenar 5 números inteiros, o script deverá
# exibir a somatória dos números armazenados.

# criação da lista
lista = []
soma = 0

# entrada de dados
for numero in range(5):
    numero = int(input("Digite um número: "))
    lista.append(numero)

# somatorio dos numeros da lista
for numero in lista:
    soma = numero + soma

# saida de dados    
print(soma)