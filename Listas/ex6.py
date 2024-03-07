# Em Python crie uma lista para armazenar 6 números reais, o script deverá
# buscar um valor entre os valores armazenados, após essa etapa o programa
# deverá exibir a mensagem “O valor foi encontrado!” ou “O valor não foi
# encontrado”

#  criação da lista vazia
lista = []

# entrada de dados
for numero in range(6):
    numero = int(input("Digite um número: "))
    lista.append(numero)  #cada numero digitado sera adicionado dentro da lista vazia

# verificando se existe um numero inserido na lista
if 30 in lista:
    print(f'O valor foi encontrado')
else:
    print(f'O valor não foi encontrado')