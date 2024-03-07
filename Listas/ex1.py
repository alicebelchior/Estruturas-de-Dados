# Crie um script em Python que deverá solicitar um número, o script deverá avaliar
# se o número informado é par ou ímpar(apresentar uma mensagem).

num = int(input("Digite um número: "))

if(num%2 == 0):
     print(f'{num} é par')
else:
     print(f'{num} é ímpar')
