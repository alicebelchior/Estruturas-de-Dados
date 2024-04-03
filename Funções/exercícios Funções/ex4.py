#  Escreva um script em Python para a construção de uma calculadora, essa deverá permitir ao usuário realizar operações de soma, subtração, multiplicação e divisão. Utilize funções, uma função para cada operação

# adição
def add(a, b):
     return a + b

# subtração
def sub(a, b):
     return a - b

# multiplicação
def mult(a, b):
     return a * b

# divisao
def div(a, b):
     return a / b

# loop para continuar na calculadora
while True:
     #  opções de operação
     print('Selecione uma operação:')
     operacao = int(input(
          '1. Adição\n'
          '2. Subtração\n'
          '3. Mutiplicação\n'
          '4. Divisão\n'))

     # entrada de dados
     a = int(input('Digite o primeiro numero: '))
     b = int(input('Digite o segundo numero: '))

     # condição para as operações
     if operacao == 1:
          print(f'{a} + {b} = {add(a, b)}')
     elif operacao == 2:
          print(f'{a} - {b} = {sub(a, b)}')
     elif operacao == 3:
          print(f'{a} x {b} = {mult(a, b)}')
     elif operacao == 4:
          print(f'{a} / {b} = {div(a, b)}')
     
     # verificar se o usuario quer continuar
     continuar = (input('Deseja continuar(s/n): '))
     print()
     if (continuar == 'n'):
          break