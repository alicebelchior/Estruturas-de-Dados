# Crie um programa gerador de tabuadas, o programa deverá solicitar qual tabuada deverá ser criada e uma função deverá criar a tabuada indicada.

# definindo função tabuada que receberá um numero
x = int(input("Digite um numero: "))

def tabuada(x):
     for valor in range(11):
          print('{0} x {1} = {2}'.format(x, valor, (x*valor)))
          # esse loop vai repetir dentro do range e imprimir os valores formatados

tabuada(x)