# Crie um novo script e nele adicione um dicionário com as 4 notas de um aluno em diferentes disciplinas(6 disciplinas). Calcule a média das notas e imprima o resultado. O programa deve apresentar a média por disciplina e dizer se o aluno foi aprovado ou não na disciplina(aprovação para notas >= a 60 pontos).

# criando um dicionario
dici = {}

#chave (disciplina) e valores (notas de 4 provas)
dici["português"] = [60, 75, 83, 90]
dici["matemática"] = [45, 88, 79, 62]
dici["história"] = [93, 79, 35, 45]
dici["geografia"] = [85, 17, 51, 59]
dici["biologia"] = [55, 84, 66, 74]
dici["química"] = [99, 85, 74, 17]

#variaveis para obter a média
soma = 0
media = 0

for disciplina in dici:
     for nota in dici[disciplina]:
          soma += nota

#imprimindo valor da media     
for disciplina in dici:
     media = soma / 4
     print(f'\n {disciplina} - {media}')