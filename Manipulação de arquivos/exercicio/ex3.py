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

import json

# dicionario vazio para "n" termos
dicionario_termo = {}

def gravacao():
     with open("dicionario.json", "w") as arquivo:
          for termo in dicionario_termo:
               # loop para escrever os termos no arquivo
               json.dump(dicionario_termo, arquivo)
          
def leitura():
     with open("dicionario.json", "r") as arquivo:
          dicionario_termo = json.load(arquivo)

def menu():
     print("1. Inserir número\n"
           "2. Listar número \n"
           "3. Exibir cálculos \n"
           "4. Sair")