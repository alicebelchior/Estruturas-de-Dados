#  Escreva um script em Python onde uma função deverá receber os dados e calcular a soma dos dígitos de um número inteiro fornecido pelo usuário. O programa deverá informar o resultado da soma dos dígitos

# função soma
def soma(a, b):
     return a+b

a = int(input('a = '))
b = int(input('b = '))
resultado = soma(a, b)
print(f'Resultado: {resultado}')