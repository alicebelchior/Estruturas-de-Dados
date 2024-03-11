# Crie um dicionário com as informações de livros, incluindo título, autor, ano de publicação e número de páginas. O dicionário deve armazenar dados de no mínimo 5 livros.
# a.	Faça com que o script liste os dados armazenados no dicionário de livros;
# b.	Adicione os dados de mais 2 livros ao dicionário;
# c.	Modifique o autor do segundo livro do dicionário;
# d.	Percorra o dicionário e imprima todas as chaves e valores.
# e.	Busque o nome de um determinado autor no dicionário(solicite o nome para busca ao usuário);

# criando um dicionario
dici = {}

# add chaves e valores
dici["titulo"] = ["Eu sou o mensageiro", "Crepúculo", "A revolução dos bichos", "Azul é a cor mais quente", "Persépolis"]
dici["autor"] = ["Markus Zusak", "Stephenie Meyer", "George Orwell", "Julie Maroh", "Marjane Satrapi"]
dici["ano"] = [2002, 2005, 1945, 2010, 2000]
dici["páginas"] = [320, 480, 152, 160, 352]

# listando os dados armazenados
for chave in dici:
     print(f'\n {chave} - {dici[chave]}')

print('\n\n')
    
# adicionando dois livros
# livro 1
dici["titulo"].append("Casos de Família")
dici["autor"].append("Ilana Casoy")
dici["ano"].append(2016)
dici["páginas"].append(528)

# livro 2
dici["titulo"].append("Meu amigo Dahmer")
dici["autor"].append("Derf Beckderf")
dici["ano"].append(2012)
dici["páginas"].append(288)

# modificando o autor do 2º livro
dici["autor"][1] = "Anne Rice"
for chave in dici:
     print(f'\n {chave} - {dici[chave]}')
        
# imprimindo chaves e valores
for chave in dici:
     print(f'\n{chave}')
     for valor in dici[chave]:
          print(f'  - {valor}')
          
