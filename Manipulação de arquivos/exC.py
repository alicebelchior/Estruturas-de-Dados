import json

# dicionario de exemplo
pessoa = {
     "nome": "Ana",
     "idade": 25,
     "cidade": "São Paulo"
}

# PROCESSO DE GRAVAÇÃO DE DICIONÁRIO EM ARQUIVO
# Grava o dicionário em um arquivo chamado "dicionario.json"
with open("dic01.json", "w") as arquivo:
     # Faz a união do dicionario com o objeto arquivo
     json.dump(pessoa, arquivo)
     
# PROCESSO DE LEITURA DE DICIONÁRIO EM ARQUIVO
# Inicializa um dicionário vazio para guardar os dados recebidos
dadosRecebidos = {}

# Abre o arquivo "dicionario.json" para leitura
with open("dic01.json", "r") as arquivo:
     # Carrega os dados do arquivo para o "dicionario_lido"
     dicionario_lido = json.load(arquivo)

# exivir o dicionario lido do arquivo
print(dicionario_lido)