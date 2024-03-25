# variaveis declaradas fora da função são chamadas pela função
num1 = 10
num2 = 20

def numeros():
     print(f'{num1 + num2}')
     num3 = 40
     
numeros()

# essa variavel não pode ser acessada de fora da função
print(num3)