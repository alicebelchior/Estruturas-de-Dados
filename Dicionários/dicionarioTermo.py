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
          print("Dicionário atualizado! \n")
     
     # ler termo
     elif opcao == 2:
          # mostrando os termos do dicionario
          print("Tem-se o(s) seguinte(s) termo(s):")
          for termo in dicionario:
               print(f"{termo}")
          
          # mostrando as definições dos termos
          leitor = input("Digite o termo cujas definições você deseja ler: \n")
          
          #verificando se o termo existe no dicionario
          if leitor.lower() in dicionario:
               # se existir, o termo é recuperado do dicionario pela var
               definicoes = dicionario[leitor.lower()]
               print(f"As definições do termo {leitor} são")
               
               # exibição das definições
               for definicao in definicoes:
                    print(f" - {definicao}")
          else:
               print("Essa palavra não existe no dicionário \n")
          print()
          
     # excluir termo
     elif opcao == 3:
          # mostrando os termos do dicionario
          print("Tem-se o(s) seguinte(s) termo(s):")
          for termo in dicionario:
               print(f"{termo}")
          
          # mostrando os termos que se quer excluir
          leitor = input("Digite o termo que você gostaria de excluir: \n")
          
          #verificando se o termo existe no dicionario
          if leitor.lower() in dicionario:
               del dicionario[leitor.lower()]
               print(f"O termo {leitor} foi excluído com sucesso! \n")
          else: 
               print("Essa palavra não existe no dicionário \n")
          
     # sair
     elif opcao == 4:
          print("Poxa, já? Então, tá. Tchau!")
          break
     
     else:
          print("Essa opção não existe, digite uma opção válida.")