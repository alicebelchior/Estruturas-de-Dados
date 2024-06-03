# Crie um programa em Python que deverá utilizar funções e gravar seus dados em arquivo, o programa deverá ainda apresentar as seguintes características e funcionalidades:
# ● Exibir um menu com 4 opções:
     # ○ inserir número,
     # ○ Listar números
     # ○ Exibir Cálculos
     # ○ Sair do programa.
# ● Ser capaz de receber um número por vez;
# ● Armazenar “n” números em uma lista;
# ● Exibir todos os números armazenados, um número por linha;
# ● Apresentar os cálculos com os números digitados:
     # ○ Média aritmética;
     # ○ Identificar o maior número da lista;
     # ○ Identificar o menor número da lista;
     # ○ Fazer a somatória dos número armazenados.
# ● O programa deve gravar os dados contidos na lista no momento que for finalizado;
# ● Ao inicializar o programa deve carregar os dados gravados na última execução;
# ● As operações devem ser feitas com a utilização de funções
     # ○ Gravação
     # ○ Leitura
     # ○ Cálculos
     # ○ Menu(opcional)
     
import pickle

# lista de "n" numeros
lista_numeros = []

def gravacao():
     with open("numero.pkl", "wb") as arquivo:
          pickle.dump(lista_numeros, arquivo)
          
def leitura():
     with open("neumero.pkl", "rb") as arquivo:
          pickle.load(arquivo)
          
def exibir_calculo():
     # somatorio
     if lista_numeros == []:
          print("Lista vazia!")
     else:
          soma = sum(lista_numeros)
          print(f"O somatório dos números da lista é {soma}")
     
     # media aritmetica
     if lista_numeros == []:
          print("Lista vazia!")
     else:
          media = soma / len(lista_numeros)
          print(f"A média aritmética da lista é {media}")
     
     # maior numero
     if lista_numeros == []:
          print("Lista vazia!")
     else:
          maior = max(lista_numeros)
          print(f"O maior número da lista é {maior}")
     
     # menor numero
     if lista_numeros == []:
          print("Lista vazia!")
     else:
          menor = min(lista_numeros)
          print(f"O menor número da lista é {menor}")

def menu():
     print("1. Inserir número\n"
           "2. Listar número \n"
           "3. Exibir cálculos \n"
           "4. Sair")

# programa principal
while True:
     menu()
     opcao = int(input("Escolha uma opção: "))
     
     # add numero
     if opcao == 1:
          while True:
               print("-" *20)
               numero = int(input("Digite um número ou '0' pra sair:"))
               if numero == 0:
                    break
               else:
                    lista_numeros.append(numero)
                    print("Número adicionado! \n")  
          
     # listar numero 
     elif opcao == 2:
          print("-" *20)
          print("Tem-se gravados os seguintes números:")
          for numero in lista_numeros:
               print(f"{numero}")
          print()
          
     # exibir calculos 
     elif opcao == 3:
          exibir_calculo()
          print()
          
     # sair  
     elif opcao == 4:
          gravacao()
          print("Já deu, então, né? Tchau. \n")
          break
     
     else:
          print("Essa opção não existe, digite uma opção válida.")

print("Programa encerrado \n")
# chamando a função leitura pra mostrar o arquivo
leitura() 