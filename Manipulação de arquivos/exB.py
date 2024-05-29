import pickle

# PROCESSO DE GRAVAÇÃO EM ARQUIVO DE UMA LISTA
# Lista de origem usada no exemplo
listaNumerosOrigem = [1, 2, 3, 4, 5]

# Grava a lista em um arquivo chamado "lista.pkl"
# wb = writing binary - Manipulação de Arquivos Binários
with open("lista.xyz","wb") as arquivo:
     pickle.dump(listaNumerosOrigem, arquivo)
     # A variável "arquivo" é um objeto que representa o arq físico
     
# PROCESSO DE LEITURA EM ARQUIVO DE UMA LISTA
# Lista de destino, que está vazia
listaNumerosDestino = []

# Abre o arquivo "lista.pkl" para leitura
# wb = reading binary - Manipulação de Arquivos Binários
with open("lista.xyz", "rb") as arquivo:
     # Carrega os dados do arquivo listaNumerosOrigem para a listaNumerosDestino
     listaNumerosDestino = pickle.load(arquivo)
          # A variável "arquivo" é um objeto que representa o arquivo físico
          
# Exibe a lista lida no arquivo
print(listaNumerosDestino)