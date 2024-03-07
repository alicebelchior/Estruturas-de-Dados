# Em Python crie uma lista para armazenar 3 números inteiros, o script deverá
# permitir ao usuário inserir 2 novos números na lista já existente, após essa
# etapa o programa deverá exibir o conteúdo da lista

#criação da lista 
lista = [1,2,3]

# inserção de novos numeros
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

# adição desses numeros na lista
lista.append(num1)
lista.append(num2)

# exibição da lista atualizada
print(lista)