# Crie um programa em Python que deverá utilizar funções e gravar seus dados em arquivo, o programa deverá ainda apresentar as seguintes características e funcionalidades:
# ● Exibir um menu com 3 opções:
     # ○ inserir palavra,
     # ○ Listar palavras
     # ○ Sair do programa.
# ● Ser capaz de receber uma palavra por vez;
# ● Armazenar “n” palavras em uma lista;
# ● Exibir todas as palavras armazenadas, uma palavra por linha;
# ● O programa deve gravar os dados contidos na lista no momento que for finalizado;
# ● Ao inicializar o programa deve carregar os dados gravados na última execução;
# ● As operações devem ser feitas com a utilização de funções
     # ○ Gravação
     # ○ Leitura
     # ○ Menu(opcional)

# lista de palavras vazias
lista_palavra = []

def gravacao():
     with open("palavra.txt", "w") as arquivo:
          # loop para escrever as palavras no arquivo
          for palavra in lista_palavra:
               arquivo.write(f"{palavra} \n")
     
def leitura():
     with open ("palavra.txt", "r") as arquivo:
          conteudo = arquivo.read()
          print(conteudo)          
     
def menu():
     # essa função sempre vai mostrar as opções inserir, listar ou sair
     print("1. Inserir palavra \n"
           "2. Listar palavra \n"
           "3. Sair")
     

# programa principal
while True:
     # chamando a função menu
     menu()
     opcao = int(input("Escolha uma opção: "))
     
     # add palavra
     if opcao == 1:
          print("-" *20)
          palavra = input("Digite uma palavra: \n")
          lista_palavra.append(palavra)
          print("Palavra adicionada! \n")
     
     # listar palavra   
     elif opcao == 2:
          print("-" *20)
          print("Tem-se gravadas as seguintes palavras:")
          for palavra in lista_palavra:
               print(f"{palavra}")
          print()
          
     # sair  
     elif opcao == 3:
          # gravar os dados contidos na lista no momento que for finalizado
          gravacao()
          print("Já deu, então, né? Tchau. \n")
          break
          
     else:
          print("Essa opção não existe, digite uma opção válida.")

print("Programa encerrado \n")
# chamando a função leitura pra mostrar o arquivo
leitura() 