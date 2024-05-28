# Crie um script em Python onde deverá haver um dicionário de termos, no programa o dicionário deverá receber "n" termos , cada termo poderá receber de uma ou mais definições. Crie o programa seguindo as seguintes especificações:
     # Novos termos devem ser inseridos no dicionário durante a execução do programa;
     # Novas definições dos termos devem ser adicionadas durante a execução do programa, um termo deve ter no mínimo um termo e no máximo "n" termos;
     # Um termo pode ser acessado e deve exibir todas as suas definições; 
     # O programa deve permitir a exclusão de um ou mais termos quando o usuário indicar o termo;

# dicionario vazio    
dicionario = {}

# loop para manter o programa rodando
while True:
     opcao = int(input("Escolha uma opção do menu: \n"
                       "1 - Adicionar termo e definição\n"
                       "2 - Ler os termos\n"
                       "3 - Excluir termo\n"
                       "4 - Sair\n"))
     
     # add novo termo
     if opcao == 1:
          # cada termo vai ter "n" definições
          definicoes = []
          
          # entrada do novo termo
          termo = input("Digite um termo: \n")
                    
          # loop para manter o trecho de adição de definição rodando
          while True:
               definicao = input("Digite uma definição para o termo acima: \n")
               definicoes.append(definicao)
               
               continuar = input("Deseja continuar (s/n)? ")
               print()
               if continuar.lower() == "n":
                    break
          
          # adicionando o termo e suas definições ao dicionário (chave: valor)
          dicionario[termo.lower()] = definicoes #.lower() = deixa tudo em minusculo
          print("Dicionário atualizado!")
     
     # ler termo
     elif opcao == 2:
          # mostrando os termos do dicionario
          for termo in dicionario:
               print(f"Tem-se o(s) seguinte(s) termo(s): \n"
               f"{termo}")
          
          # mostrando as definições dos termos
          leitor = input("Digite o termo cujas definições você deseja ler: \n")
          if leitor == termo:
               
               # exibição das definições
               for termo in dicionario:
                    print(f"Definições de {dicionario[termo.lower()]}: \n"
                         f"{dicionario[definicoes]}")
          
     # excluir termo
     elif opcao == 3:
          
          
     # sair
     elif opcao == 4:
          print("Poxa, já? Então, tá. Tchau!")
          break
     
     else:
          print("Essa opção não existe, digite uma opção válida.")