# Crie um script em Python que deverá calcular a soma de todos os seus elementos. O valor obtido deve ser exibido ao final do programa.

# Declaração da tupla
tupla = tuple([i for i in range(11)])

soma = 0

# soma dos elementos da tupla
for i in tupla:
          soma += i
print(soma)