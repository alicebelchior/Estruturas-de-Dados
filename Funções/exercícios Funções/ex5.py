# Escreva um script em Python para simular o funcionamento de uma lâmpada, nesse programa o usuário poderá ligar e desligar a lâmpada, o programa deverá informar se a lâmpada está ligada ou desligada. Monte este programa utilizando funções.

# originalmente a lampada estara desligada
lampada_ligada = False

# lampada ligada
def lamp_on():
     lampada_ligada
     lampada_ligada = True
     
     
# lampada desligada
def lamp_off():
     lampada_ligada
     lampada_ligada = False
     
# verificar estado da lampada
def verif_lamp():
     if lampada_ligada:
          print("A lâmpada está ligada\n")
     else:
          print("A lâmpada está desligada\n")

# loop para ligar/desligar/verificar a lampada
while True:
     escolha = int(input('Selecione uma opção:\n'
          '1. Ligar\n'
          '2. Desligar\n'
          '3. Verificar\n'))
     
     if escolha == 1:
          lamp_on()
     elif escolha == 2:
          lamp_off
     elif escolha == 3:
          verif_lamp()
     else:
          print("Opçã errada, otário")
          break
          