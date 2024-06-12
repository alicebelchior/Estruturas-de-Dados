# Crie um programa em Python que deverá utilizar funções e gravar seus dados em arquivo, o programa deverá ainda apresentar as seguintes características e funcionalidades:
# ● Exibir um menu com as seguintes opções:
     # ○ inserir Termo(cada termo deve ter 2 atributos)
     # ○ Listar Termos.
     # ○ Sair do programa.
# ● Ser capaz de receber um termo por vez;
# ● Armazenar “n” termos no dicionário;
# ● Exibir todos os termos e atributos quando for solicitado(fazer de forma organizada).
# ● O programa deve gravar os dados no momento que for finalizado;
# ● Ao inicializar o programa deve carregar os dados gravados na última execução;
# ● As operações devem ser feitas com a utilização de funções

# "a" = modo adição e uma linha é adicionada ao final do arquivo
with open("dicionario.txt", "a") as arquivo:
     arquivo.write("\nEsta linha foi adicionada depois da primeira")

# dicionario vazio para "n" termos
dicionario_termo = {}

def gravacao():
     with open("dicionario.txt", "w") as arquivo:
          # loop para escrever as palavras no arquivo
          for termo in dicionario_termo:
               arquivo.write(f"{termo}, 1º atributo: {atributo_1}, 2º atributo: {atributo_2} \n")
          
def leitura():
     with open ("dicionario.txt", "r") as arquivo:
          conteudo = arquivo.read()
          print(conteudo) 

def menu():
     print("1. Inserir termo\n"
           "2. Listar termo \n"
           "3. Sair")

leitura()

#programa principal 
while True:
     menu()
     opcao = int(input("Escolha uma opção: "))
     
     #add termo e atributo
     if opcao == 1:
          print("-" *20)
          termo = input("Digite o termo: ")
          atributo_1 = input("Digite o primeiro atributo: ")
          atributo_2 = input("Digite o segundo atributo: ")
          dicionario_termo[termo] = {"1º atributo": atributo_1, "2º atributo": atributo_2}
          print("Termo e atibutos adicionados! \n")

     # LISTAR
     elif opcao == 2:
          print("-" *20)
          print("Tem-se gravados os seguintes termos:")
          print(dicionario_termo.items())
          #.items() retorna uma visualização dos itens do dicionário
          
     # SAIR
     elif opcao == 3:
          gravacao()
          print("Já deu, então, né? Tchau. \n")
          break

     else:
          print("Essa opção não existe, digite uma opção válida.")

print("Programa encerrado! \n")


# REFAZER EM SEM JSON