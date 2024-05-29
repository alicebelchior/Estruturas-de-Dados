# serve para complementar um arquivo existente
# "a" = modo adição e uma linha é adicionada ao final do arquivo
with open("exemplo.txt", "a") as arquivo:
     arquivo.write("\nEsta linha foi adicionada depois da primeira")

# "w" = modo escrita, o que apaga qualquer conteúdo anterior e escreve novas linhas
with open("exemplo.txt", "w") as arquivo:
     # escreve no arquivo
     arquivo.write("\nBom dia!")
     arquivo.write("\nEu sou um arquivo de teste!")
     arquivo.write("\nblá, blá, blá!")

# "r" = modo leitura e todo o conteúdo atual é lido e impresso    
with open("exemplo.txt", "r") as arquivo:
     # lê todo o conteudo do arquivo
     conteudo = arquivo.read()
     print(conteudo)